# Close

## Intent

Formally close a ticket by moving its folder from `docs/pending/` to `docs/complete/`. This action makes explicit what was previously an implicit step — ensuring that completion is deliberate, auditable, and consistent across all ticket types.

Close is the terminal state of the workflow. No further actions follow Close in the normal flow.

## When to Close

- All implementation, testing, and documentation work for the ticket has been verified complete
- A Reflect action (if executed) found no issues requiring new tickets or remediation
- The Author confirms that external tracking systems (issue tracker, project board) are updated if applicable

Close is NOT appropriate when:
- Reflect revealed problems that warrant new tickets — defer Close and create new tickets instead
- An implementer was interrupted mid-session and artifact presence is uncertain — investigate first
- The Reviewer cannot verify required artifacts are present in the ticket folder

## Roles & Responsibilities

**Author** — confirms completion readiness and external state. The Author initiated the work and knows whether it is truly done.

**Reviewer** — verifies artifact presence systematically and executes the folder move. The Reviewer acts as an independent gate to ensure nothing was missed.

## Procedure

### 1. Author: Confirm Completion Readiness

The Author explicitly requests Close by confirming that all implementation, testing, and documentation work is complete. This must be a separate invocation of the Close action — it does not happen automatically when any other action finishes.

### 2. Reviewer: Verify Artifact Presence

Check the ticket folder for required artifacts:

- [ ] `ticket.md` — always present (originating document)
- [ ] `plan.md` — present if the ticket was promoted to a plan; note absence if applicable
- [ ] `implementation.md` — present if the ticket involved implementation; note absence for discovery-only or investigation-only tickets
- [ ] `reflect.md` — present if Reflect was executed; note absence only if the Author confirms reflection is not warranted (e.g., trivial changes)

If any required artifact is missing and its presence was expected, flag this before proceeding. For standalone Discover or Investigate tickets, missing `plan.md` or `implementation.md` is normal and should be noted but not treated as a failure.

### 3. Author: Confirm External State

If the project uses external tracking (issue tracker, project board), confirm those are updated to reflect completion. This step may be skipped for projects without external tracking systems.

### 4. Reviewer: Execute Move

Move the entire ticket folder atomically from `docs/pending/` to `docs/complete/`:

```
mv docs/pending/<id>-<name>/ docs/complete/
```

This is a single directory-level operation. Individual files must not be copied or moved separately. The entire ticket folder — including all artifacts produced during the workflow — moves together.

## Guidance

- If Reflect produces recommendations for immediate action, defer Close and create new tickets. Closing while known issues remain unresolved defeats the purpose of the audit trail.
- Multiple implementers or interrupted sessions are exactly when artifact verification matters most — use this step to ensure no session's work was lost before marking complete.
- The folder move is the only status transition in the workflow. A ticket folder in `docs/pending/` means in progress or not yet started; a ticket folder in `docs/complete/` means done.
