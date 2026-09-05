# Project Assessment

## Intent

Evaluate the overall health and coherence of a project — not a single plan or diff, but the project as a whole. The output is a structured set of findings — concerns, questions, and a verdict — that answers whether the project is on track, coherent, and worth continuing as currently scoped.

Project Assessment fills the gap between PlanReview (pre-implementation, single plan) and CodeReview (post-implementation, single MR). Its unique scope is cross-cutting concerns that span multiple work items, designs, and time: goal drift, orphaned work, missing dependencies, and risks that no individual work item captures.

## When to Run

- After a significant phase of work items completes and the next phase is being scoped.
- When stakeholders question whether the project is still on track or the mission remains valid.
- When new information arises — a technical constraint, a changed external dependency, a shift in priorities — that may invalidate or significantly alter the project mission.
- As a scheduled health check at defined project milestones.
- When a project has been inactive for an extended period and needs a re-entry assessment before work resumes.

## Roles

**AI:**
- Reads all available project artifacts (project document, design documents, work items) without fatigue or anchoring bias.
- Produces a project state summary.
- Evaluates exhaustively across all five dimensions, surfacing findings with specificity.
- Flags findings as uncertain when they depend on intent or context the AI cannot fully determine.

**Human:**
- Provides the project name and any background not captured in project artifacts (stakeholder context, verbal decisions, external constraints).
- Clarifies uncertain findings based on domain knowledge.
- Judges which findings are blocking vs. acceptable given project context.
- Delivers the final verdict.

## Procedure

### 1. Locate Project Artifacts

Identify and read:
- The project document (`project.md`) for the named project.
- All design documents referenced by or co-located with the project document.
- All work items associated with the project, in any state (pending, active, complete, archived, on hold).
- All phase records under the project's `phases/` folder (`Phase.md`), together with the work items that declare each phase, including declarers from other projects.

If the project document does not exist, stop immediately. Status = **Deferred**. Note which artifact could not be located.

If design documents or work items cannot be located but the project document exists, note the absences as findings within the appropriate dimensions and continue.

### 2. Project State Summary

Produce a brief summary covering:
- Project mission as stated in the project document.
- Number of work items by state: pending, active, complete, on hold, archived.
- Most recently completed work (if any), and approximate project age or active duration.
- Any notable conditions: no active work items, all work complete, large backlog with no recent completions, etc.

This summary orients the human and establishes shared context before findings are presented. It is not a judgment — it is factual description.

### 3. Evaluate

Assess the project across five dimensions:

**Goal Alignment** — are active and pending work items traceable to the project's stated goals? Are any work items pursuing outcomes that have drifted from the project mission? Has the project mission itself become outdated given current circumstances?

**Scope Integrity** — is scope creeping (new work items added that were not implied by the original project scope or design)? Are there work items that should be closed, deferred, or split? Is the project's design still representative of what is being built?

**Work Item Health** — are work items in a consistent and progressing state? Identify: stalled items (in active state with no recent progress), blocked items without documented resolution plans, and orphaned work items (referenced in design documents or other work items but not present in the backlog). Note items that have been on hold for an extended period without revisit. Where the project owns phases, also identify: a phase declared `complete` while a declaring work item is still open (the close gate was bypassed by hand), and a phase declared `active` with no declaring work items or no movement among them.

**Dependency Status** — are there unresolved cross-work-item dependencies that block forward progress? Are assumed external dependencies (libraries, services, APIs, team outputs) still valid? Are any work items blocked on each other in a cycle?

**Risk Surface** — what project-level risks exist that no individual work item captures? Are there missing work items that the project requires before it can succeed? Has anything changed in the project's context (technology landscape, stakeholder needs, constraints) that constitutes a risk not yet reflected in the backlog?

### 4. Report Findings

Organize findings into two tiers:

- **Blocking** — must be resolved before the project can be considered on track: goal drift that invalidates active work items, stalled or orphaned work without any resolution plan, unresolved dependency cycles, missing work items the project cannot succeed without, scope inflation that fundamentally misrepresents the project.
- **Non-blocking** — worth addressing but do not prevent forward progress: minor scope additions that are reasonable extensions of the mission, work items that are on hold but have a documented plan, external dependencies that are unvalidated but low-risk.

Flag findings as **uncertain** when they depend on intent, domain knowledge, or context the AI cannot fully determine. Uncertain findings without human oversight available default to **Blocking**.

List all uncertain findings separately with their disposition (confirmed, dismissed, or remaining uncertain).

For each blocking and non-blocking finding: state the dimension, the specific concern, the evidence from project artifacts, and why it matters. Be specific enough that the human knows what to address.

### 5. Human Review

The human reviews the AI's findings:
- Confirms or dismisses uncertain findings based on stakeholder context and system knowledge.
- Reclassifies any findings where the AI's blocking/non-blocking judgment does not match project standards.
- Identifies anything the AI missed that requires manual scrutiny (organizational constraints, verbal commitments not in any document, external timelines).

### 6. Produce Artifact

Write `projectassessment.md` in the project folder. The artifact contains:

- **Assessment Date** — date the assessment was performed.
- **Project Mission** — the mission as stated in the project document (copied verbatim or paraphrased if lengthy).
- **Project State Summary** — the summary produced in step 2.
- **Findings** — organized by dimension, each finding tagged Blocking or Non-blocking. Uncertain findings listed in a dedicated subsection with their disposition.
- **Status** — one of: Healthy, Attention Required, or Deferred.
- **Next Steps** — for Attention Required status, a brief list of specific actions required to resolve blocking findings.

### 7. Deliver Verdict

State the status clearly and, for Attention Required, identify which blocking findings must be resolved and by whom. For Healthy status, note any non-blocking findings worth addressing and confirm the project is clear to continue.

## Status Outcomes

- **Healthy** — no blocking findings; any non-blocking findings are minor and do not indicate systemic goal drift or risk. The project is on track and may continue.
- **Attention Required** — one or more blocking findings exist that must be resolved before the project can be considered on track; OR numerous non-blocking findings (more than five, or affecting more than half the evaluation dimensions) indicate systemic drift that warrants revision even in the absence of explicitly blocking issues.
- **Deferred** — the assessment cannot begin because the project document does not exist. This is a precondition failure, not an evaluation result.

## Notes

- **Evaluate Project Health, Not Idea Merit**: Assess the project's current state and trajectory, not whether the original idea was good. A well-scoped project executing cleanly on a limited goal is Healthy; a sprawling project with undefined boundaries is not, regardless of ambition.
- **A Completed Project Is Not Unhealthy**: If all work items are complete and the project has met its stated goals, this is a valid terminal state. Do not flag natural completion as a risk or gap.
- **Match Depth to Complexity**: A two-work-item project with a clear mission needs a lighter assessment than a multi-phase initiative with dozens of items. Scale rigor to what is genuinely needed.
- **Uncertain Findings Require Attention**: Findings the AI cannot resolve without intent context are not noise — they surface exactly the gaps that require human judgment. Handle them deliberately.
- **Be Specific**: "Work items may be misaligned" is less useful than naming the specific work items and the specific goal statement they diverge from.
