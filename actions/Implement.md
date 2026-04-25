# Implement

## Intent

Implement a project from its planning documents. The AI reads the plans, implements the project incrementally, and maintains a structured log of work, decisions, and problems. The human provides the implementation prompt (project-specific) and intervenes when needed; the AI does the implementation work.

The implementation prompt lives in the project repository and specifies what to read, what to implement, and in what order. This document describes the general procedure that applies to any implementation.

## Prerequisites

- A complete set of planning documents (produced by the Plan action)
- An implementation prompt in the project repo specifying reading order, implementation order, constraints, and exclusions

## Procedure

### 1. Detect Guidelines

Before reading planning documents, identify which language/tooling guidelines apply to this project:

- If `go.mod` exists → read and apply `guidelines/Go.md`
- If it's a VS Code extension or Node.js project (package.json with @types/vscode) → read and apply `guidelines/TypeScript.md`
- If the project uses Docker-based builds (`Dockerfile.dev`, Makefile with docker targets) → read and apply `guidelines/Docker.md`
- For investigations, `guidelines/Evidence.md` applies automatically

Read each applicable guideline in full before proceeding. These are not optional unless a feature plan explicitly opts out.

### 2. Read Before Implementing

Read all planning documents in the order specified by the implementation prompt before writing any code. This includes:

- Feature plans for all tickets in scope (including their Plan Structure sections)
- Guidelines already read in step 1
- Any other workflow or context documents

The purpose is to understand the full scope, constraints, and dependencies before making implementation decisions.

### 3. Implement Incrementally

Implement features in the order specified by the implementation prompt. For each feature:

1. Implement the feature according to its planning document
2. Compile or build to verify correctness
3. Fix any errors before moving to the next feature

Do not batch all implementation and then compile once at the end. Incremental verification catches errors early and reduces rework.

Infrastructure and scaffold (build configuration, project structure, dependency setup) typically come first, even if the planning documents number them differently, because everything else depends on a working build.

### 4. Maintain an Implementation Log

Create `implementation.md` in the ticket folder (e.g., `docs/pending/07-investigate-pipeline-jobs/implementation.md`). Update it as work progresses. The log should contain:

- **Work completed** — which features have been implemented, in what order, and their current state
- **Decisions made** — implementation choices where the planning documents left discretion (AI freedom sections), and why the choice was made
- **Inconsistencies found** — contradictions, ambiguities, or gaps discovered in the planning documents during implementation, and how they were resolved
- **Problems encountered** — anything that didn't work as expected, required iteration, or deviated from the plan

Keep entries concise and factual. If implementation is interrupted, the log should be sufficient for another session to continue.

### 5. Verify Completion

When all features are implemented:

- Confirm the build succeeds (compile, package, or equivalent)
- Confirm the project is launchable/runnable as described in the planning documents
- Update the implementation log with final status

### 6. Document

Follow the procedure in `actions/Document.md` to verify that the project's documentation (README, code comments, help text, etc.) is accurate and consistent with the changes just made.

### 7. Reflect

Follow the procedure in `actions/Reflect.md` to write a reflective assessment as `reflect.md` in the ticket's folder. This captures what went well, what could have gone better, and concrete recommendations for improving the planning documents, framework, or tooling.

## Guidance

- Follow the constraints in the planning documents strictly. Invariants and SHALL statements are non-negotiable. AI freedom sections are where discretion applies.
- When a planning document is ambiguous, make a reasonable choice, document it in the implementation log, and continue. Do not block on ambiguity.
- When a planning document contradicts another, note the inconsistency in the implementation log and resolve it in the direction that best serves the project's stated goals.
- Guidelines applied in step 1 apply throughout implementation. If a feature plan conflicts with a guideline, log the conflict and resolve it in the implementation log.
- The implementation log is the primary artifact beyond the code itself. It enables continuation after interruption and feeds the reflection process.
