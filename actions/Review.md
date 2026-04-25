# Review

## Intent

Evaluate a merge request thoroughly and produce clear, actionable feedback. The output is a structured set of observations — concerns, questions, and approvals — that helps the author understand what needs to change and why, or confirms the change is ready to merge.

Review is a cooperative process: the AI performs exhaustive mechanical scanning and surfaces findings; the human provides intent context, exercises judgment on ambiguous findings, and delivers the final verdict. Neither does this well alone — the AI catches what fatigued human eyes miss across large or repetitive diffs; the human understands system intent, team conventions, and acceptable risk in ways the AI cannot fully infer.

## When to Review

- A merge request has been submitted and is awaiting review
- A reviewer has been assigned or has volunteered to evaluate a change
- A draft MR is being shared for early feedback before it is ready to merge

## Roles

**Human:**
- Provides the MR context and any background the AI needs (linked tickets, intent not captured in the description, relevant system knowledge)
- Clarifies findings the AI flags as uncertain
- Judges which findings are actually blocking vs. acceptable given team context
- Delivers the final verdict and posts comments to the MR

**AI:**
- Reads the full diff without fatigue or anchoring bias
- Scans exhaustively for mechanical issues across all files, including large and repetitive changesets
- Surfaces subtle issues that are easy to miss at scale: misspellings, shadowed variables, variable name mismatches, copy-paste errors, inconsistent changes across similar files
- Distinguishes linter-class changes (whitespace, comment formatting, trivial rewordings) from substantive changes, so the human can focus attention appropriately
- Evaluates each change against the dimensions below and reports findings with enough specificity for the human to act on them

## Procedure

### 1. Human: Establish Context

Before the AI reads the diff, provide:

- The MR title, description, and any linked tickets or planning documents
- Any background not captured in the MR itself: what system behavior is changing, what problem is being solved, relevant constraints
- Any areas of particular concern or focus (e.g., "pay attention to the error handling in the retry logic")

If the MR description is absent or insufficient, note this — it is itself a finding. A reviewable MR should be self-describing.

### 2. AI: Read and Categorize the Diff

Read all changed files in full. Do not skim. For each file, identify:

- What category of change this is: substantive (logic, behavior, structure) or mechanical (formatting, whitespace, comment wording, generated code)
- What has changed and why, based on the description and code context

Produce a brief **change summary** grouping files by category. This orients the human and makes clear where scrutiny is most needed. Large volumes of mechanical changes should be called out explicitly so the human is not lulled into treating them as low-risk without confirmation.

### 3. AI: Evaluate

Assess all substantive changes across these dimensions:

**Correctness** — does the code do what the description says it should? Are there logic errors, off-by-one cases, incorrect assumptions about data, or edge cases that are unhandled?

**Safety** — does the change introduce risk? Consider: security vulnerabilities, data loss scenarios, race conditions, inconsistent state, backward-incompatible changes to APIs or contracts, irreversible side effects.

**Clarity** — is the code readable and maintainable? Consider: naming, structure, comments where non-obvious logic is present, and whether a future reader would understand the intent without needing to ask the author.

**Tests** — are the changes adequately tested? Are new behaviors covered? Are existing tests still meaningful, or do they need updating? Absence of tests is worth noting explicitly, not silently accepting.

**Scope** — does the change stay within its stated purpose? Unrelated or opportunistic changes mixed into an MR increase review surface and risk.

**Consistency** — does the change follow the conventions, patterns, and style of the codebase? For large MRs with many similar files, verify that the pattern is applied uniformly — inconsistencies across similar files are a common source of subtle bugs.

Also scan exhaustively for mechanical issues regardless of change category:

- Misspellings in identifiers, comments, log messages, or documentation
- Shadowed variables or identifier reuse that may mask intent
- Variable or parameter name mismatches (e.g., a renamed variable used inconsistently)
- Copy-paste errors in repeated blocks
- Inconsistent application of a change across files that should be identical

### 4. AI: Report Findings

Organize findings into three tiers:

- **Blocking** — must be resolved before merge: correctness errors, safety risks, missing required tests, inconsistencies that could cause runtime failures
- **Non-blocking** — worth addressing but do not block merge: clarity improvements, naming suggestions, minor structural observations
- **Linter-class** — mechanical changes only (whitespace, comment rewording, generated code churn): call these out as a group rather than line by line, and flag any that are unexpectedly large or mixed with substantive changes

For each blocking and non-blocking finding: state what it is, where it is, and why it matters. Be specific enough that the author knows exactly what to address.

Flag findings as **uncertain** when the concern depends on intent or system context the AI cannot fully determine. These are handed to the human for judgment rather than presented as definitive.

### 5. Human: Review Findings and Decide

Review the AI's findings:

- Confirm or dismiss uncertain findings based on system knowledge and team context
- Reclassify any findings where the AI's blocking/non-blocking judgment does not match the team's standards
- Identify anything the AI missed that requires manual scrutiny (integration behavior, deployment implications, operational concerns)

### 6. Human: Deliver the Review

Post feedback to the MR. Inline comments for findings tied to specific lines; a top-level summary comment for the overall verdict and any general observations.

A good review comment:
- States the concern and why it matters
- Is specific enough that the author knows what to address
- Suggests a direction when one is obvious, without dictating implementation when the author is better positioned to decide

Conclude with a verdict: approve, request changes, or (if genuinely uncertain) state what additional information is needed.

## Guidance

- Establish context before the AI reads the diff. Reviewing a changeset without knowing its intent produces surface-level findings.
- Treat linter-class changes as a distinct category, not as evidence of low risk. A large batch of formatting changes can obscure a substantive change mixed in among them.
- Uncertain findings are not noise — they are the AI surfacing something it cannot resolve alone. Give them deliberate attention rather than dismissing them wholesale.
- Distinguish blocking from non-blocking clearly. A review where everything looks like a blocker trains authors to ignore feedback. A review where real blockers are buried in suggestions trains authors to merge prematurely.
- Be specific. "This might have a race condition" is less useful than "if two goroutines call this concurrently before the lock is initialized, both may see a nil pointer."
- For large MRs with many similar files, explicitly verify uniform application of the intended pattern. The AI should flag inconsistencies; the human should confirm they are not intentional.
- A short review of a small, well-scoped MR is not a failure of rigor — it reflects an MR that was ready. Match depth to complexity.
- Approve when the change is ready. Withholding approval as leverage or out of excessive caution blocks good work and erodes trust in the review process.
