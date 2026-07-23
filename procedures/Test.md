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

### 3. Produce `test.md`

Document the testing process and results in a `test.md` file within the work item folder.

#### Required Sections:
- **Test Summary**: High-level pass/fail status and summary of coverage.
- **Automated Results**: Output or summary of test suite executions.
- **Manual Verification**: Description of manual steps taken and their outcomes.
- **Findings**: A clearly enumerated list of all problems found.

### 4. Handle Findings

All findings in `test.md` must be addressed:

- **Minor Issues**: Bugs, typos, or minor deviations should be corrected immediately. Re-run affected tests to verify the fix.
- **Significant Issues**: If a finding requires design changes, significant architectural changes, or falls outside the scope of the current work item/project design:
    - Do NOT implement the change immediately.
    - Document the issue clearly in `test.md`.
    - Suggest the creation of one or more new work items to address the issue.
    - Consult the user/reviewer to decide if the current work item can proceed to completion or if it is blocked.

## Guidance

- **Negative Testing**: Always include test cases for invalid input, error states, and boundary conditions.
- **Evidence-Based**: Where possible, include logs, screenshots, or command output in `test.md`. Apply `skills/evidence.md`: report each result at the confidence the evidence supports, and remember that passing automated metrics does not verify a result until the artifact behind it is examined (a build that produces a file with the right shape can still produce the wrong file).
- **No Guesswork**: If it's unclear how to test a specific component, refer back to the `Discover` procedure or ask the user for clarification.
