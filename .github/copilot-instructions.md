---
name: workflow-enforcement
description: "Always use when: performing tasks related to planning, implementation, testing, or documentation within this workspace. Enforces the procedures defined in the workflow/ directory."
---

# Workflow & Procedure Enforcement

This workspace follows the structured planning and implementation framework defined in the `workflow` directory.

## Core Directives
1. **Procedural First**: Before performing any task (Design, Work Item, Plan, Code, Test, etc.), search for the corresponding procedure in `workflow/procedures/` (e.g., `Plan.md`, `Code.md`, `WorkItem.md`).
2. **Follow Artifact Patterns**: Artifacts (plans, work items, implementation logs) MUST follow the naming conventions and structures defined in their respective procedures.
3. **Centralized Management**: All management artifacts live in the `tickets` repository under `docs/pending/`, `docs/projects/`, or `docs/archive/`.
4. **No Code in Plans**: Ensure `plan.md` files describe behavior and invariants without containing code snippets (structs, functions).
5. **Language and Tooling Guidelines**: Strictly adhere to the rules in `workflow/skills/` (Go, TypeScript, Docker, Markdown, tooling, etc.).

## Procedures Reference
- **Initiating Work**: Use `WorkItem.md` to capture new tasks in `docs/pending/`.
- **Planning**: Follow `Plan.md` and `PlanReview.md` before implementation begins.
- **Implementation**: Follow the `Code` procedure and maintain incremental `code.md` logs.
- **Verification**: Follow `Test.md` and produce formal `test.md` artifacts.
- **Completion**: Use `Complete.md` to update status and `Archive.md` for cleanup.

## Principles
- **Clear Intent**: Ensure the "why" and intended product usage are captured during Design and Planning. Intent is higher level than "building software"; it defines the value and use cases. (Note: Work items may be simple passing thoughts and are a partial exception).
- Be precise, objective, and unambiguous.
- Use SHALL statements for mandatory outcomes in plans.
- Respect "Explicit AI Freedom" sections in plans to optimize implementation details.
