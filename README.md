# Project Planning Framework

## Purpose

A structured approach for planning and documenting features with precise, unambiguous language that enables correct implementation on first attempt.

The goal is to produce plans so detailed and clear that an AI (or another human) can implement features correctly without guesswork or misalignment, while leaving non-critical decisions open for optimal choices.

## About

This repository contains meta-instructions — a guide for creating feature plans, not a finished software product. Think of it as the instruction manual before assembling the machine: we define a consistent, unambiguous process first.

The workflow is supported by **Agents** — automated actors that help execute specific procedures. See [AGENTS.md](AGENTS.md) for the full registry of available capabilities.

## File Layout

**Actions** — step-by-step procedures for each phase:
- `Project.md` — initiate and manage high-level initiatives
- `Design.md` — architectural blueprint for projects
- `DesignReview.md` — independent evaluation of designs
- `WorkItem.md` — intake for work items (keep them short)
- `Discover.md` — investigate products, APIs, or technology domains
- `Investigate.md` — diagnose runtime system behavior using observability data
- `Plan.md` — produce a feature plan with enough detail for correct first-pass implementation
- `Implement.md` — implement incrementally from plans, maintaining an implementation log
- `CodeReview.md` — cooperative human+AI merge request review of implementation artifacts
- `PlanReview.md` — independent evaluation of plan documents before implementation begins
- `Document.md` — verify documentation accuracy after changes
- `Reflect.md` — capture what went well, what didn't, and concrete recommendations
- `Complete.md` — formally mark a work item as complete in `workitem.md`
- `Archive.md` — move a completed work item folder to `docs/archive/` or a project's archive folder

**Guidelines** — language/tooling-specific rules:
- `Markdown.md` — quality gates for Markdown artifacts (link checking, structure verification, spell checking)
- `TypeScript.md` — VS Code extension / Node.js conventions (Docker-based builds)
- `Go.md` — Go module setup, tooling, conventions
- `Docker.md` — container-first build environment (`Dockerfile.dev` + `Makefile` pattern)
- `Evidence.md` — evidence assessment rules (Hub for Logs, Metrics, Groundcover)
- `Debug.md` — AI agent debugging methodology (structured hypothesis generation, bias mitigation)

## Typical Workflow

```
Project → Design → Design Review → Work Item → Plan → Plan Review → Implement → Code Review → Document → Reflect → Complete (→ Archive)
```

1. **Project** — define high-level initiatives in `docs/projects/<slug>/project.md`
2. **Design** — architectural blueprint in `docs/projects/<slug>/design.md`
3. **Design Review** — evaluate design against project goals (Gate: status $\rightarrow$ `Designed`)
4. **Work Item** — capture work items in `docs/pending/<id>/workitem.md` (centralized management)
5. **Plan** — produce `plan.md` following the guidance in `procedures/Plan.md`
6. **Plan Review** — independent evaluation of the plan document before implementation begins
7. **Implement** — build incrementally per plan, log decisions in `implementation.md`
8. **Code Review** — cooperative human+AI review of merge requests after implementation
9. **Document** — verify documentation accuracy and consistency after changes
10. **Reflect** — capture lessons in `reflect.md`
11. **Complete** — update status to `complete` in `workitem.md`

*Discover and Investigate are optional procedures available at any point — before Plan, between steps, or in isolation. Research is assisted by the **Discover Agent**. Archive is an optional final step to move completed items to long-term storage (either general or project-specific).*

### Consumer Project Setup

When using this framework, scaffold `docs/projects/`, `docs/pending/`, and `docs/archive/` directories in your central ticket/management repository. Work items are managed here, while code changes occur in their respective repositories. The full set of procedure documents and guidelines live in this framework repository.
