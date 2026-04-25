# Project Planning Framework

## Purpose

A structured approach for planning and documenting features with precise, unambiguous language that enables correct implementation on first attempt.

The goal is to produce plans so detailed and clear that an AI (or another human) can implement features correctly without guesswork or misalignment, while leaving non-critical decisions open for optimal choices.

## About

This repository contains meta-instructions — a guide for creating feature plans, not a finished software product. Think of it as the instruction manual before assembling the machine: we define a consistent, unambiguous process first.

## File Layout

**Actions** — step-by-step procedures for each phase:
- `Ticket.md` — intake for work items (keep them short)
- `Discover.md` — investigate products, APIs, or technology domains before planning
- `Investigate.md` — diagnose runtime system behavior using observability data
- `Plan.md` — produce a feature plan with enough detail for correct first-pass implementation
- `Implement.md` — implement incrementally from plans, maintaining an implementation log
- `CodeReview.md` — cooperative human+AI merge request review of implementation artifacts
- `PlanReview.md` — independent evaluation of plan documents before implementation begins
- `Document.md` — verify documentation accuracy after changes
- `Reflect.md` — capture what went well, what didn't, and concrete recommendations

**Guidelines** — language/tooling-specific rules:
- `TypeScript.md` — VS Code extension / Node.js conventions (Docker-based builds)
- `Go.md` — Go module setup, tooling, conventions
- `Docker.md` — container-first build environment (`Dockerfile.dev` + `Makefile` pattern)
- `Evidence.md` — evidence assessment rules for investigations

## Typical Workflow

```
Ticket → Plan → Plan Review → Implement → Code Review → Reflect
       ↑        ↓              ↑         ↑
    Discover (optional, any)  Investigate (optional, any)
```

1. **Ticket** — capture the work item in `docs/pending/<id>/ticket.md`
2. **Plan** — produce `plan.md` following the guidance in `actions/Plan.md`
3. **Plan Review** — independent evaluation of the plan document before implementation begins
4. **Implement** — build incrementally per plan, log decisions in `implementation.md`
5. **Code Review** — cooperative human+AI review of merge requests after implementation
6. **Reflect** — capture lessons in `reflect.md`, move folder to `docs/completed/`

*Discover and Investigate are optional actions available at any point — before Plan, between steps, or in isolation.*

### Consumer Project Setup

When using this framework in a project repo, scaffold `docs/pending/` and `docs/completed/` directories there. The full set of action documents (Ticket through Reflect) and guidelines live in this framework repository.
