# Design

## Intent

Establish the high-level architectural blueprint for a Project. Design documents focus on the "how" at a system or multi-component level, ensuring that individual work items will fit together into a cohesive whole.

Design is broader than Planning. While a Plan (`plan.md`) details changes for a specific work item, a Design (`design.md`) details the architecture, data models, and interface contracts for a Project.

## When to Design

- A Project has been initiated and its purpose is understood
- High-level architectural decisions need to be made before work items can be defined
- Changes affect multiple repositories or services
- New patterns or standards are being introduced to the codebase

## Document Storage & Naming

The design document (a prose artifact) lives within the project folder in all modes:

- `docs/projects/<slug>/design.md`

## Required Content

Every `design.md` must include:

- **Context** — a brief reminder of the Project's purpose.
- **Architectural Overview** — a high-level description of the solution. Diagrams (Mermaid) are encouraged.
- **Key Components** — description of the primary modules, services, or layers involved.
- **Data Models / Schemas** — definitions of significant data structures or database changes.
- **Interfaces / APIs** — contract definitions for communication between components.
- **Non-Functional Requirements** — performance, security, scalability, or observability constraints.
- **Alternatives Considered** — why this design was chosen over other options.

## Procedure

1. **Draft** — create the `design.md` and document the proposed architecture.
2. **Review** — follow the `DesignReview.md` procedure to ensure the design meets the project goals and technical standards.
3. **Iterate** — update the design based on review feedback.
4. **Approve** — once approved, the design serves as the foundation for decomposing the project into Work Items.

## Decision Records

Designs and project docs stamp decisions ("matrix rows are two-column", "951 superseded") that
later change for good reasons. Handle that change ADR-style — the record is append-only:

- A decision entry is **dated** and states the decision plus a one-line why.
- **Never rewrite a stamped decision in place.** Superseding one means appending a new dated
  entry that names what it replaces and why — the old entry survives as the explanation for why
  artifacts built under it look the way they do. Git history alone is not the record; the doc
  itself must show the succession.
- This applies equally when the original decision was simply wrong: corrections are new entries
  too.
- The discipline binds decisions once **stamped** — a design under active drafting (pre-approval)
  is still a living document and may be edited freely, per the Guidance below. The binding point
  is design approval, or the moment a decision is recorded as settled in a project doc.
- Relation to **Alternatives Considered**: that section is point-in-time rationale for the
  drafted shape; decision records are dated commitments whose later changes must stay traceable.
  (World-facts rather than intent follow the codex claim-lifecycle supersession convention in the
  lore vault instead.)

## Guidance

- Focus on the "High-Level Invariants" that must be true across all work items.
- Avoid over-specifying details that belong in a work item's `plan.md`.
- Use the Design phase to resolve cross-cutting concerns (e.g., "How will we handle authentication across these three repos?").
- The Design document is a living document during the Design phase, but should become relatively stable once the project moves to Execution.
- **Avoid code in design documents.** Express concepts, intent, and structure in prose. Specific implementations, struct definitions, and function signatures belong in the planning and implementation phases where an implementer can make the right choices in context. Exceptions are appropriate when a specific interface must be fixed for compatibility reasons, or when documenting an external API contract.
