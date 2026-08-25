# Design Review

## Intent

Independently evaluate a Project's `design.md` to ensure it is technically sound, aligns with project goals, and provides a clear path for decomposition into work items. The Design Review is a critical gate that prevents architectural misalignment from reaching the implementation phase.

## When to Conduct a Design Review

- A Project's `design.md` has been drafted and is ready for scrutiny
- Significant changes are made to an existing Project's architecture

## Procedure

1. **Submit** — the Author presents the `design.md` to the Reviewer.
2. **Evaluate** — the Reviewer audits the design against the following criteria:
    - **Alignment**: Does the design solve the problem defined in the Project's purpose?
    - **Completeness**: Are all significant components, interfaces, and data models addressed?
    - **Feasibility**: Can this design be implemented within the project's constraints?
    - **Maintainability**: Does the design follow established patterns and avoid unnecessary complexity?
    - **Observability**: Are there clear hooks for monitoring and debugging?
    - **Security/Performance**: Are non-functional requirements adequately addressed?
3. **Feedback** — the Reviewer provides specific, actionable feedback or asks clarifying questions.
4. **Resolution** — the Author addresses feedback, updating the `design.md` as needed.
5. **Approval** — once the Reviewer is satisfied, the Design Review is complete. Under a self-applied review (below), "satisfied" means no finding remains unresolved or undispositioned, with the artifact on disk as the evidence a later reader can check.

## Self-Applied Review

Design Review is preferably performed by a reviewer other than the design's author. When no external reviewer is available, the author performs the review directly in the same session — the gate is never skipped, and "no reviewer available" is not a disposition. Under self-application:

- All evaluation criteria are assessed and the findings recorded in the artifact (see Document Storage), which SHALL record the review mode (`external` or `self-applied`).
- A finding SHALL NOT be dismissed on the author's preference alone. A dismissal cites evidence: an opened file, a recorded decision, a stated project constraint.
- Findings that hinge on a judgment only the owner can make — product direction, scope trade-offs, acceptance of risk — are recorded in the artifact as open questions rather than silently resolved. The Outcome may still trigger with those questions visible for the owner to revisit; that is what keeps a self-applied review from becoming a self-granted approval.

## Document Storage

The review produces an artifact stored beside the design it reviews, in the project folder — not in a work item folder, since Design Review gates a project rather than a work item:

- `designreview.md` — reviews `design.md`
- `designreview-<aspect>.md` — reviews `design-<aspect>.md`, for projects carrying more than one design

The artifact contains: **Status** (Approved, or Revisions Required), **Review Mode** (`external` or `self-applied`), and **Findings** organized by the evaluation criteria, each with a disposition (resolved, design revised, or open question for the owner). Keep it proportionate — a short review of a small design is appropriate.

The spellings `design-review.md`, `design-<aspect>-review.md`, and `artifacts-design-review.md` appear in older artifacts and are non-canonical; do not create new files with these names.

## Outcome

Successful completion of a Design Review triggers:
1. Update the Project's status to `Designed`.
2. Authorization to begin creating Work Items in `docs/pending/` based on the approved design.

## Guidance

- Design Review is about architecture and strategy, not implementation details.
- Be critical of complexity. The best designs are often the simplest ones that meet the requirements.
- Ensure that the design is "decomposable" — it should be clear how to break it into independent work items.
