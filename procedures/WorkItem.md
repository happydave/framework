# Work Item

## Intent

Capture a potential work item — a feature idea, bug report, improvement, or observation — as a lightweight record in a centralized `docs/pending/` directory. Work items are intake documents, not plans. They preserve enough context for later triage and planning without requiring deep analysis at the time of creation.

Work items may originate from any source: an external issue tracker, a conversation, a problem encountered during implementation, or an idea that surfaces opportunistically during unrelated work. The goal is to capture it before the context is lost.

## When to Create a Work Item

- A feature idea or enhancement is identified
- A bug or unexpected behavior is discovered during testing or usage
- An external request or issue needs to be tracked
- A project design is being decomposed into actionable steps
- Any time the thought "we should do X" arises and X is not already tracked

Do not defer capture. A brief work item written now is more valuable than a detailed one never written.

## Document Storage & Naming

Work items are stored in a central management repository (e.g., `tickets`), not in individual code repositories.

Each work item gets its own folder under `docs/pending/`, named with an identifier and short description in kebab-case. The intake document inside is always named `workitem.md`.

Two naming conventions are supported for the folder:

- **Sequential numbering** (default): `docs/pending/07-investigate-pipeline-jobs/workitem.md`
- **External identifier** (when available): `docs/pending/PROJ-123-investigate-pipeline-jobs/workitem.md`

Sequential numbers use two-digit prefixes and reflect creation order, not priority or implementation order. When an external system (issue tracker, project board) provides an identifier, use it as the prefix instead.

The folder is the home for all artifacts related to this work item. As the work progresses through planning and implementation, additional files are added to the same folder (see Plan and Implement actions). When work is complete, the entire folder moves from `docs/pending/` to `docs/archive/` following the procedure in Archive.

## Required Content

Every `workitem.md` must include:

- **Title** — a concise description of the work item.
- **Status** — the current state of the work item (e.g., `pending`, `complete`).
- **Project** — the slug of the project this work item belongs to, or `none` for standalone items.
- **Description** — enough context to understand the need without referring to the original source. One to three sentences is often sufficient. Include the "why" — what problem this solves or what capability it enables.

## Optional Content

Include these when they are known and useful. Omit them when they are not:

- **Proposed Changes** — a brief sketch of what might be built. This is a starting point for planning, not a commitment.
- **Acceptance Criteria** — conditions that would confirm the work is done. Keep these outcome-oriented, not implementation-specific.
- **Target Project** — which project will contain the implementation work; defaults to the capturing project when omitted or empty. Supports multiple targets via comma-separated listing, though one work item per project is recommended for clarity. This field can be safely omitted when the work item originates inside the target project.
- **Source** — where the work item originated (external issue URL, implementation log reference, conversation summary) if it helps preserve context.

## Procedure

1. **Capture** — create the work item folder and `workitem.md` with at minimum the Title and Description. Err on the side of writing it down quickly rather than crafting it perfectly.
2. **Contextualize** — if immediately obvious, add proposed changes and acceptance criteria. If not, leave them out — they belong in the planning phase, not the work item.
3. **File it** — commit the work item to the repository so it is not lost.

## Completion

When work is fully implemented and verified, follow the procedure in `procedures/Complete.md` to formally mark the work item as complete.

## Guidance

- Work items are not plans. They do not need to meet the standard of a feature plan document. They exist to prevent ideas and problems from falling through the cracks.
- Keep work items short. A work item that takes more than five minutes to write is probably trying to be a plan.
- Do not duplicate external issue trackers verbatim. Summarize the relevant context in the project's own terms.
- When a work item is promoted to a plan (via the Plan action), a `plan.md` is added to the folder — the `workitem.md` remains unchanged.
- Acceptance criteria in work items are intentionally lighter than in feature plans. They answer "how would we know this is done?" not "what are all the edge cases?"
- When Complete determines the work item is finished, no further active development is expected for this work item.
