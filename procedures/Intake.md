# Intake

## Intent

Capture incoming raw material — ideas, observations, feedback dumps, requests — at the moment it occurs, before context is lost and before any commitment is made. Intake is the zero-friction front door of the workflow: writing the thought down is the entire cost.

Intake items are un-atomized by nature. One intake file may yield zero, one, or many work items; several intake files may converge into one. Atomization, classification, and acceptance are triage's job (`Triage.md`), not capture's. Capture requires no decisions: no ID, no folder, no project assignment, no classification.

## When to Use Intake

- An idea, improvement, or "we should do X" thought surfaces and would otherwise be lost.
- A defect is noticed in passing. (A deliberate, structured defect capture goes through `BugReport.md` instead.)
- Feedback arrives as a pile: playtest notes, a batch of mixed requests, a wishlist.
- Anything worth remembering that is not yet worth deciding about.

Intake is an on-ramp, not a mandatory stage. Work that arrives already atomic and accepted — a project decomposition, a deliberate bug report, a directly scoped request — goes straight to a work item (`WorkItem.md`).

## Document Storage & Naming

Intake items are flat markdown files in the central management repository (e.g., `tickets`) at `docs/intake/`, named `YYYY-MM-DD-<slug>.md` with a short kebab-case slug. No numeric IDs, no folders, no counter. If a slug would collide with an existing same-day file, pick a more specific slug.

## Format

Free-form body. A single sentence is valid intake. A pasted dump is valid intake. No frontmatter is required.

Add only what costs nothing at capture time:

- where it came from, if it helps preserve context
- a project hint, if obvious

## Lifecycle

An intake file rests in `docs/intake/` until it is triaged. The visible contents of `docs/intake/` are exactly the untriaged queue — an empty listing means caught up.

Triage (`Triage.md`) assigns each item in the file a disposition: promoted to one or more work items, spawned a project, merged into an existing work item, or declined with a one-line reason. Each disposition is appended to the intake file, and once every item in the file has one, the file moves to the sibling `docs/intake-processed/`.

Dispositions are one-directional and write-once per item: the intake file records what it spawned; nothing ever links back to an intake file, and a recorded disposition is never revised. A multi-item file with items still open stays in `docs/intake/`, partial dispositions recorded inline, until every item is dispositioned.

## Guidance

- Do not defer capture. A one-sentence intake file written now is more valuable than a polished work item never written.
- Do not polish. Capture is not authoring — the real write-up happens at triage and planning.
- Do not use intake as a backlog. Accepted work belongs in work items; intake is the unvetted queue.
- Anti-rot is triage-on-touch: glance at the inbox when sitting down to project work; a non-empty `ls docs/intake/` is the prompt. There is no scheduled ritual.
- Declined is a real outcome. "Considered and said no" preserved in the processed file is signal, not waste.
