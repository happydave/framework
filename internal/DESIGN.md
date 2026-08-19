# Workflow Framework Design

This document records the design principles, naming conventions, and structural decisions governing the development of this framework. It is intended for framework maintainers, not end-users.

## Core Intent

The primary goal of this framework is to enable the production of high-quality code with high confidence in implementation accuracy and integrity. To achieve this, the design follows these principles:

- **Centralized Workflow Definition**: The authoritative workflow sequence and structure are defined in `AGENTS.md`. Individual procedure documents (`procedures/*.md`) should focus on the internal procedure of that specific step and avoid redundantly specifying the broader workflow context.
- **Automation-Ready**: The workflow is intended to operate within a largely automated process. Procedures and roles (Reviewer, Author) are defined to be actor-agnostic, allowing for seamless integration into automated pipelines with minimal human oversight.
- **Durable Audit Trail**: Every action produces structured markdown artifacts (e.g., `plan.md`, `code.md`, `reflect.md`). This provides a clear audit trail for:
    - **Instruction Accuracy**: The `Dispatch` procedure ensures the exact instructions and context provided to execution agents are recorded in `briefs/`.
    - **Accuracy Verification**: Confirming implementation matches planning and requirements.
    - **Troubleshooting**: Diagnosing where a process failed or where ambiguity was introduced.
    - **Continuous Improvement**: Using historical artifacts to identify patterns and refine the framework itself.

## Naming Conventions

### File Naming
- **Workflow Guidance Documents**: All files in `procedures/`, `skills/`, and `agents/` must use **PascalCase** (e.g., `Plan.md`, `TypeScript.md`, `WorkItem.md`). This distinguishes the framework's authoritative instructions from project-specific artifacts.
- **Projects vs. Work Items**: 
    - **Projects** are high-level initiatives tracked in `docs/projects/<slug>/project.md`. 
    - **Work Items** are tactical units of work tracked in `docs/pending/<id>/workitem.md`. 
- **Work Items vs. Tickets**: We use the term **Work Item** to describe the conceptual unit of work (feature, bug, task). The term **Ticket** is reserved for the physical reference identifier. Files created within specific work item folders must use **lowercase-kebab-case** and the work item's root document is always named `workitem.md` (e.g., `workitem.md`, `plan.md`, `code.md`, `debug.md`). This makes them visually distinct from the framework files.

### Referencing
- When a document refers to a framework file, use the capitalized name: "Follow the steps in `Plan.md`."
- When a document refers to a project's specific instance, use the lowercase name: "The project manifest is found in `project.md`."
- When a document refers to a work item's specific instance, use the lowercase name: "The author provides the `plan.md` from the folder."

## Structural Principles

- **Centralized Orchestration**: The framework moves away from keeping work items inside individual code repositories. Instead, work items and projects are managed in a central "tickets" repository, while implementation spans multiple "target" repositories.
- **Actor Agnosticism**: Procedures should be written to be performed by a "Reviewer" or "Author" rather than explicitly "Human" or "AI." This allows the framework to transition from human-driven to AI-driven to fully automated without rewriting the core logic.
- **Separation of Concerns**: `procedures/` define *what* to do; `guidelines/` define *how* to do it in specific contexts (languages, tools); `agents/` define *who* executes the procedure (for AI-driven steps).
- **Independent Verification**: Where possible, critical steps (like Design Review and Plan Review) should be designed as external gates that don't rely solely on the original author's self-assessment.
- **Positive Instruction Framing**: Where possible, write guidance as affirmative requirements rather than prohibitions. LLMs respond more reliably to positive constraints ("each invariant must trace to the work item") than to negative ones ("never add unstated invariants"). When a prohibition is tempting, look for the positive gate that achieves the same result — a traceability check, a "before doing X, verify Y" step, or a criterion the output must satisfy.
- **Agent Task Suitability**: Subagents are appropriate for tasks where the output is grounded and verifiable by inspection — file moves, code changes that will be diff'd, search results. They are poorly suited to analytical tasks (plan review, code review) where prose output can be fabricated without reading the actual artifacts: a cold-start agent has no conversation context, receives only a folder path, and can pattern-match from its role definition to produce structurally correct but factually invented output. For analytical review steps, inline execution by the orchestrating session is preferred — it already has context, has already read relevant files, and does not have this trust gap.
- **Context Optimization**: To minimize token pressure and align with LLM initial read limits, core framework documents follow a principle of "progressive context disclosure."
    - **100-Line Target**: Primary skills and procedures aim to remain under 100 lines.
    - **Modular Decomposition**: If a topic requires extensive detail, the primary file provides the mandatory "High-Level Invariants" and links to specialized sub-documents for implementation details.
