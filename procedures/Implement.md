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

### 3. Scaffold Implementation Log

Create `implementation.md` in the ticket folder (e.g., `docs/pending/07-investigate-pipeline-jobs/implementation.md`) with the following structure:

```markdown
# Implementation Log: <ticket title>

## Work Completed

## Decisions Made

## Inconsistencies Found

## Problems Encountered

## Final Status
```

This is a **mandatory gate** — do not proceed to step 4 until `implementation.md` exists with the above structure. Each section header must be present even if empty. The log is the primary artifact for session continuity: if this session is interrupted, another session (or you, in a future session) will read this file to understand what has been done and what remains. **An empty or missing `implementation.md` means implementation has not started.**

Populate each section as work progresses:
- **Work completed** — append entries after each verified change. Each entry should identify which plan feature/requirement it addresses, the files modified, and current state (e.g., "verified clean build").
- **Decisions made** — record implementation choices where the planning documents left discretion (AI freedom sections), and why the choice was made. Record these *at the time of making the decision*, not retrospectively.
- **Inconsistencies found** — note contradictions, ambiguities, or gaps discovered in the planning documents during implementation, and how they were resolved.
- **Problems encountered** — anything that didn't work as expected, required iteration, or deviated from the plan. Include root cause if apparent.

Keep entries concise and factual. The log must be sufficient for another session to continue without loss of context.

### 4. Implement Incrementally

Infrastructure and scaffolding (build configuration, project structure, dependency setup) typically come first, even if the planning documents number them differently, because everything else depends on a working build.

Implement changes (other than infrastructure and scaffolding) in the order specified by the plan. For each change:

1. Implement the change according to the plan
2. Test to verify correctness
3. Fix any errors before moving to the next change
4. **Update `implementation.md` — log what was done, any decisions taken, and current state**

A change is not complete until both the code changes AND the corresponding `implementation.md` entry are done. Do not batch multiple changes before updating the log. Incremental documentation serves two purposes: it enables session continuity if interrupted (the log is the handoff artifact for the next session), and it forces you to verify each step before moving on. Avoid batching changes then compiling once at the end — incremental verification catches errors early, reduces rework, and produces a reliable audit trail.

### 5. Verify Completion

When all features are implemented:

- Run the verification steps (build and test procedures) defined by the applicable guidelines identified in step 1.
- Confirm clean results for each verification step.
- Ensure `implementation.md` is up to date — every completed change must have a corresponding log entry, and "Final Status" must be populated. If entries are missing, go back and fill them before proceeding.

### 6. Document

Follow the procedure in `procedures/Document.md` to verify that the project's documentation (README, code comments, help text, etc.) is accurate and consistent with the changes just made.

When a change affects only documentation files (e.g., updating README, action files), there is no code-level drift between implementation and documentation to detect. In such cases the Document pass may be minimal — confirming "no drift detected" rather than producing corrections. The Document action is still performed; its output is simply lightweight.

## Guidance

- Follow the constraints in the planning documents strictly. Invariants and SHALL statements are non-negotiable. AI freedom sections are where discretion applies.
- When a planning document is ambiguous, make a reasonable choice, document it **in `implementation.md` at the time of making the decision**, and continue. Do not block on ambiguity.
- When a planning document contradicts another, note the inconsistency in `implementation.md` and resolve it in the direction that best serves the stated goals of the plan and/or project.
- Guidelines applied in step 1 apply throughout implementation. If a plan change conflicts with a guideline, log the conflict and resolution in `implementation.md`.
- Guideline-defined build and test procedures take precedence over any generic interpretation of those terms. When a guideline specifies how to build or test, follow it exactly.
- If a guideline does not define build or test steps, use conventional defaults for that domain (e.g., the standard tool invocation for that language or format) and record the decision in `implementation.md`.
- **The implementation log is the handoff artifact.** It enables continuation after session interruption — if this session restarts, the next instance reads `implementation.md` to understand what was done and what remains. A missing or empty log means context is lost and work must be redone. **Documenting a change is part of completing it; code changes without corresponding log entries are incomplete.**
