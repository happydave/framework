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
5. **Approval** — once the Reviewer is satisfied, the Design Review is complete.

## Outcome

Successful completion of a Design Review triggers:
1. Update the Project's status to `Designed`.
2. Authorization to begin creating Work Items in `docs/pending/` based on the approved design.

## Guidance

- Design Review is about architecture and strategy, not implementation details.
- Be critical of complexity. The best designs are often the simplest ones that meet the requirements.
- Ensure that the design is "decomposable" — it should be clear how to break it into independent work items.
