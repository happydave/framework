#!/usr/bin/env python3
"""Flag repeated word blocks within Markdown documents.

Implements the duplicate-detection heuristic from skills/markdown.md: any block of
8 or more consecutive words that appears more than once within the same document is
reported for review. Detection is per-file — repetition across different files is
normal and is not reported.

Results are advisory, not a build gate: finding duplicates is a successful run and
exits 0. A non-zero exit means the tool could not do its job (bad arguments, or a
path it could not read).

YAML frontmatter and fenced code blocks are excluded by default, because repeated
command lines and frontmatter keys are legitimate repetition that would otherwise
dominate the output. Pass --include-code to analyze fenced blocks too. Tables are
analyzed as ordinary text, since repetition across rows is the copy-paste error
this check exists to catch.

Usage:
    internal/dupcheck.py FILE [FILE ...]
    internal/dupcheck.py -n 12 docs/pending/*/plan.md
    internal/dupcheck.py --self-test
"""

import argparse
import re
import sys

DEFAULT_MIN_WORDS = 8

# A token is a run of non-whitespace with leading/trailing punctuation stripped, so
# "deleted." and "deleted," match while service_number and 3.26.3 stay intact.
_TRIM = re.compile(r"^[^0-9A-Za-z_]+|[^0-9A-Za-z_]+$")
_FENCE = re.compile(r"^\s*(```|~~~)")


def tokenize(text, include_code=False):
    """Return [(word, line_number)] for a document, lowercased and trimmed."""
    lines = text.splitlines()
    start = 0

    # Skip YAML frontmatter: a leading '---' line through the next '---' line.
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break

    tokens = []
    in_fence = False
    for offset, line in enumerate(lines[start:], start=start + 1):
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence and not include_code:
            continue
        for raw in line.split():
            word = _TRIM.sub("", raw).lower()
            if word:
                tokens.append((word, offset))
    return tokens


def find_duplicates(text, min_words=DEFAULT_MIN_WORDS, include_code=False):
    """Find maximal repeated word blocks.

    Returns [(word_count, occurrences, [line_numbers], text)] sorted longest first.
    Only maximal blocks are returned: a repeated 12-word span is reported once as 12
    words, not as five overlapping 8-word findings. Occurrences are counted by start
    position, so two copies on one line still count as two.
    """
    tokens = tokenize(text, include_code=include_code)
    words = [w for w, _ in tokens]
    # Two distinct start positions need at least one token more than the block length.
    if len(words) <= min_words:
        return []

    # Group start positions by their min_words-long opening n-gram.
    starts = {}
    for i in range(len(words) - min_words + 1):
        starts.setdefault(tuple(words[i:i + min_words]), []).append(i)

    findings = {}
    for positions in starts.values():
        if len(positions) < 2:
            continue
        for a_index, a in enumerate(positions):
            for b in positions[a_index + 1:]:
                # Left-maximality: if the preceding words also match, this pair is
                # the tail of a longer match that will be reported on its own.
                if a > 0 and b > 0 and words[a - 1] == words[b - 1]:
                    continue
                # Extend right as far as the two spans agree.
                length = min_words
                while (b + length < len(words)
                       and words[a + length] == words[b + length]):
                    length += 1
                key = tuple(words[a:a + length])
                seen_at = findings.setdefault(key, set())
                seen_at.add(a)
                seen_at.add(b)

    results = []
    for key, seen_at in findings.items():
        lines = sorted({tokens[p][1] for p in seen_at})
        results.append((len(key), len(seen_at), lines, " ".join(key)))
    results.sort(key=lambda r: (-r[0], r[2]))
    return results


def report(path, results, out=sys.stdout):
    """Print one file's findings. Returns the number of findings."""
    if not results:
        print(f"{path}: no repeated blocks", file=out)
        return 0
    label = "block" if len(results) == 1 else "blocks"
    print(f"{path}: {len(results)} repeated {label}", file=out)
    for count, occurrences, lines, text in results:
        where = ", ".join(str(n) for n in lines)
        plural = "line" if len(lines) == 1 else "lines"
        print(f"  {count} words, {occurrences} occurrences ({plural} {where}):", file=out)
        print(f"    {text}", file=out)
    return len(results)


