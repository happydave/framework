# Implement

## Intent

Implement a project from its plan document. Read the plan, implement the plan incrementally, and maintain a structured log of work, decisions, and problems (implementation.md).

The plan lives in the ticket folder and specifies what to read, what to implement, and in what order. This document describes the general procedure that applies to any Implement action.

## Prerequisites

- A plan (typically plan.md)

## Procedure

### 1. Identify Applicable Guidelines

Before implementing the plan, identify which guidelines apply to this project:

- Look at the `plan.md` for this ticket. The plan's **Applicable Guidelines** section lists which `guidelines/*.md` documents apply and what each defines as the **build** and **test** steps for this project.
- If `plan.md` does not exist, or if it exists but is missing the **Applicable Guidelines** section, **stop immediately** and inform the requester: the plan is missing or incomplete. Do not proceed with implementation until a valid plan with an Applicable Guidelines section is provided.

Read all identified guidelines before proceeding. These guidelines are not optional unless a plan explicitly opts out.

Terminology used throughout this document:
- **Build** — any procedure that compiles, formats, lints, or otherwise transforms source artifacts into verified output, as defined by the applicable guideline.
- **Test** — any procedure that validates correctness against specified behavior (unit tests, integration checks, structural validation), as defined by the applicable guideline.
- **Verification steps** — the collective build and test procedures defined by applicable guidelines.

### 2. Read Before Implementing

Read the plan document and all applicable guideline documents before proceeding.

The purpose is to understand the full scope, constraints, and dependencies before making implementation decisions.

### 3. Document Progress Incrementally

Create `implementation.md` in the ticket folder (e.g., `docs/pending/07-investigate-pipeline-jobs/implementation.md`). Update it as work progresses. The log should contain:

- **Work completed** — which features have been implemented, in what order, and their current state
- **Decisions made** — implementation choices where the planning documents left discretion (AI freedom sections), and why the choice was made
- **Inconsistencies found** — contradictions, ambiguities, or gaps discovered in the planning documents during implementation, and how they were resolved
- **Problems encountered** — anything that didn't work as expected, required iteration, or deviated from the plan

Keep entries concise and factual. If implementation is interrupted, the log should be sufficient for another session to continue.

### 4. Implement Incrementally

Infrastructure and scaffolding (build configuration, project structure, dependency setup) typically come first, even if the planning documents number them differently, because everything else depends on a working build.

Implement changes (other than infrastructure and scaffolding) in the order specified by the plan. For each change:

1. Implement the change according to the plan
2. Test to verify correctness
3. Fix any errors before moving to the next change
4. Update `implementation.md`

Avoid batching changes then compiling once at the end. Incremental verification catches errors early and reduces rework.

### 5. Verify Completion

When all features are implemented:

- Run the verification steps (build and test procedures) defined by the applicable guidelines identified in step 1.
- Confirm clean results for each verification step.
- Update the implementation log with final status.

### 6. Document

Follow the procedure in `actions/Document.md` to verify that the project's documentation (README, code comments, help text, etc.) is accurate and consistent with the changes just made.

## Guidance

- Follow the constraints in the planning documents strictly. Invariants and SHALL statements are non-negotiable. AI freedom sections are where discretion applies.
- When a planning document is ambiguous, make a reasonable choice, document it in the implementation log, and continue. Do not block on ambiguity.
- When a planning document contradicts another, note the inconsistency in the implementation log and resolve it in the direction that best serves the stated goals of the plan and/or project.
- Guidelines applied in step 1 apply throughout implementation. If a plan change conflicts with a guideline, log the conflict and resolution in the implementation log.
- Guideline-defined build and test procedures take precedence over any generic interpretation of those terms. When a guideline specifies how to build or test, follow it exactly.
- If a guideline does not define build or test steps, use conventional defaults for that domain (e.g., the standard tool invocation for that language or format) and record the decision in `implementation.md`.
- The implementation log is the primary artifact beyond the code itself. It enables continuation after interruption and feeds the continuous improvement process.
