# Project

## Intent

Define a high-level goal or initiative that requires multiple work items to achieve. A project provides the context, vision, and architectural direction that individual work items must align with. It serves as an orchestration layer rather than a place for code changes.

## When to Create a Project

- A goal is too large or complex for a single work item
- An initiative involves changes across multiple repositories
- A "discovery" phase reveals a significant new feature area that needs structured decomposition
- Any time high-level design and architectural oversight are needed before breaking down work

Projects are "never finished" in the traditional sense; they exist as long as the initiative is active. They can be archived once all associated work items are completed and the goal is met.

## Document Storage & Naming

Projects are documented in a central location (e.g., a `tickets` repository), not within individual code repositories. Each project has a folder at `docs/projects/<slug>/` which holds the project record and prose artifacts:

- `design.md`: The architectural design for the project (see `Design.md`).
- `archive/`: A folder where completed work items associated with this project are moved.

## Required Content

Every project record must include:

- **Title** — a concise name for the project.
- **Status** — `active`, `inactive`, or `archived`. Starts as `active`.
- **Purpose** — the high-level "why" and "what" of the project.
- **Scope** — the boundaries of the project, including which repositories or systems are involved.

## Optional Content

- **Backlog** — a list of Work Item IDs associated with this project and their current status.
- **Decisions** — dated, append-only decision entries. Settled decisions recorded in a project
  doc follow the Decision Records convention in `Design.md`: supersede by appending a new dated
  entry that names what it replaces and why — never by rewriting the stamped original.

## Procedure

1. **Initiate** — create `docs/projects/<slug>/project.md` with the Title, Purpose, Scope, and Status set to `active`.
2. **Discovery (Optional)** — if the project requires research before design, follow `Discover.md`.
3. **Design** — produce a high-level design following `Design.md`.
4. **Design Review** — subject the design to a formal review following `DesignReview.md`.
5. **Decomposition** — break the design down into individual Work Items following the WorkItem procedure, linking each back to the project.
6. **Execution** — manage the execution of work items.

## Status Tracking

- **active**: Project is being actively worked on.
- **inactive**: Project is paused or deprioritized.
- **archived**: All work items are finished and the project goal has been met.

Status updates are manual.
