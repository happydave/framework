# Plan Review

## Intent

Critically assess a plan document to ensure it is sufficient to guide correct implementation on first attempt. The output is a structured set of observations — concerns, questions, and recommendations — that identifies gaps, contradictions, or ambiguities before implementation begins.

Plan Review is an *external* quality gate that provides an independent evaluation of the plan document before implementation begins.

## Triggering Conditions

- A plan document has been produced following the `Plan` action and is awaiting evaluation.
- An independent quality check is required before implementation begins.
- A stakeholder wants validation that the plan is ready for the `Implement` action.

## Roles

**Reviewer:**
- **Prerequisites**: Access to the originating `ticket.md` (for Scope Alignment), access to applicable guideline documents identified during evaluation, and knowledge of any project-specific constraints stated in the plan's Dependencies & Context or Explicit AI Freedom sections.
- Systematically evaluates the plan across five dimensions: Completeness, Coherence, Precision, Scope, and Compliance.
- Identifies contradictions, ambiguities, and scope inflation.
- Organizes findings into tiered categories with section-level precision.
- Produces a structure summary confirming which required sections are substantive.
- Delivers the final Status and posts structured feedback.

**Author:**
- Provides the plan and any context not captured within it (stakeholder constraints, technical limitations, etc.).
- Addresses findings and revises the plan until it reaches a Complete state.

**Human Oversight (as needed):**
- Clarifies findings the Reviewer flags as uncertain.
- Judges findings based on domain knowledge when automated logic is insufficient.
- Reclassifies findings where blocking/non-blocking status does not match project standards.

## Procedure

### 1. Initiate Review

The Author provides the plan (typically `plan.md` in the ticket folder).

If the plan document does not exist, stop immediately and inform the requester that the plan is missing.

If a prerequisite artifact (e.g., `ticket.md`) cannot be located, Status = Deferred with an explanation of which artifact could not be found.

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

**Scope Alignment** — does the plan stay within the mandate of the originating `ticket.md`? Distinguish reasonable deductions from purely opportunistic additions.

**Compliance** — does the plan conflict with any applicable `guidelines/[language].md` rules? Plans may override applicable guideline rules when explicitly documented in the plan itself. The Reviewer checks for two things: (a) whether a conflict exists, and (b) whether the plan explicitly acknowledges and justifies the override. Unjustified conflicts remain Blocking; explicit overrides with justification are Non-blocking structural observations unless they violate an Invariant.

### 4. Reporting

The Reviewer organizes findings into two tiers:
- **Blocking** — must be resolved before proceeding: missing sections, contradictions, scope inflation, or ambiguity in critical sections.
- **Non-blocking** — worth addressing but implementation may continue: minor ambiguity in non-critical sections, partially-filled optional sections, or structural observations.

Flag findings as **uncertain** when they depend on intent or context the Reviewer cannot fully determine. When the Reviewer flags a finding as uncertain and no human oversight is available, the finding defaults to **Blocking**. The `planreview.md` output SHALL list all uncertain findings separately with their disposition so they are visible.

### 5. Judgment and Refinement

**Revision Cycle Protocol:**
- The Author may revise and resubmit up to **three times**.
- Each resubmission SHALL address all Blocking findings and note how Non-blocking findings were handled (addressed, deferred with rationale, or acknowledged).
- If three revisions have occurred and the plan still has unresolved Blocking findings, Status defaults to **Significant Findings** and the matter is escalated for human decision on whether to continue planning, reduce scope, or close the ticket.

If human oversight is involved:
- Confirm or dismiss uncertain findings based on domain knowledge.
- Reclassify findings if the blocking/non-blocking judgment differs from project standards.
- Identify anything the Reviewer missed (e.g., organizational nuances).

### 6. Status

The Reviewer produces `planreview.md` in the ticket folder, populated according to the artifact structure defined in this procedure. The file includes: **Status** (Complete, Significant Findings, or Deferred), a **Structure Summary** of which plan sections are present and substantive, **Findings** organized by dimension (Completeness, Coherence, Precision, Scope, Compliance) with each tagged as Blocking or Non-blocking, an **Uncertain Findings** subsection listing all uncertain findings with their disposition, and **Free-form Feedback** for observations that don't fit structured categories.

## Findings Tiers

### Deferred — prerequisite artifact is absent

The review cannot begin because a required document (e.g., `plan.md` or the originating `ticket.md`) does not exist. This is a precondition failure, not an evaluation result.

### Blocking — plan cannot proceed until resolved

- Missing required sections or placeholder-only content.
- Internal contradictions (e.g., conflicting invariants).
- Behaviors that violate stated invariants (e.g., unencrypted export vs. encryption invariant).
- Scope inflation beyond the originating ticket.
- Ambiguity in critical sections (Behaviors, Invariants, Edge Cases) that could lead to incorrect implementation.

### Non-blocking — worth addressing but planning may continue

- Vague terms in non-critical sections (metadata, meta-information).
- Partially-filled sections with minor gaps.
- Overly broad AI Freedom sections that don't conflict with specific constraints.

## Status

- **Complete**: No blocking findings AND remaining non-blocking findings are minor (single-digit count, no pattern of systemic issues). Numerous non-blocking findings (more than five, or affecting more than half the plan's sections) indicate systemic quality concerns that warrant revision even in the absence of Blocking findings.
- **Significant Findings**: Blocking findings remain OR numerous non-blocking findings indicate systemic quality concerns that warrant revision even in the absence of Blocking findings.
- **Deferred**: The review cannot begin because a prerequisite artifact is absent (e.g., no `plan.md` exists, or no originating `ticket.md` exists). This is a precondition failure. If the Reviewer cannot determine whether a prerequisite artifact exists, Status is Deferred with an explanation of which artifact could not be located.

## Notes

- **Evaluate Plan Quality, Not Merely Idea Merit**: Evaluate the planning artifact's quality, not just the technical merit of the idea.
- **Ambiguity as a Blocker**: If a term could lead to different implementation choices, it needs clarification. Ambiguity often masks hidden contradictions.
- **Match Depth to Complexity**: A short review for a small, well-scoped plan is appropriate.
- **Be Specific**: Reference section names and line numbers. "Possible race condition" is less helpful than naming the conflicting invariant and behavior.
- **Release When Ready**: If the plan can guide correct implementation, release it for the next step without delay.
