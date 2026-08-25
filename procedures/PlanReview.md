# Plan Review

## Intent

Critically assess a plan document to ensure it is sufficient to guide correct implementation on first attempt. The output is a structured set of observations — concerns, questions, and recommendations — that identifies gaps, contradictions, or ambiguities before implementation begins.

Plan Review is a *preferably external* quality gate. Its evaluation is independent in the sense that matters: independent of the plan's own reasoning, not necessarily performed by a second party. If no external reviewer is available, the same agent SHALL perform the review itself in the same session — a **self-applied** review. The gate is never skipped; "no reviewer available" is not a disposition. See **Self-Applied Review** for how the two-party protocol collapses to one agent.

## Roles

**Reviewer:**
- **Prerequisites**: Access to the originating `workitem.md` (for Scope Alignment), access to applicable guideline documents identified during evaluation, and knowledge of any project-specific constraints stated in the plan's Dependencies & Context or Explicit AI Freedom sections.
- Systematically evaluates the plan across five dimensions: Completeness, Coherence, Precision, Scope, and Compliance.
- Identifies contradictions, ambiguities, and scope inflation.
- **Fixes minor issues directly** (e.g., typos, minor wording ambiguity, trivially-wrong references) rather than reporting them as findings.
- For issues that are substantive or unreasonably complex to resolve without additional context, stops and notifies the requester rather than attempting a fix.
- Organizes findings into tiered categories with section-level precision.
- Produces a structure summary confirming which required sections are substantive.
- Delivers the final Status and posts structured feedback.

**Author:**
- Provides the plan and any context not captured within it (stakeholder constraints, technical limitations, etc.).
- Clarifies uncertain findings the Reviewer cannot resolve from the plan alone.
- Addresses findings and revises the plan until it reaches a Complete state.

## Self-Applied Review

When no external reviewer is available, the plan's author performs the review in the same session. The dimensions, the findings tiers, and the `planreview.md` artifact are identical to an external review; only the role assignments collapse. Under self-application:

- "Stops and notifies the requester" means surfacing to the human owner — the requester is the owner in both modes.
- The Revision Cycle Protocol applies unchanged: each self-revision is a real edit to `plan.md` addressing all Blocking findings, and three failed cycles still escalate to the owner as Significant Findings.
- Step 5's Author-availability clause (confirm or dismiss uncertain findings from domain knowledge) is external-review only. Its purpose is to let the Author supply context the Reviewer lacked; a self-reviewer already holds all of the author's context, so uncertainty that survives it is genuine and cannot be cleared by asserting the author's availability.

Self-review's characteristic failure mode is rubber-stamping — a reviewer inclined to confirm the plan it just wrote. Three countermeasures are mandatory:

1. `planreview.md` SHALL record the review mode (`external` or `self-applied`) so a later reader can weight the findings.
2. The Precision spot-check SHALL be performed and its sample recorded in the artifact — which claims were checked against which opened files. It is the most bias-resistant step in the review because it is factual rather than judgmental.
3. Uncertain findings SHALL NOT be resolved in the plan's favor by default (see Reporting).

## Procedure

### 1. Initiate Review

The Author provides the plan (typically `plan.md` in the work item folder).

If the plan document does not exist, stop immediately and inform the requester that the plan is missing.

If a prerequisite artifact (e.g., `workitem.md`) cannot be located, Status = Deferred with an explanation of which artifact could not be found.

### 2. Structural Analysis

The Reviewer reads the plan in its entirety to identify:
- Presence and substance of each section (not just placeholders).
- Category of content: metadata, constraints, requirements, details, or meta-information.

Produce a **plan structure summary** confirming which sections are present and substantively filled.

A section contains **substantive content** when it provides information sufficient for an independent agent to evaluate whether the plan meets its stated objective without guessing missing details. Concrete indicators include:
- Specific conditions, constraints, or outcomes described in natural language.
- Named failure modes with specified responses (not just "handle errors").
- Scenario sequences that define inputs and expected outputs.

A section contains **placeholder content** when it consists only of headings with no body text, generic markers ("TBD", "[details to follow]"), single vague words ("appropriate", "sufficient"), or category names without elaboration ("see guidelines" with no specific guidance cited).

### 3. Evaluation

The Reviewer assesses the plan across these dimensions:

**Completeness** — are all required sections from `Plan.md` present? Are there gaps in failure modes, security-relevant behaviors, or edge cases?

**Coherence** — are there internal contradictions? Check invariants against each other and against required behaviors. Ensure invariants are provable.

**Precision** — are terms specific and unambiguous? Flag vague language like "appropriate" or "as needed" in critical sections (Invariants, Behaviors, Edge Cases, Data Changes).

Precision is accuracy as well as clarity. Where the plan makes a concrete claim about existing code, content, or data, spot-check a sample of those claims against the artifact each one cites or describes — `Plan.md` requires the planner to have opened it (see its **Open-and-verify** rule), and this is the gate that checks they did. A claim that is precise but false is Blocking: unlike vagueness, which an implementer will notice and question, a confident wrong claim propagates silently into the implementation.

