# Ticket

## Intent

Capture a potential work item — a feature idea, bug report, improvement, or observation — as a lightweight record in the project's `docs/pending/` directory. Tickets are intake documents, not plans. They preserve enough context for later triage and planning without requiring deep analysis at the time of creation.

Tickets may originate from any source: an external issue tracker, a conversation, a problem encountered during implementation, or an idea that surfaces opportunistically during unrelated work. The goal is to capture it before the context is lost.

## When to Create a Ticket

- A feature idea or enhancement is identified but is not part of the current implementation scope
- A bug or unexpected behavior is discovered during testing or usage
- An external request or issue needs to be tracked within the project
- An implementation reflection produces a recommendation that warrants its own work item
- Any time the thought "we should do X" arises and X is not already tracked

Do not defer capture. A brief ticket written now is more valuable than a detailed ticket never written.

## Document Storage & Naming

Each ticket gets its own folder under `docs/pending/`, named with an identifier and short description in kebab-case. The ticket document inside is always named `ticket.md`.

Two naming conventions are supported for the folder:

- **Sequential numbering** (default): `docs/pending/07-investigate-pipeline-jobs/ticket.md`
- **External identifier** (when available): `docs/pending/PROJ-123-investigate-pipeline-jobs/ticket.md`

Sequential numbers use two-digit prefixes and reflect creation order, not priority or implementation order. When an external system (issue tracker, project board) provides an identifier, use it as the prefix instead.

The ticket folder is the home for all artifacts related to this work item. As the work progresses through planning and implementation, additional files are added to the same folder (see Plan and Implement actions). When work is complete, the entire folder moves from `docs/pending/` to `docs/complete/` following the procedure in Close.

## Required Content

Every ticket must include:

- **Title** — a concise description of the work item
- **Description** — enough context to understand the need without referring to the original source. One to three sentences is often sufficient. Include the "why" — what problem this solves or what capability it enables.

## Optional Content

Include these when they are known and useful. Omit them when they are not:

- **Proposed Changes** — a brief sketch of what might be built. This is a starting point for planning, not a commitment.
- **Acceptance Criteria** — conditions that would confirm the work is done. Keep these outcome-oriented, not implementation-specific.
- **Target Project** — which project will contain the implementation work; defaults to the capturing project when omitted or empty. Supports multiple targets via comma-separated listing, though one ticket per project is recommended for clarity. This field can be safely omitted when the ticket originates inside the target project.
- **Source** — where the ticket originated (external issue URL, implementation log reference, conversation summary) if it helps preserve context.

## Procedure

1. **Capture** — create the ticket folder and `ticket.md` with at minimum the Title and Description. Err on the side of writing it down quickly rather than crafting it perfectly.
2. **Contextualize** — if immediately obvious, add proposed changes and acceptance criteria. If not, leave them out — they belong in the planning phase, not the ticket.
3. **File it** — commit the ticket to the repository so it is not lost.

## Completion

When work on a ticket is fully implemented and verified, follow the procedure in `actions/Close.md` to formally close the ticket.

## Guidance

- Tickets are not plans. They do not need to meet the standard of a feature plan document. They exist to prevent ideas and problems from falling through the cracks.
- Keep tickets short. A ticket that takes more than five minutes to write is probably trying to be a plan.
- Do not duplicate external issue trackers verbatim. Summarize the relevant context in the project's own terms.
- When a ticket is promoted to a plan (via the Plan action), a `plan.md` is added to the ticket's folder — the ticket itself remains unchanged.
- Acceptance criteria in tickets are intentionally lighter than in feature plans. They answer "how would we know this is done?" not "what are all the edge cases?"
- When Close determines the ticket is complete, no further actions are expected for this ticket.
