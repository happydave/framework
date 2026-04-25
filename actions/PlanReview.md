# Plan Review

## Intent

Evaluate a plan document to ensure it is sufficient to guide correct implementation on first attempt. The output is a structured set of observations — concerns, questions, and approvals — that identifies gaps, contradictions, or ambiguities before implementation begins.

Plan Review is an *external* quality gate that runs after the author's own "Critically Assess" step in `Plan.md`. While self-assessment identifies issues through the lens of intent, Plan Review provides an independent check to catch blind spots, structural problems, and assumption gaps.

## When to Plan Review

- A plan document has been produced following the `Plan` action and is awaiting evaluation.
- An independent quality check is required before implementation begins.
- A stakeholder wants validation that the plan is ready for the `Implement` action.

## Roles

**Reviewer (Automated or Human):**
- Systematically evaluates the plan across five dimensions: Completeness, Coherence, Precision, Scope, and Compliance.
- Identifies contradictions, ambiguities, and scope inflation.
- Organizes findings into tiered categories with section-level precision.
- Produces a structure summary confirming which required sections are substantive.
- Delivers the final verdict and posts structured feedback.

**Author:**
- Provides the plan and any context not captured within it (stakeholder constraints, technical limitations, etc.).
- Confirms completion of the "Critically Assess" step from `Plan.md`.
- Addresses findings and revises the plan until it reaches an approved state.

**Human Oversight (as needed):**
- Clarifies findings the Reviewer flags as uncertain.
- Judges findings based on domain knowledge when automated logic is insufficient.
- Reclassifies findings where blocking/non-blocking status does not match project standards.

## Procedure

### 1. Initiate Review

The Author provides the following:
- The plan (typically `plan.md` in the ticket folder).
- Relevant context not in the plan (constraints, known limitations, etc.).
- Confirmation that "Critically Assess" from `Plan.md` is complete.

If the plan is absent or insufficient, return **Deferred** with an explanation of what is missing.

### 2. Structural Analysis

The Reviewer reads the plan in its entirety to identify:
- Presence and substance of each section (not just placeholders).
- Category of content: metadata, constraints, requirements, details, or meta-information.

Produce a **plan structure summary** confirming which sections are present and substantively filled.

### 3. Evaluation

The Reviewer assesses the plan across these dimensions:

**Completeness** — are all required sections from `Plan.md` present? Are there gaps in failure modes, security-relevant behaviors, or edge cases?

**Coherence** — are there internal contradictions? Check invariants against each other and against required behaviors. Ensure invariants are provable.

**Precision** — are terms specific and unambiguous? Flag vague language like "appropriate" or "as needed" in critical sections (Invariants, Behaviors, Edge Cases, Data Changes).

**Scope Alignment** — does the plan stay within the mandate of the originating `ticket.md`? Distinguish reasonable deductions from purely opportunistic additions.

**Compliance** — does the plan conflict with any applicable `guidelines/[language].md` rules?

### 4. Reporting

The Reviewer organizes findings into two tiers:
- **Blocking** — must be resolved before proceeding: missing sections, contradictions, scope inflation, or ambiguity in critical sections.
- **Non-blocking** — worth addressing but implementation may continue: minor ambiguity in non-critical sections, partially-filled optional sections, or structural observations.

Flag findings as **uncertain** when they depend on intent or context the Reviewer cannot fully determine.

### 5. Judgment and Refinement

If human oversight is involved:
- Confirm or dismiss uncertain findings based on domain knowledge.
- Reclassify findings if the blocking/non-blocking judgment differs from project standards.
- Identify anything the Reviewer missed (e.g., organizational nuances).

### 6. Verdict

The Reviewer (or Human Oversight) delivers the verdict and posts feedback in the ticket folder. Use inline notes for section-specific findings and a summary for the overall verdict.

## Findings Tiers

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

## Verdict

- **Approved**: Plan is ready. All blocking findings are resolved.
- **Revisions Requested**: Blocking findings remain, or a high concentration of non-blocking issues undermines quality.
- **Deferred**: Insufficient context exists (e.g., no `ticket.md`) to evaluate the plan.

## Guidance

- **Plan vs. Idea**: Evaluate the planning artifact's quality, not just the technical merit of the idea.
- **Ambiguity is a Blocker**: If a term could lead to different implementation choices, it needs clarification. Ambiguity often masks hidden contradictions.
- **Match Depth to Complexity**: A short review for a small, well-scoped plan is appropriate.
- **Be Specific**: Reference section names and line numbers. "Possible race condition" is less helpful than naming the conflicting invariant and behavior.
- **Approve When Ready**: Avoid withholding approval as leverage; if it can guide correct implementation, approve it.

