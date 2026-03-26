# Implement

## Intent

Implement a project from its planning documents. The AI reads the plans, implements the project incrementally, and maintains a structured log of work, decisions, and problems. The human provides the implementation prompt (project-specific) and intervenes when needed; the AI does the implementation work.

The implementation prompt lives in the project repository and specifies what to read, what to implement, and in what order. This document describes the general procedure that applies to any implementation.

## Prerequisites

- A complete set of planning documents (produced by the Plan action)
- An implementation prompt in the project repo specifying reading order, implementation order, constraints, and exclusions
- Applicable framework guidelines (e.g., `guidelines/Docker.md`, language-specific guidelines) identified in the implementation prompt or feature plans

## Procedure

### 1. Read Before Implementing

Read all planning documents in the order specified by the implementation prompt before writing any code. This includes:

- Feature plans for all tickets in scope
- Any workflow or context documents
- Applicable framework guidelines

The purpose is to understand the full scope, constraints, and dependencies before making implementation decisions.

### 2. Implement Incrementally

Implement features in the order specified by the implementation prompt. For each feature:

1. Implement the feature according to its planning document
2. Compile or build to verify correctness
3. Fix any errors before moving to the next feature

Do not batch all implementation and then compile once at the end. Incremental verification catches errors early and reduces rework.

Infrastructure and scaffold (build configuration, project structure, dependency setup) typically come first, even if the planning documents number them differently, because everything else depends on a working build.

### 3. Maintain an Implementation Log

Create `implementation.md` in the ticket's folder (e.g., `docs/pending/07-investigate-pipeline-jobs/implementation.md`). Update it as work progresses. The log should contain:

- **Work completed** — which features have been implemented, in what order, and their current state
- **Decisions made** — implementation choices where the planning documents left discretion (AI freedom sections), and why the choice was made
- **Inconsistencies found** — contradictions, ambiguities, or gaps discovered in the planning documents during implementation, and how they were resolved
- **Problems encountered** — anything that didn't work as expected, required iteration, or deviated from the plan

Keep entries concise and factual. If implementation is interrupted, the log should be sufficient for another session to continue.

### 4. Verify Completion

When all features are implemented:

- Confirm the build succeeds (compile, package, or equivalent)
- Confirm the project is launchable/runnable as described in the planning documents
- Update the implementation log with final status

### 5. Reflect

Follow the procedure in `actions/Reflect.md` to write a reflective assessment as `reflect.md` in the ticket's folder. This captures what went well, what could have gone better, and concrete recommendations for improving the planning documents, framework, or tooling.

### 6. Complete

Move the ticket folder from `docs/pending/` to `docs/completed/`.

## Guidance

- Follow the constraints in the planning documents strictly. Invariants and SHALL statements are non-negotiable. AI freedom sections are where discretion applies.
- When a planning document is ambiguous, make a reasonable choice, document it in the implementation log, and continue. Do not block on ambiguity.
- When a planning document contradicts another, note the inconsistency in the implementation log and resolve it in the direction that best serves the project's stated goals.
- Apply applicable framework guidelines (Docker, language-specific, etc.) throughout implementation. These are not optional unless a feature plan explicitly opts out.
- The implementation log is the primary artifact beyond the code itself. It enables continuation after interruption and feeds the reflection process.
