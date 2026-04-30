# Discover

## Intent

Deeply investigate a product, solution, technology, methodology, or domain to understand what it offers, how it works, and what is useful. The `discover.md` file serves as the living record of this investigation, from initial scoping through to final assessment. It is not just a summary of results, but the document that drives the discovery process.

Discovery exists to build informed understanding before committing to any course of action. It may be broad or narrow, matching the scope of the request.

Discovery can be performed at the **Project** level (to define high-level architecture) or the **Work Item** level (to research specific implementation details). It can also be used as a standalone activity to determine if an initiative should be classified as a Project or a single Work Item.

## When to Discover

- Evaluating a product, service, or tool for potential adoption or integration
- Investigating an API, SDK, or platform's capabilities before planning work against it
- Exploring methodologies, conceptual frameworks, or industry standards
- Determining if a goal is "Project-sized" (requires multiple steps and design) or "Work Item-sized"
- Understanding a technology domain well enough to make informed decisions
- Answering a specific technical feasibility question that requires research
- Any time the question is "what is possible here?" rather than "what should we build?"

Discovery is not planning. It informs planning and design. A discovery document may lead to projects, work items, plans, or a decision to do nothing — all are valid outcomes.

## Document Storage & Naming

Discovery documents live inside a work item or project folder when one exists, or in their own folder under `docs/pending/` when discovery is standalone.

The presence of `discover.md` in a folder indicates that discovery has been **initiated**. It serves as the primary entry point, scoping document, and final summary. A folder may also contain auxiliary files (e.g., `procedures.md`, `adaptations.md`) when the discovery requires specialized deliverables.

- `docs/pending/07-investigate-pipeline-jobs/discover.md`
- `docs/pending/PROJ-123-investigate-pipeline-jobs/discover.md`
- `docs/pending/03-evaluate-monitoring-tools/discover.md`

A folder may contain both `discover.md` and `workitem.md` when discovery was prompted by a work item, or `discover.md` alone when discovery preceded any work item.

## Procedure

### 1. Initiate and Scope

Create `discover.md` immediately. Clarify what is being investigated and why. Fill in the **Status**, **Subject**, **Motivation**, and **Scope** sections.

- **Status** — start with `scoping`.
- **Subject** — the product, API, technology, methodology, or domain under investigation.
- **Motivation** — what decision or work this discovery is meant to inform.
- **Scope** — explicit boundaries, quality gates for sources, and evidence calibration (how `guidelines/Evidence.md` applies to this research).

For high-complexity tasks, submit the `discover.md` for review and move Status to `pending-approval` before starting deep investigation.

### 2. Investigate

Once scoped (and approved if necessary), update Status to `investigating`. Research the subject thoroughly within the established scope. This may include:

- Official documentation, API references, and specifications
- Available endpoints, methods, data formats, and authentication mechanisms
- Capabilities, features, and limitations
- Pricing, licensing, and access constraints
- Integration patterns and existing tooling (SDKs, CLI tools, libraries)
- Community resources, known issues, and maturity indicators

Follow leads. Discovery is not a checklist — pursue what is relevant and interesting as the investigation unfolds. Adjust depth based on what you find: spend more time on areas that are promising or complex, less on areas that are straightforward or clearly irrelevant.

### 3. Assess Usefulness

For each significant capability or finding, evaluate:

- Is this relevant to the motivation established in step 1?
- How could this be used? What would it enable?
- What are the constraints, limitations, or risks?
- What is missing or unclear that would need further investigation?

Separate what is confirmed from what is inferred or uncertain using confidence labels adapted from `guidelines/Evidence.md`:
- **Confirmed** — Cross-referenced across multiple independent industry standards, peer-reviewed sources, or official documentation.
- **Supported** — Consistent with industry practice and found in reliable sources, but not independently cross-verified.
- **Hypothesis** — Plausible interpretation or single-source opinion that has not been validated.
- **Inconclusive** — Conflicting evidence or opinions that cannot be reconciled.

### 4. Finalize the Document

Update Status to `completed`. Ensure the document is structured around findings and their assessment, serving as a reliable reference for those who did not participate in the investigation.

## Required Content

Every discovery document must include:

- **Status** — `scoping`, `pending-approval`, `investigating`, or `completed`.
- **Subject** — what was investigated, including version or date context.
- **Motivation** — why this investigation was conducted.
- **Scope** — the boundaries of the research, quality gates for sources, and out-of-scope definitions.
- **Methodology & Sources** — how the discovery was conducted and the specific sources consulted.
- **Summary** — a concise overview of key findings.
- **Findings** — detailed account of what was discovered, organized by topic, with confidence labels.
- **Assessment** — evaluation of usefulness, feasibility, risks, and gaps.

## Optional Content

Include when relevant, omit when not:

- **Recommendations** — suggested next steps based on the findings (e.g., classify as Project, create a Work Item, proceed to planning, investigate further, abandon).
- **Open Questions** — specific unknowns that could not be resolved during discovery and may need follow-up.
- **References** — links to documentation, API references, or other sources consulted.

## Guidance

- Discovery documents are reference material. Write them to be read later by someone (human or AI) who needs to understand the subject without repeating the investigation.
- Be specific. "The API supports filtering" is less useful than "The `/events` endpoint accepts a `type` query parameter that filters by event category; supported values are listed at [reference]."
- Separate facts from opinions. State what you found, then state what you think about it — clearly distinguished.
- Scope controls depth. A request to "look into X" warrants broad exploration. A request to "find out if X supports Y" warrants a focused answer. Match the document's depth to the request's scope.
- Do not pad discovery documents with background information the reader already knows. Focus on what was learned, not what was already understood.
- If discovery reveals enough information to act on, say so. If it reveals that more investigation is needed, say that too. The document should make the natural next step obvious.
