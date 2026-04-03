# Project Planning Framework

## Purpose

This framework provides a structured approach for planning and documenting features with precise, unambiguous language that enables correct implementation on first attempt.

The goal is to produce plans so detailed and clear that an AI (or another human) can implement features correctly without guesswork or misalignment, while leaving non-critical decisions open for optimal choices.

## About

Important: This repository contains meta-instructions. It is a guide for creating feature plans, not a finished software product. We are currently refining this framework to ensure AI agents can understand and implement features correctly from the outset. Think of it like building the instruction manual before assembling the machine. At this stage, we are concerned with defining a consistent, unambiguous process — not specific feature requirements yet.

## Document Structure

This framework includes guidelines and core documents for creating plans and descriptions:

- **This README** — Overview of the entire system
- `actions/Ticket.md` — Lightweight intake for work items
- `actions/Discover.md` — Deep investigation of products, technologies, or domains
- `actions/Investigate.md` — Diagnose runtime system behavior using observability data
- `actions/Plan.md` — Complete workflow instructions and methodology
- `actions/Implement.md` — Implementation process (incremental implementation, implementation log)
- `actions/Reflect.md` — Post-implementation reflection and recommendations
- `actions/Document.md` — Verify documentation is accurate and consistent after changes
- `actions/Review.md` — Cooperative human+AI merge request review
- `templates/feature.md` — Instructions for writing lean, outcome-oriented feature plans
- `guidelines/Go.md` — Go-specific guidelines (module setup, tooling, conventions)
- `guidelines/TypeScript.md` — TypeScript/npm guidelines (Docker-based builds, VS Code extension conventions)
- `guidelines/Docker.md` — Container-first build environment guidelines

### Consumer Project Structure

When using this framework in a project, the project repository contains:

- `docs/pending/<ticket-id>/` — active work items, each containing `ticket.md`, `discover.md`, `plan.md`, `implementation.md`, `reflect.md` as they progress
- `docs/completed/<ticket-id>/` — finished work items (moved from `docs/pending/` on completion)

## Using This Framework

### For Project Documentation

Important: This repository contains the framework itself. It is intended to be referenced from inside other projects where the work is actually being done. 

The `templates/` and `guidelines/` folders live in this framework repository. 

When you start a new project (the consumer repository), you should scaffold `docs/pending/` and `docs/completed/` directories there to hold the active execution state.

When documenting an actual project's plans in your consumer repository:

1. **Create tickets for work items**  
   For each feature or task, create a folder in `docs/pending/` with a `ticket.md` inside.  
   Follow the guidance in the framework's `actions/Ticket.md`.

2. **Discover** (when needed)  
   If the work item requires investigation — evaluating a product, researching an API, or understanding a technology before planning — conduct discovery and add `discover.md` to the ticket's folder. Not every ticket needs discovery; skip this step when the domain is already well understood.  
   See the framework's `actions/Discover.md`.

3. **Investigate** (when needed)  
   If a work item involves diagnosing runtime system behavior — tracing callers, identifying error sources, or understanding what is actually happening in production — conduct an investigation and add `investigate.md` to the ticket's folder. Investigation may also happen independently of the planning workflow, prompted by an alert or operational question.  
   See the framework's `actions/Investigate.md`.

4. **Plan**  
   For each ticket that needs planning, add `plan.md` to the ticket's folder.  
   Follow the guidance in the framework's `templates/feature.md` .
   Refine until the Critical Assess step confirms the document is unambiguous and complete.  
   See the framework's `actions/Plan.md`.

5. **Implement**  
   Follow the feature plan to build the feature incrementally, maintaining an implementation log as you go.  
   See the framework's `actions/Implement.md`.

6. **Review**  
   When the change is ready (or ready for early feedback), submit a merge request and conduct a cooperative human+AI review. The AI scans the full diff for correctness, safety, consistency, and mechanical issues; the human provides intent context, resolves uncertain findings, and delivers the verdict.  
   See the framework's `actions/Review.md`.

7. **Document**  
   Verify that the project's documentation (README, code comments, help text, etc.) is accurate and consistent with the changes just made.  
   See the framework's `actions/Document.md`.

8. **Reflect**  
   After implementation, capture what went well, what didn't, and concrete recommendations for improving the process, plans, or tooling.  
   See the framework's `actions/Reflect.md`.

9. **Complete**  
   Move the ticket folder from `docs/pending/` to `docs/completed/`.

## Plan Style

### Language & Tone

- Plain Markdown only
- Concise, objective, strictly descriptive
- Minimal rhetorical flourish
- No code blocks unless explaining plan format
- Explicitly grant AI freedom in non-critical areas (see `templates/feature.md`)

## Expected Output Quality

A healthy feature plan satisfies:

- Clear objective and non-negotiable invariants
- Behaviors and verifications sufficient to confirm correctness without guesswork
- Edge cases and error responses covered where significant
- No unstated assumptions or contradictions
- Critical decisions stated; non-critical ones left open
- Human and AI remain collaboratively involved throughout refinement

## License

This project is released into the public domain under the [Unlicense](https://unlicense.org/).  
You are free to use, modify, distribute, and do whatever you want with it — no restrictions, no attribution required.