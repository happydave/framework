# Complete

## Intent

Formally mark a work item as complete by updating its status. This represents the conclusion of all creative and technical work (planning, implementation, review, documentation) and signals that the work item is ready for archival.

Completion is the logical end of the active workflow. It ensures that the state of the work item is explicitly recorded within the artifact itself.

## When to Complete

- All implementation and documentation work for the work item has been verified complete.
- A Reflect action (if executed) has been finalized.
- The work item meets all acceptance criteria defined in `workitem.md` and `plan.md`.

Complete is NOT appropriate when:
- Unresolved blocking findings remain from a Code Review or Plan Review.

## Procedure

### 1. Verify Artifact Presence

Check the work item folder for required artifacts:

- [ ] `code.md` — must be present if the work item involved implementation.
- [ ] `reflect.md` — should be present for non-trivial work items.

### 2. Update Status

Update the `Status` field in `workitem.md` to `complete`.

If a `Completed Date` or similar metadata field is used in the project, update that as well.

### 3. Update Project

Update the work item status in the project doc (if a project is specified).

If this completion **closes a design line or milestone** (its last work item is now complete),
move that line's completed rows and version-history prose from the project's anchor document
into the project's history log **in the same edit**, leaving the anchor a one-line summary +
history link. Anchors carry open work; history carries done work — offloading at the closure
boundary keeps the anchor from silently re-accumulating (the failure mode is rows accreting
until a project assessment forces a cleanup).
