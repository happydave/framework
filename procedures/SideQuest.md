# SideQuest

## Intent

Execute a one-off task, random chore, or minor investigation with minimal friction while preserving a basic audit trail. A SideQuest bypasses the heavy machinery of the standard workflow (Plan, Code, Review, Test, Document, Reflect) in favor of a single, free-form execution and documentation step.

SideQuests are for when the overhead of planning exceeds the value of the work itself, but doing the work completely undocumented is unacceptable.

## When to use SideQuest

- One-off scripting, data cleanup, or minor refactoring.
- Quick bug fixes that are trivial and carry negligible risk.
- Isolated research too trivial to warrant a `Discover`, `Investigate`, or `Spike` lifecycle. (A
  question with a real feasibility/cost answer and a design that matters belongs in `Spike.md`, not
  here — a mis-designed quick experiment measures the wrong thing convincingly.)
- Random tasks that "just need to get done."

DO NOT use SideQuest for:
- Features or complex bug fixes (use `Plan` -> `Code`).
- Changes that require strict security or architecture review.
- Anything that requires cross-component coordination.

## Procedure

### 1. Prerequisite: Work Item
A SideQuest must begin with a `workitem.md` in a `docs/pending/` folder to capture the original request, context, and any explicitly stated constraints.

### 2. Execution
The author (human or AI agent) performs the requested task directly based on the `workitem.md`. 
- No `plan.md` is required.
- No `code.md` log is maintained during the work.
- **Versioning**: SideQuests are explicitly **exempt** from standard project version increment rules (e.g., semantic version bumps) unless the work item explicitly requests a version bump.

### 3. Documentation
Upon completion of the work, the author creates a `sidequest.md` file in the work item folder. This single artifact replaces all other workflow documents for this task.

### 4. Completion
Once `sidequest.md` is written, the work item's `Status` is immediately changed to `complete` in `workitem.md`.

## The `sidequest.md` Template

Create `sidequest.md` in the work item folder using the following structure:

```markdown
# SideQuest: <Work Item Title>

## Original Request & Constraints
<!-- Briefly summarize what was asked and any rules provided (can be copied/adapted from workitem.md). -->

## What Was Done
<!-- Free-form narrative of the interesting details of the execution. What approach was taken? Were there any surprises? -->

## Audit Trail (What Changed and Why)
<!-- Bulleted list of specific files changed, scripts run, or configurations altered, and the rationale. -->
- `path/to/file`: <Reason for change>
- Ran command `xyz`: <Reason for execution>
```

## Guidance

- **Minimal Friction**: Do not over-document. The goal is an audit trail, not a novel.
- **Agent Handoff**: If an AI agent completes the SideQuest, it should write the `sidequest.md` and immediately execute the `Complete` action in the same session.
