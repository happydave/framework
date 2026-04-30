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

Projects are documented in a central location (e.g., a `tickets` repository), not within individual code repositories.

Each project gets its own folder under `docs/projects/`, named with a slug (kebab-case). The primary document is always named `project.md`.

- `docs/projects/new-api-framework/project.md`

The project folder also contains:
- `design.md`: The architectural design for the project (see `Design.md`).
- `archive/`: A folder where completed work items associated with this project are moved.

## Required Content

Every `project.md` must include:

- **Title** — a concise name for the project.
- **Status** — `New`, `Designed`, or `Active`. Starts as `New`.
- **Purpose** — the high-level "why" and "what" of the project.
- **Scope** — the boundaries of the project, including which repositories or systems are involved.
- **Backlog** — a list of Work Item IDs associated with this project and their current status.

## Procedure

1. **Initiate** — create the project folder and `project.md` with the Title, Purpose, and Scope. Set Status to `New`.
2. **Discovery (Optional)** — if the project requires research before design, follow `Discover.md`.
3. **Design** — produce a high-level design following `Design.md`.
4. **Design Review** — subject the design to a formal review following `DesignReview.md`. Upon approval, update project status to `Designed`.
5. **Decomposition** — break the design down into individual Work Items. Create these in the central `docs/pending/` directory, linking each back to the project.
6. **Execution** — manage the execution of work items. Update the project's Backlog as work progresses.

## Status Tracking

- **New**: Project initiated, design not yet completed or approved.
- **Designed**: Design has passed Design Review.
- **Active**: Work items are being implemented.
- **Completed**: (Future) All work items are finished and the project goal is met.

Status updates are manual for now.
