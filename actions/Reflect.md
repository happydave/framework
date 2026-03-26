# Reflect

## Intent

After implementation completes, capture what happened so the process, documentation, and tooling improve over time. This is not a narrative — it is a structured record that feeds concrete changes back into the planning framework, feature templates, guidelines, and implementation prompts.

The reflection should be written by the AI that performed the implementation, reviewed by the human, and stored alongside the other ticket artifacts.

## When to Reflect

At the end of every implementation, or when implementation is interrupted and will be resumed in a new session.

## Document Storage

Create `reflect.md` in the ticket's folder alongside `ticket.md`, `plan.md`, and `implementation.md` (e.g., `docs/pending/07-investigate-pipeline-jobs/reflect.md`).

## Procedure

### 1. Record What Went Well

Identify aspects of the implementation that worked effectively. These may include:

- Planning documents that were clear and sufficient
- Implementation order or sequencing that avoided rework
- Constraints that prevented mistakes
- Tooling or infrastructure that worked as expected
- Scope discipline that kept the implementation focused

The purpose is to reinforce what should be preserved or repeated.

### 2. Record What Could Have Gone Better

Identify friction, errors, and rework during implementation. For each item, note:

- What happened
- Why it happened (root cause if apparent)
- How it was resolved

Focus on issues that originated from the process, documentation, or tooling — not incidental problems like a service being temporarily unavailable.

### 3. Produce Recommendations

For each significant issue, propose a concrete change to prevent or reduce it in future implementations. Recommendations should target specific documents or artifacts:

- Feature plans (e.g., add a missing invariant to feature 08)
- Framework templates (e.g., add a section to `templates/feature.md`)
- Framework guidelines (e.g., update `guidelines/Docker.md`)
- Implementation prompts (e.g., add an instruction to compile incrementally)
- Makefile or tooling (e.g., add a pre-flight check)

Avoid vague recommendations. "Improve documentation" is not actionable. "Add an invariant to feature 08 stating that `.vscode/tasks.json` commands must use Makefile targets" is.

### 4. Human Review

The human reviews the reflection and decides which recommendations to act on. Not every recommendation warrants a change — some may be one-off issues not worth codifying.

## Guidance

- Keep entries concise and factual.
- Separate problems caused by documentation gaps from problems caused by implementation errors. Both are worth recording, but they have different fixes.
- If the implementation was interrupted and resumed, note where the break occurred and whether the implementation log was sufficient to continue.
- The reflection is a companion to the implementation log — it exists to feed improvements back into the process, not to stand alone.
