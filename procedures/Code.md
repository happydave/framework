# Code

## Intent

Implement a project from its plan document. Read the plan, implement the plan incrementally, and maintain a structured log of work, decisions, and problems (code.md).

The plan lives in the work item folder and specifies what to read, what to implement, and in what order. This document describes the general procedure that applies to any Code action.

## Prerequisites

- A work item (workitem.md)
- A plan (plan.md)

- If `plan.md` does not exist, it is not possible to successfully complete the Code procedure, therefore **stop immediately**.

## Procedure

### 1. Read Applicable Skills and Guidelines

Before implementing the plan, identify which guidelines apply to this project:

- Look at the `plan.md` for this work item. The plan's **Applicable Guidelines** section lists which skills and guidelines documents apply.  Fully read each listed document.
- If `plan.md` does not exist, or if it exists but is missing the **Applicable Guidelines** section, **stop immediately** and inform the requester: the plan is missing or incomplete. Do not proceed with implementation until a valid plan with an Applicable Guidelines section is provided.

Read all identified guidelines before proceeding. These guidelines are not optional unless a plan explicitly opts out.

Terminology used throughout this document:
- **Build** — any procedure that compiles, formats, lints, or otherwise transforms source artifacts into verified output, as defined by the applicable guideline.
- **Test** — any procedure that validates correctness against specified behavior (unit tests, integration checks, structural validation), as defined by the applicable guideline.
- **Verification steps** — the collective build and test procedures defined by applicable guidelines.

### 2. Read Before Implementing

Read the plan document and all applicable guideline documents before proceeding.

The purpose is to understand the full scope, constraints, and dependencies before making implementation decisions.

### 3. Scaffold Implementation Log

**The implementation log is the handoff artifact** and implementation is not complete until implementation log is complete.

Create `code.md` in the work item folder (e.g. `docs/pending/07-investigate-pipeline-jobs/code.md`).

Populate each section as work progresses:
- **Work Completed** — append entries after each verified change. Each entry should identify which plan feature/requirement it addresses, the files modified, and current state (e.g., "verified clean build").
- **Decisions Made** — record implementation choices where the planning documents left discretion (AI freedom sections), and why the choice was made. Record these *at the time of making the decision*, not retrospectively.
- **Inconsistencies Found and Resolved** — note contradictions, ambiguities, or gaps discovered in the planning documents during implementation, and how they were resolved.
- **Problems Encountered** — anything that didn't work as expected, required iteration, or deviated from the plan. Include root cause if apparent.
- **Verification Results** — table mapping each acceptance criterion from the work item to its outcome:

  | Acceptance Criterion | Status | Notes |
  | -------------------- | ------ | ----- |
  | \<criterion from workitem\> | [ ] | |

Keep entries concise and factual. The log must be sufficient for another session to continue if interrupted. On long work items, a **Not Yet Verified** section — claims made but not yet backed by a run — is worth more to the next session than another paragraph of what was done; move items out of it as they are verified.

### 4. Implement Incrementally

Infrastructure and scaffolding (build configuration, project structure, dependency setup) typically come first, even if the planning documents number them differently, because everything else depends on a working build.

Implement changes (other than infrastructure and scaffolding) in the order specified by the plan. For each change:

1. Implement the change according to the plan
2. Test to verify correctness
3. Fix any errors before moving to the next change
4. **Update `code.md` — log what was done, any decisions taken, and current state**

Two disciplines within this loop:

- **Restate structural constraints before writing.** When the plan constrains a component structurally (locking rules, goroutine ownership, allocation budgets), restate those constraints at the top of the implementation log entry before writing the code, and check them off as the code satisfies them. A constraint held in mind while writing is a constraint that drifts.
- **A negative control must be seen to fail.** A test written to prove that a defect *would* be caught is not done when it compiles — it is done when it has been run and observed to fail for the stated reason. A negative control that has never failed proves nothing about the detector.

A change is not complete until both the code changes AND the corresponding `code.md` entry are done. Do not batch multiple changes before updating the log. Incremental documentation serves two purposes: it enables session continuity if interrupted (the log is the handoff artifact for the next session), and it forces you to verify each step before moving on. Avoid batching changes then compiling once at the end — incremental verification catches errors early, reduces rework, and produces a reliable audit trail.

### 5. Verify Completion

When all features are implemented:

- Run the verification steps (build and test procedures) defined by the applicable guidelines identified in step 1.
- Confirm clean results for each verification step. Per `skills/evidence.md`, a passing gate confirms the gate, not necessarily the outcome: for an acceptance criterion that produces an artifact, inspect the artifact itself (an `[agent]`-tagged criterion, per `Plan.md`, is the agent's to verify and close — do not defer it as if it needed the owner).
- **Increment the project version following the policy in `skills/versioning.md`.**
- Ensure `code.md` is up to date — every completed change must have a corresponding log entry, and "Final Status" must be populated. If entries are missing, go back and fill them before proceeding.

## Guidance

- Follow the constraints in the planning documents strictly. Invariants and SHALL statements are non-negotiable. AI freedom sections are where discretion applies.
- Create temporary directories inside the project repository, not outside it. Outside the repo, each file system action requires manual approval; inside the repo, there are no such restrictions.
- When a planning document is ambiguous, make a reasonable choice, document it **in `code.md` at the time of making the decision**, and continue. Do not block on ambiguity. Software can be rewritten and git provides a rollback path — the cost of a recoverable wrong decision is almost always lower than the cost of stopping.
- When a planning document contradicts another, note the inconsistency in `code.md` and resolve it in the direction that best serves the stated goals of the plan and/or project.
- When a change merges overlapping content from multiple documents into one, apply the Merge Union Check in `skills/markdown.md`: enumerate the source items from the pre-change versions and tick each off against the merged result before considering the step done.
- Guidelines applied in step 1 apply throughout implementation. If a plan change conflicts with a guideline, log the conflict and resolution in `code.md`.
- Guideline-defined build and test procedures take precedence over any generic interpretation of those terms. When a guideline specifies how to build or test, follow it exactly.
- If a guideline does not define build or test steps, use conventional defaults for that domain (e.g., the standard tool invocation for that language or format) and record the decision in `code.md`.
- **The implementation log is the handoff artifact.** It enables continuation after session interruption — if this session restarts, the next instance reads `code.md` to understand what was done and what remains. A missing or empty log means context is lost and work must be redone. **Documenting a change is part of completing it; code changes without corresponding log entries are incomplete.**
