# Merge

## Purpose

Perform a clean, conflict-resolved rebase of a feature branch onto a target branch, producing a linear history with a single well-formed commit per logical concern.

## When to Use

Use when a feature branch has diverged from its target branch to the point where a rebase requires non-trivial conflict resolution, and a linear history with a squashed, ticket-tagged commit is the desired outcome.

Use `GitMerge.md` instead when the strategy itself is the open question (merge vs. squash vs. rebase), when branch history must be preserved, or when the branch is published and cannot be rewritten. `GitMerge.md` selects a strategy and records the rationale; this procedure executes one specific strategy in depth.

> **This procedure rewrites history.** Squash and rebase both rewrite the feature branch. Do not run it on a branch other actors have based work on. If the branch is published to a shared remote, confirm with the requester that a force-push is acceptable before starting; if it is not, use `GitMerge.md` and select the Merge strategy instead.

## Prerequisites

- Working tree is clean. If it is not, stash or commit in-progress changes before starting.
- Target branch has been fetched from origin and the local ref is current.
- The ticket identifier for the branch is known.
- A work item folder exists or is created. The merge artifact lives here.

## Procedure

### Phase 1: Pre-Merge Audit

1. Record the feature branch name and HEAD SHA.
2. Record the target branch name and HEAD SHA.
3. Compute the merge base SHA (`git merge-base HEAD <target>`).
4. Enumerate files changed on the feature branch (vs. merge base).
5. Enumerate files changed on the target branch (vs. merge base).
6. Identify the intersection — files changed on both sides. These are where conflicts will occur **and** where silent logical conflicts may exist even without markers.
7. Classify every file in the intersection:
   - **Standard** — resolve manually
   - **Generated** — re-generate after rebase; do not conflict-resolve
   - **Lock** — re-run the lock tool after rebase; do not conflict-resolve
8. Determine the next available artifact filename in the work item folder (`merge-01.md`, `merge-02.md`, etc.) and create it using the template below. Populate the header and Intersection section immediately.

### Phase 1b: Resolution Planning (optional)

After completing Phase 1, assess the Standard-classified files in the intersection:
- If the intersection is small and the changes are straightforward, proceed to Phase 2.
- If the intersection contains many Standard files, complex logic changes, or the branches have diverged significantly, propose a Resolution Planning pass to the requester before squashing.

If planning is chosen:
1. For each Standard file in the intersection, read both sides on clean history:
   - Target branch diff: `git diff <merge-base> <target> -- <file>`
   - Feature branch diff: `git diff <merge-base> HEAD -- <file>`
2. For each file, populate a row in the artifact Resolution Plan section:
   - What the target branch changed and why (intent)
   - What the feature branch changed and why (intent)
   - Predicted conflict type: none / textual / logical / both
   - Proposed resolution strategy
3. Review the completed plan with the requester before proceeding to Phase 2. Revise any entries where the requester disagrees with the proposed strategy.

The value of this pass is that resolution decisions are made while reading clean, unambiguous code — before conflict markers, cognitive load, and time pressure complicate the picture.

### Phase 2: Squash

1. Determine the number of logical units on the branch. If more than one independent concern is present, **stop and ask the requester how many commits they want**. Do not make this determination silently.
2. Squash the branch commits to the agreed number of logical commits.
3. Each commit message MUST follow this format:
   ```
   TICKET-ID: <one-line description matching the ticket subject>
   ```
4. **Review the full squashed diff before proceeding.** Verify: no debug code, no commented-out blocks, no unresolved TODO markers, no incomplete changes. This is the last clean checkpoint before rebase complexity begins.
5. Update the artifact with the squash commit message.

### Phase 3: Rebase

> **Recovery:** If you need to stop mid-rebase for any reason, `git rebase --abort` returns the branch to its post-squash state. The SHAs captured in Phase 1 are your recovery anchors.

1. Begin the rebase onto the target branch.
> **Side naming during a rebase is reversed relative to a merge.** Commits are replayed *onto* the target branch, so HEAD is the target: `--ours` is the **target branch** and `--theirs` is the **feature-branch commit being applied**. Do not carry merge-time intuition into these commands.

2. For each conflicted file, apply the Phase 1 classification:
   - **Generated** — take the target branch version unconditionally (`git checkout --ours <file>`). Mark resolved. Do not manually edit. Regeneration happens in Phase 5.
   - **Lock** — take the target branch version unconditionally (`git checkout --ours <file>`). Mark resolved. Re-running the lock tool happens in Phase 5.
   - **Standard** — if a Resolution Plan entry exists for this file, follow the planned strategy. Otherwise: read both sides (feature branch and target branch), understand the intent of each change, then write the resolution. Do not resolve from context alone. If the correct resolution is genuinely uncertain, stop and consult the requester.