**Scope Alignment** — does the plan stay within the mandate of the originating `workitem.md`? Distinguish reasonable deductions from purely opportunistic additions.

**Compliance** — does the plan conflict with any applicable `skills/[language].md` rules? Plans may override applicable guideline rules when explicitly documented in the plan itself. The Reviewer checks for two things: (a) whether a conflict exists, and (b) whether the plan explicitly acknowledges and justifies the override. Unjustified conflicts remain Blocking; explicit overrides with justification are Non-blocking structural observations unless they violate an Invariant.

### 4. Reporting

The Reviewer organizes findings into two tiers:
- **Blocking** — must be resolved before proceeding: missing sections, contradictions, scope inflation, or ambiguity in critical sections.
- **Non-blocking** — worth addressing but implementation may continue: minor ambiguity in non-critical sections, partially-filled optional sections, or structural observations.

Flag findings as **uncertain** when they depend on intent or context the Reviewer cannot fully determine. An uncertain finding defaults to **Blocking** unless a human adjudicates it. Under a self-applied review, the author's presence in the session does not constitute adjudication: a Blocking uncertain finding is resolved the way any Blocking finding is — revise the plan so the uncertainty no longer exists, or hold it for the owner. It SHALL NOT be resolved in the plan's favor by default. The `planreview.md` output SHALL list all uncertain findings separately with their disposition so they are visible.

### 5. Judgment and Refinement

**Revision Cycle Protocol:**
- The Author may revise and resubmit up to **three times**.
- Each resubmission SHALL address all Blocking findings and note how Non-blocking findings were handled (addressed, deferred with rationale, or acknowledged).
- If three revisions have occurred and the plan still has unresolved Blocking findings, Status defaults to **Significant Findings** and the matter is escalated for human decision on whether to continue planning, reduce scope, or close the work item.

If the review is external and the Author is available to address uncertain findings (inoperative under self-application — see Self-Applied Review):
- Confirm or dismiss uncertain findings based on domain knowledge and project context.
- Identify anything the Reviewer missed (e.g., organizational nuances).

### 6. Status

The Reviewer produces `planreview.md` in the work item folder, populated according to the artifact structure defined in this procedure. The file includes: **Status** (Complete, Significant Findings, or Deferred), the **Review Mode** (`external` or `self-applied`), a **Structure Summary** of which plan sections are present and substantive, **Findings** organized by dimension (Completeness, Coherence, Precision, Scope, Compliance) with each tagged as Blocking or Non-blocking — under self-application the Precision findings include the recorded spot-check sample — an **Uncertain Findings** subsection listing all uncertain findings with their disposition, and **Free-form Feedback** for observations that don't fit structured categories.

## Findings Tiers

### Deferred — prerequisite artifact is absent

The review cannot begin because a required document (e.g., `plan.md` or the originating `workitem.md`) does not exist. This is a precondition failure, not an evaluation result.

### Blocking — plan cannot proceed until resolved

- Missing required sections or placeholder-only content.
- Internal contradictions (e.g., conflicting invariants).
- Behaviors that violate stated invariants (e.g., unencrypted export vs. encryption invariant).
- Scope inflation beyond the originating work item.
- Ambiguity in critical sections (Behaviors, Invariants, Edge Cases) that could lead to incorrect implementation.

### Non-blocking — worth addressing but planning may continue

- Vague terms in non-critical sections (metadata, meta-information).
- Partially-filled sections with minor gaps.
- Overly broad AI Freedom sections that don't conflict with specific constraints.

## Status

- **Complete**: No blocking findings AND remaining non-blocking findings are minor (single-digit count, no pattern of systemic issues). Numerous non-blocking findings (more than five, or affecting more than half the plan's sections) indicate systemic quality concerns that warrant revision even in the absence of Blocking findings.
- **Significant Findings**: Blocking findings remain OR numerous non-blocking findings indicate systemic quality concerns that warrant revision even in the absence of Blocking findings.
- **Deferred**: The review cannot begin because a prerequisite artifact is absent (e.g., no `plan.md` exists, or no originating `workitem.md` exists). This is a precondition failure. If the Reviewer cannot determine whether a prerequisite artifact exists, Status is Deferred with an explanation of which artifact could not be located.

## Notes

- **Evaluate Plan Quality, Not Merely Idea Merit**: Evaluate the planning artifact's quality, not just the technical merit of the idea.
- **Ambiguity as a Blocker**: If a term could lead to different implementation choices, it needs clarification. Ambiguity often masks hidden contradictions.
- **Match Depth to Complexity**: A short review for a small, well-scoped plan is appropriate.
- **Be Specific**: Reference section names and line numbers. "Possible race condition" is less helpful than naming the conflicting invariant and behavior.
- **Release When Ready**: If the plan can guide correct implementation, release it for the next step without delay.
