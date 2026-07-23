# Code Review

## Intent

Verify that the changes produced by the Code procedure correctly implement the plan before proceeding to Test. The output is a structured set of findings — blocking issues that must be resolved, non-blocking observations worth noting, and confirmation that the implementation is ready to proceed.

Code Review is a cooperative process: the Agent performs exhaustive mechanical scanning and evaluates changes against the plan; the Reviewer exercises judgment on ambiguous findings and decides what must be resolved before Test begins.

## When to Use

- The Code procedure has completed and `code.md` is up to date.
- Before proceeding to the Test procedure.

## Roles

**Reviewer:**
- Clarifies findings the Agent flags as uncertain
- Judges which findings are blocking vs. acceptable given intent and context
- Decides whether to fix issues in-place or proceed to Test with known non-blocking observations

**Agent:**
- Reads the full diff without fatigue or anchoring bias
- Evaluates changes against the plan's requirements, invariants, and acceptance criteria
- Surfaces mechanical issues that are easy to miss at scale: misspellings, shadowed variables, name mismatches, copy-paste errors, inconsistent changes across similar files
- **Defaults to action**: if a finding has an obvious, good solution, applies the fix directly and notes it in the findings summary
- For findings without an obvious solution, weighs risk before deciding how to proceed (see step 4)
- Stops the pipeline and escalates to the Reviewer only for high-risk decisions where the cost of a wrong call exceeds the cost of pausing

## Procedure

### 1. Agent: Read Context

Read the following before reviewing the diff:

- `plan.md` — the authoritative specification: requirements, invariants, acceptance criteria, and applicable guidelines
- `workitem.md` — original intent and constraints
- `code.md` — what was done, decisions made, and any deviations from the plan

If `code.md` is missing or contains only empty scaffolding, this is a **blocking finding** — report it and do not proceed until it is provided.

Follow any document references in plan.md or workitem.md that are relevant to evaluating correctness (e.g., design docs, linked specifications).

### 2. Agent: Review the Diff

Obtain the local diff (e.g., `git diff` for unstaged, `git diff --cached` for staged, or the set of files modified during the Code procedure).

Read all changed files in full. Do not skim. For each file, identify:

- What category of change this is: substantive (logic, behavior, structure) or mechanical (formatting, whitespace, comment wording, generated code)
- Whether the change corresponds to a requirement or decision recorded in `plan.md` or `code.md`

Produce a brief **change summary** grouping files by category. Flag any changes that are not traceable to the plan or `code.md` — these may be unintended or out-of-scope.

### 3. Agent: Evaluate

Assess all substantive changes across these dimensions:

**Correctness** — does the implementation match what the plan specifies? Check requirements, invariants, and acceptance criteria explicitly. Note any gaps between what was planned and what was built. Per `skills/evidence.md`, do not accept a passing metric as proof a result is correct: where a criterion produces an artifact (a rendered output, a generated file, a document), the review is not complete until that artifact has been examined, not just its summary counts. An `[agent]`-tagged criterion (see `Plan.md`) is one the review is expected to verify this way.

**Safety** — does the change introduce risk? Consider: security vulnerabilities, data loss scenarios, race conditions, inconsistent state, irreversible side effects.

**Clarity** — is the code readable and maintainable? Naming, structure, and whether a future reader would understand the intent without needing to ask the author.

**Tests** — are new behaviors covered? Are existing tests still meaningful? Absence of tests for plan-specified behaviors is a blocking finding.

**Scope** — does the change stay within what the plan specifies? Unrelated or opportunistic changes should be flagged.

**Consistency** — for changes applied across multiple similar files, verify the pattern is applied uniformly. Inconsistencies across similar files are a common source of subtle bugs.

Also scan exhaustively for mechanical issues regardless of change category:

- Misspellings in identifiers, comments, log messages, or documentation
- Shadowed variables or identifier reuse that may mask intent
- Variable or parameter name mismatches
- Copy-paste errors in repeated blocks

### 4. Agent: Report Findings

For each finding, apply one of three responses before reporting:

**Fix directly** — if there is an obvious, good solution: apply it, then include the finding in the summary as resolved. This is the default for linter-class issues, typos, name mismatches, and any substantive issue where the correct fix is unambiguous.

**Decide and proceed** — if there is no obvious solution but the risk is low: make a reasoned choice, apply it, document the rationale, and flag it in the summary for Reviewer awareness. Low risk means the decision is reversible via git and does not affect external contracts, security, or data integrity.

**Stop and escalate** — if there is no obvious solution and the risk is high: halt and surface to the Reviewer before proceeding. High-risk decisions include: security vulnerabilities, data loss scenarios, breaking changes to external APIs or contracts, and scope changes that meaningfully deviate from the plan.

Organize the findings summary into three tiers:

- **Escalations** — decisions stopped for Reviewer input; include what was found, why it is high-risk, and what options exist
- **Resolved** — issues found and fixed, including both direct fixes and decided-and-proceeded cases; include the rationale for any judgment calls
- **Observations** — non-blocking notes the Reviewer may want to be aware of but that do not require action before Test

### 5. Reviewer: Act on Escalations

Review any escalated findings:

- Provide the missing context or make the call the Agent could not
- The Agent then applies the resolution and updates the findings summary

If there are no escalations, no Reviewer action is required — proceed to Test.

## Guidance

- The plan is the primary evaluation standard. A change that works but doesn't match the plan is a finding; a plan gap discovered during review should be noted in `code.md`.
- Default to action. Software can be rewritten and git provides a rollback path — the cost of a recoverable wrong decision is almost always lower than the cost of stopping unnecessarily.
- Escalate sparingly. Escalation is for decisions where recovery would be expensive or impossible: security holes, data loss, broken external contracts, significant unplanned scope. Everything else is low risk by default.
- Distinguish escalations from observations clearly. Treating every finding as a stop trains reviewers to ignore findings; burying real escalations in observations leads to proceeding with unresolved high-risk decisions.
- A short review of a small, well-scoped change is not a failure of rigor — it reflects a change that was ready. Match depth to complexity.