CASES = [
    # (name, text, min_words, expected (word_count, occurrence_count) tuples)
    ("duplicate reported as one maximal block",
     "the album is deleted and the photo count is decremented for the panel.\n"
     "Filler words go here to separate the two passages from each other.\n"
     "the album is deleted and the photo count is decremented for the panel.\n",
     8, [(13, 2)]),
    ("clean file reports nothing",
     "Each sentence here is entirely distinct from every other sentence.\n"
     "No block of eight consecutive words recurs anywhere within this file.\n",
     8, []),
    ("threshold override finds a shorter block",
     "alpha beta gamma delta epsilon zeta\nalpha beta gamma delta omega\n",
     4, [(4, 2)]),
    ("default threshold ignores a short block",
     "alpha beta gamma delta epsilon zeta\nalpha beta gamma delta omega\n",
     8, []),
    ("three occurrences collapse into one finding",
     "one two three four five six seven eight nine\nfiller here\n"
     "one two three four five six seven eight nine\nmore filler\n"
     "one two three four five six seven eight nine\n",
     8, [(9, 3)]),
    ("fenced code blocks are excluded",
     "```\nrepeat this exact command line again and again and again please\n```\n"
     "```\nrepeat this exact command line again and again and again please\n```\n",
     8, []),
    ("frontmatter is excluded",
     "---\ntitle: a title that is long enough to trip the check on its own\n---\n"
     "Body text that does not repeat anything at all.\n",
     8, []),
    ("punctuation and case do not block a match",
     "The album is deleted, and the photo count drops.\nunrelated filler line\n"
     "the album is deleted. And the photo count drops!\n",
     8, [(9, 2)]),
    ("two copies on one line count as two occurrences",
     "the album is deleted and the count drops "
     "the album is deleted and the count drops\n",
     8, [(8, 2)]),
    ("a block repeated just past the minimum length is still found",
     "alpha beta gamma delta epsilon zeta eta theta alpha beta gamma delta "
     "epsilon zeta eta theta\n",
     8, [(8, 2)]),
    ("empty input is not an error",
     "", 8, []),
]


def self_test(out=sys.stdout):
    """Run embedded known-answer cases. Returns True when all pass."""
    failures = 0
    for name, text, min_words, expected in CASES:
        results = find_duplicates(text, min_words=min_words)
        actual = [(count, occurrences) for count, occurrences, _, _ in results]
        if actual == expected:
            print(f"PASS  {name}", file=out)
        else:
            failures += 1
            print(f"FAIL  {name}\n      expected {expected}\n      actual   {actual}",
                  file=out)
    total = len(CASES)
    print(f"\n{total - failures}/{total} cases passed", file=out)
    return failures == 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=("Flag repeated word blocks within Markdown documents "
                     "(skills/markdown.md duplicate-detection heuristic). "
                     "Advisory: finding duplicates exits 0."),
        epilog=("YAML frontmatter and fenced code blocks are excluded unless "
                "--include-code is given. Detection is per-file; repetition "
                "across files is not reported."))
    parser.add_argument("files", nargs="*", metavar="FILE",
                        help="Markdown files to analyze")
    parser.add_argument("-n", "--min-words", type=int, default=DEFAULT_MIN_WORDS,
                        help=f"minimum block length in words (default {DEFAULT_MIN_WORDS})")
    parser.add_argument("--include-code", action="store_true",
                        help="analyze fenced code blocks as well")
    parser.add_argument("--self-test", action="store_true",
                        help="run the tool's own known-answer cases and exit")
    args = parser.parse_args(argv)

    if args.self_test:
        return 0 if self_test() else 1
    if not args.files:
        parser.error("no files given (use --self-test to verify the tool itself)")
    if args.min_words < 2:
        parser.error("--min-words must be at least 2")

    unreadable = []
    for path in args.files:
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError as err:
            # Keep going: a stale path in a glob must not abandon the rest.
            print(f"{path}: cannot read ({err.strerror})", file=sys.stderr)
            unreadable.append(path)
            continue
        report(path, find_duplicates(text, args.min_words, args.include_code))

    return 1 if unreadable else 0


if __name__ == "__main__":
    sys.exit(main())
