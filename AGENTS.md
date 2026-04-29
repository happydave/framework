# Agent Registry

## Purpose
This document is the central registry for the AI agents defined in this framework. It maps **Procedures** (how to work) to **Agents** (the automated actors), enabling both humans and other AI to discover and invoke the correct capability for any workflow step.

## Agent Directory

| Agent | Target Procedure | Role | Location |
|---|---|---|---|
| **Work Item Agent** | `WorkItem.md` | Intake and clarify work; create `ticket.md`. | `agents/WorkItem.md` |
| **Discover Agent** | `Discover.md` | Research domains and APIs; create `discover.md`. | `agents/Discover.md` |
| **Explore** | (Read-only) | Fast codebase exploration and Q&A. | (Built-in) |

*Planned Agents: Planner (`Plan.md`), Reviewer (`PlanReview.md`), Implementer (`Implement.md`), Documenter (`Document.md`), Reflector (`Reflect.md`), Archiver (`Archive.md`).*

## Interaction Principles

### 1. Progressive Context Disclosure
To optimize for AI context limits (e.g., 100-line initial peeks), this registry provides only the "What" and "Where." Full "How" logic is deferred to specific agent files, which in turn reference Procedural source files only when active.

### 2. Standard Handoffs
Agents are workflow-aware. Upon successful completion of a task, an agent SHALL indicate the next logical step and suggest the appropriate agent to the user (e.g., "**Work Item** complete. You may now invoke the **Planner Agent**"). Handoffs typically end with the **Reviewer Agent** executing the **Complete** action.

### 3. Actor-Agnostic Design
Agents are designed to follow the procedures in `procedures/*.md` exactly as a human would. This ensures that the framework's core logic remains the single source of truth, regardless of whether a human or AI is performing the step.

## How to Invoke
In supported editors (like VS Code), agents can be invoked by name (e.g., `@Work Item Agent`) or via the command palette. Each agent is configured to automatically read the relevant `Procedure` and `Guideline` documents upon activation.
