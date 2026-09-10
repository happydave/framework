# Test

## Intent

Formally verify the implementation against requirements, acceptance criteria, and quality standards. This procedure ensures that the changes work as intended, do not introduce regressions, and meet the technical requirements defined in the planning phase.

## When to Test

- Implementation is complete and documented in `code.md`.
- Code review has been finalized (or is being conducted in parallel with testing).
- The changes are ready for final verification before documentation and completion.

## Input & Guidance Priority

Test guidance may be found in multiple locations. When conflicting or overlapping guidance exists, follow this priority order:

1.  **Work Item Plan** (`plan.md`): Specific test cases, edge cases, and acceptance criteria defined for this work item.
2.  **Project README/Manifest**: Project-wide testing standards, required test suites, or environment configurations.
3.  **Language/Framework Guidelines**: General best practices for the specific technology stack (e.g., `Go.md`, `TypeScript.md`).

## Roles & Responsibilities

**Author** — executes automated tests, performs manual verification, and records results.

**Reviewer** — verifies that the test coverage is sufficient and that all findings have been addressed or triaged.

## Procedure

### 1. Identify Test Requirements

Gather testing instructions from the sources identified in the **Input & Guidance Priority** section. List all required:
- Unit tests
- Integration tests
- Manual verification steps
- Performance or security checks (if applicable)

### 2. Execute Tests

Run the identified test suites and perform manual verification. If any steps require human intervention (e.g., UI verification, hardware interaction), the AI agent must explicitly ask the user to perform these steps and report the results.

### 3. Run the Negative Controls

A test that passes against a deliberately broken implementation is not evidence. For each behavior the plan specifies in its **Required Behaviors & Verifications**, remove or invert that behavior and confirm the intended tests fail — and that they fail on the cases that target it. The scope is the plan's behaviors: not every new test, and not every line of the change. Before breaking anything, read the next paragraph — it constrains which behaviors may be checked this way at all.

**Before breaking anything, check what the behavior guards.** Where it guards a destructive, irreversible, or outward-facing operation, run the control against the predicate that decides, never by driving the operation itself — see *A destructive operation decides in a pure predicate* in `AGENTS.md`. Where the decision is not separable from the act, do not run the control: the non-separability is itself the finding, and the restructuring comes first. A control is run *with the guard removed*, so a control that reaches the operation performs it.

The shape this asks for is small. In hoardmq's failover driver, `validateStoreRoot` decides — it inspects a path and touches nothing — `removeStore` calls it before `os.RemoveAll`, and the guard's test asserts on `validateStoreRoot`, passing it `/`, `/etc` and the home directory precisely because a predicate cannot act on them. A second test hands `removeStore` only a directory it created itself. Breaking that guard fails the test and removes nothing; that was verified by running exactly this control. An earlier version of the same guard was written inline and tested by calling the remover with those same arguments — running the identical check against it destroyed a host's home directory.

Which cases fail matters as much as that something failed. A mutation that breaks more cases than expected, or fewer, has located a gap. In md-mcp WI 1169 a mutation passed the entire suite and revealed that the invariant the plan had singled out as the subtle one had no test at all — every other case was byte-identical either way, so the assertions that appeared to cover it did not.

Record the result in `test.md` as a table of the break, the test, and the failure observed. Where a control could not be run — a behavior that will not compile once removed, or an operation whose decision is not separable — name the behavior and the reason. An omitted control must not be indistinguishable from one that passed.

This is `skills/evidence.md`'s "actively seek contradictory evidence" applied to the suite itself: a control that *should* fail is what distinguishes a test with teeth from a test that agrees with whatever it is given.

### 4. Produce `test.md`

Document the testing process and results in a `test.md` file within the work item folder.

#### Required Sections:
- **Test Summary**: High-level pass/fail status and summary of coverage.
- **Automated Results**: Output or summary of test suite executions.
- **Manual Verification**: Description of manual steps taken and their outcomes.
- **Negative Controls**: the table of breaks run, the tests they broke, and the failures observed — or, where none were run, which behaviors went uncontrolled and why.
- **Findings**: A clearly enumerated list of all problems found.

### 5. Handle Findings

All findings in `test.md` must be addressed:

- **Minor Issues**: Bugs, typos, or minor deviations should be corrected immediately. Re-run affected tests to verify the fix.
- **Significant Issues**: If a finding requires design changes, significant architectural changes, or falls outside the scope of the current work item/project design:
    - Do NOT implement the change immediately.
    - Document the issue clearly in `test.md`.
    - Suggest the creation of one or more new work items to address the issue.
    - Consult the user/reviewer to decide if the current work item can proceed to completion or if it is blocked.

## Guidance

- **Negative Testing**: Always include test cases for invalid input, error states, and boundary conditions. **An assertion of absence must first establish the presence it qualifies** — a test that is satisfied when the thing it guards never happens at all passes while proving nothing. Assert that the value reaches the output, then assert how it appears there. This matters most for escaping, injection, redaction, and secret-scanning checks, where a vacuous test reads as security coverage: raji-local-mcp's reflected-input test asserts the hostile value is echoed at all *before* asserting that it is echoed escaped, and says so in a comment. The timing case is the same rule — when a test asserts that a disabled or detached component receives *nothing*, precede the assertion with a wait for the last event that was expected to arrive, otherwise the assertion can pass simply because it ran before anything was delivered. The converse shape is a content scan, which is scoped to the artifact's code rather than its prose, so a check cannot trip on documentation of itself.
- **Evidence-Based**: Where possible, include logs, screenshots, or command output in `test.md`. Apply `skills/evidence.md`: report each result at the confidence the evidence supports, and remember that passing automated metrics does not verify a result until the artifact behind it is examined (a build that produces a file with the right shape can still produce the wrong file).
- **No Guesswork**: If it's unclear how to test a specific component, refer back to the `Discover` procedure or ask the user for clarification.
