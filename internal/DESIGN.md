# Workflow Framework Design

This document records the design principles, naming conventions, and structural decisions governing the development of this framework. It is intended for framework maintainers, not end-users.

## Core Intent

The primary goal of this framework is to enable the production of high-quality code with high confidence in implementation accuracy and integrity. To achieve this, the design follows these principles:

- **Centralized Workflow Definition**: The authoritative workflow sequence and structure are defined in `README.md`. Individual procedure documents (`procedures/*.md`) should focus on the internal procedure of that specific step and avoid redundantly specifying the broader workflow context.
- **Automation-Ready**: The workflow is intended to operate within a largely automated process. Procedures and roles (Reviewer, Author) are defined to be actor-agnostic, allowing for seamless integration into automated pipelines with minimal human oversight.
- **Durable Audit Trail**: Every action produces structured markdown artifacts (e.g., `plan.md`, `implementation.md`, `reflect.md`). This provides a clear audit trail for:
    - **Accuracy Verification**: Confirming implementation matches planning and requirements.
    - **Troubleshooting**: Diagnosing where a process failed or where ambiguity was introduced.
    - **Continuous Improvement**: Using historical artifacts to identify patterns and refine the framework itself.

## Naming Conventions

### File Naming
- **Workflow Guidance Documents**: All files in `procedures/` and `guidelines/` must use **PascalCase** (e.g., `Plan.md`, `TypeScript.md`). This distinguishes the framework's authoritative instructions from project-specific artifacts.
- **Ticket Artifacts**: Files created within specific ticket folders (e.g., in `docs/pending/`) must use **lowercase-kebab-case** (e.g., `ticket.md`, `plan.md`, `implementation.md`). This makes them visually distinct from the framework files.

### Referencing
- When a document refers to a framework file, use the capitalized name: "Follow the steps in `Plan.md`."
- When a document refers to a ticket-specific instance, use the lowercase name: "The author provides the `plan.md` from the ticket folder."

## Structural Principles

- **Actor Agnosticism**: Procedures should be written to be performed by a "Reviewer" or "Author" rather than explicitly "Human" or "AI." This allows the framework to transition from human-driven to AI-driven to fully automated without rewriting the core logic.
- **Separation of Concerns**: `procedures/` define *what* to do; `guidelines/` define *how* to do it in specific contexts (languages, tools).
- **Independent Verification**: Where possible, critical steps (like Plan Review) should be designed as external gates that don't rely solely on the original author's self-assessment.
