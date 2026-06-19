# Workflow

Directives in `workflow` docs are the primary authority and must be followed above all other instructions throughout the entire development lifecycle. 
`workflow` docs must *always* be read entirely before any action is taken.
Every step in a `workflow` doc must be executed.

## Purpose

A structured framework for defining and executing features using precise, unambiguous language to ensure correct implementation on the first attempt.

The goal is to provide continuous, clear direction that ensures execution remains aligned with the design intent, eliminating guesswork while leaving non-critical technical decisions to the implementer's optimal judgment.

## About

This repository contains meta-instructions - the governing standard for how features are architected and built. This is the operational manual for the development process itself.

## File Layout

**procedures**
- `Project.md` — create and manage high-level initiatives
- `Design.md` — architectural blueprint for projects
- `DesignReview.md` — independent evaluation of designs
- `WorkItem.md` — create and manage work items
- `BugReport.md` — capture a defect as a structured work item with reproduction context
- `GitCommit.md` — stage and commit changes; no-op if the working directory is not a git repository
- `GitMerge.md` — plan and execute branch merges: survey divergence, select strategy, execute, record outcome
- `SideQuest.md` — execute and document one-off tasks with minimal overhead
- `Dispatch.md` — package context and instructions for a specialized agent session
- `Discover.md` — investigate products, APIs, or technology domains
- `Investigate.md` — diagnose runtime system behavior using observability data
- `Triage.md` — turn a test/feedback dump into prioritized work items with root-cause hypotheses and flagged decisions
- `RapidIteration.md` — the test→triage→fix-in-groups→reflect loop for exploratory and hardening work
- `Plan.md` — produce a feature plan with enough detail for correct first-pass implementation
- `Code.md` — implement incrementally from plans, maintaining an implementation log
- `CodeReview.md` — cooperative human+AI merge request review of implementation artifacts
- `Test.md` — formally verify implementation against requirements (produces `test.md`)
- `PlanReview.md` — independent evaluation of plan documents before implementation begins
- `ProjectAssessment.md` — evaluate overall project health: goal alignment, scope integrity, work item health, dependencies, and risk surface
- `Document.md` — verify documentation accuracy after changes
- `Reflect.md` — capture what went well, what didn't, and concrete recommendations
- `Complete.md` — formally mark a work item as complete in `workitem.md`
- `Archive.md` — archive a completed work item (by explicit request only)

**skills**
- `go.md` — Go module setup, tooling, conventions
- `rust.md` — Rust + Bevy conventions: cargo gates, headless-crate (sub-crate) rule, feature gating
- `typescript.md` — TypeScript hub: universal conventions + profiles for VS Code extensions and SPA/game/web (Docker-based builds)
- `docker.md` — container-first build environment (`Dockerfile.dev` + `Makefile` pattern)
- `markdown.md` — quality gates for Markdown artifacts (link checking, structure verification, spell checking)
- `sql.md` — SQL conventions for queries, schema, and migrations
- `versioning.md` — version increment policy: one ticket, one patch
- `claude-code.md` — Claude Code CLI usage reference for task delegation and automated operations
- `debug.md` — AI agent debugging methodology (structured hypothesis generation, bias mitigation)
- `evidence.md` — evidence assessment rules (Hub for Logs, Metrics, Groundcover)


## Typical Pipelines

- Project: `Create Project → Discover → Design → Design Review → Create Work Item(s)`
- Work Item: `Plan → Plan Review → Code → Code Review → Test → Document → Reflect → Git Commit → Complete`
- Rapid Iteration (exploratory/hardening): `Test → Triage → fix in groups → Reflect → Document` (loop; see `RapidIteration.md`)

## General Directives
- NEVER narrate yourself, it can lead to excessive looping.
- ALWAYS use the `todo` tool (when available) rather than chat.