3. Append each resolved conflict to the Conflicts Resolved section of the artifact before continuing to the next conflict.
4. Run `git rebase --continue`. A rebase may require multiple rounds of conflict resolution if squashing produced more than one commit.
5. Complete the rebase.

### Phase 4: Logical Conflict Check

For every file in the intersection that did **not** produce conflict markers:
- Read both the incoming change (from target) and your change (from feature branch).
- Verify your change is still correct given what changed on the target branch.

Common patterns to look for:
- Symbol renamed on target; feature branch calls the old name (no marker, broken at compile)
- Interface method added on target; feature branch implements the old interface (no marker, broken at compile)
- Behavior changed on target that feature branch logic depends on (no marker, silently wrong)

Note: the build in Phase 5 also catches logical conflicts in files outside the intersection (e.g., your branch adds a new file calling a function removed on the target). Phase 4 and Phase 5 address different failure surfaces; neither substitutes for the other.

**4b. Master-only additions.** List all files added exclusively by the target branch (present in target HEAD, absent in the merge base and in the feature branch). For each such file, check whether the feature branch changed any interface, function signature, type, or constant that the file references. If so, update the file to match the feature branch's current API.

Record findings — or "none found" — in the artifact before proceeding to Phase 5.

This phase is not optional. A clean rebase is not a correct rebase.

### Phase 5: Post-Rebase Verification

1. Regenerate all generated files that were in the intersection.
2. Re-run lock file tools for any lock files that were in the intersection (e.g., `go mod tidy`, `npm install`).
3. Run the full build.
4. Run the full test suite. Do not use short or filtered runs.
5. If the build or tests fail: verify whether the same failure exists on the target branch before concluding the merge caused it. A failure that pre-exists on the target is not a merge failure.
6. Update the artifact Verification section with results.
7. All steps must pass before the merge is considered complete. If failures remain after investigation, stop and consult the requester.

### Phase 6: Completion

1. Set the artifact Status to `complete` and record the final branch HEAD SHA.
2. Inform the requester: the merge is complete and the artifact is in the work item folder.

## Artifact Template (`merge-NN.md`)

```markdown
# Merge: <TICKET-ID>
**Date:** YYYY-MM-DD
**Feature Branch:** `<name>` @ `<SHA>`
**Target Branch:** `<name>` @ `<SHA>`
**Merge Base:** `<SHA>`

## Intersection
| File | Classification |
|---|---|

## Resolution Plan
<!-- Optional — populated during Phase 1b for complex merges. Omit for simple merges. -->

| File | Target Change (intent) | Feature Change (intent) | Conflict Type | Resolution Strategy |
|---|---|---|---|---|

## Squash Commit
<commit message>

## Conflicts Resolved
<!-- If an actual resolution differs from the Resolution Plan, note the divergence and the reason in the row. -->
| File | Resolution |
|---|---|

## Logical Conflict Check
<!-- Describe any logical conflicts found and how resolved. "None found" if clean. -->

## Verification
- [ ] Generated files regenerated
- [ ] Lock files regenerated
- [ ] Build: pass / fail
- [ ] Tests: pass / fail

**Final HEAD:** `<SHA>`
**Status:** in-progress / complete / aborted
```

## Invariants

- The feature branch MUST NOT have other actors' work based on it; rewriting published history requires explicit requester confirmation.
- The working tree MUST be clean before starting.
- The target branch ref MUST be current (fetched from origin) before starting.
- The squash commit message MUST begin with the ticket identifier.
- Generated files MUST be regenerated, not conflict-resolved.
- Lock files MUST be regenerated by their tool, not conflict-resolved.
- The full test suite MUST pass after rebase.
- Logical conflicts MUST be reviewed even when no conflict markers exist.
- A `merge-NN.md` artifact MUST exist in the work item folder and MUST be kept current throughout.

## Explicit Agent Freedom

The agent has discretion over:
- Specific git commands used to accomplish each phase
- How to enumerate changed files (git log, git diff, etc.)
- Order of conflict resolution within a single rebase step
- How to identify generated and lock files (by path pattern, `.gitattributes`, project convention, etc.)
- The exact number suffix for the artifact filename (next available)
