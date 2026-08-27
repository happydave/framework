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
- `Intake.md` — zero-friction capture of raw ideas, observations, and dumps into the intake inbox for later triage
- `WorkItem.md` — create and manage work items
- `BugReport.md` — capture a defect as a structured work item with reproduction context
- `GitCommit.md` — stage and commit changes; no-op if the working directory is not a git repository
- `GitMerge.md` — plan and execute branch merges: survey divergence, select strategy, execute, record outcome
- `Merge.md` — execute one strategy in depth: audited squash-and-rebase of a diverged feature branch, with logical-conflict review
- `SideQuest.md` — execute and document one-off tasks with minimal overhead
- `Spike.md` — answer one feasibility/cost/design question with a throwaway build and a recorded verdict
- `Dispatch.md` — package context and instructions for a specialized agent session
- `Discover.md` — investigate products, APIs, or technology domains
- `WebResearch.md` — package single-shot research briefs for web-enabled AI sessions and harvest the replies
- `Investigate.md` — diagnose runtime system behavior using observability data
- `Triage.md` — turn the intake queue or a test/feedback dump into prioritized work items with root-cause hypotheses and flagged decisions
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
- `markdown.md` — quality gates for Markdown artifacts (link checking, structure verification, merge union check, spell checking)
- `sql.md` — SQL conventions for queries, schema, and migrations
- `versioning.md` — version increment policy: one ticket, one patch (Go projects exempt — they version via git tags)
- `claude-code.md` — Claude Code CLI usage reference for task delegation and automated operations
- `debug.md` — AI agent debugging methodology (structured hypothesis generation, bias mitigation)
- `evidence.md` — evidence assessment rules (Hub for Logs, Metrics, Groundcover)
- `authoring-skills.md` — how we write skills: directive not narrative, application-tested; synthesizes superpowers `writing-skills` + tickets `creating-skills`
- `tooling.md` — tool-selection policy and credential handling for external tools

**agents** (agent personas — attach when dispatching a specialized session)
- `Merge.md` — Merge Agent: drives `procedures/Merge.md` interactively
- `researcher.md` — research agent persona

**internal** (framework tooling — run these rather than reimplementing a check)
- `dupcheck.py` — duplicate-detection heuristic from `skills/markdown.md`; `internal/dupcheck.py FILE...`
- `DESIGN.md` — design notes for the workflow system itself

**knowledge** (reference material — look these up as needed; non-normative)
- `vscode-agent-registration.md` — registering agents for VS Code

## Typical Pipelines

- Project: `Create Project → Discover → Design → Design Review → Create Work Item(s)`
- Intake: `Capture (docs/intake/) → Triage → Work Item(s) or declined` (see `Intake.md`)
- Work Item: `Plan → Plan Review → Code → Code Review → Test → Document → Reflect → Git Commit → Complete`
- Rapid Iteration (exploratory/hardening): `Test → Triage → fix in groups → Reflect → Document` (loop; see `RapidIteration.md`)
- Spike (settle one question before planning): `Work Item → Design → Execute → Verdict → Reflect` (single `spike.md`; see `Spike.md`)

## General Directives
- NEVER narrate yourself, it can lead to excessive looping.
- ALWAYS use the `todo` tool (when available) rather than chat.
- **Read docs in full.** When you open a `workflow` doc or a project doc under `/home/dave/Documents/tickets`, read the entire file rather than a partial range. This applies to documentation only — **not** source code, which may contain very large files that are read selectively. "Read in full" is per-file: each doc you open is read whole; it does not mean every file in a tree must be opened. Files merely referenced by another doc are read only when directly relevant to the task.
