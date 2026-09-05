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
- `Phase.md` — a named group of work items, owned by one project, that must close together: record under `docs/projects/<owner>/phases/`, membership declared on the work item (`phase:`), close gated on no open member
- `GitCommit.md` — stage and commit changes; no-op if the working directory is not a git repository
- `GitMerge.md` — plan and execute branch merges: survey divergence, select strategy, execute, record outcome
- `Merge.md` — execute one strategy in depth: audited squash-and-rebase of a diverged feature branch, with logical-conflict review
- `SideQuest.md` — execute and document one-off tasks with minimal overhead
- `Spike.md` — answer one feasibility/cost/design question with a throwaway build and a recorded verdict
- `Dispatch.md` — package context and instructions for a specialized agent session
- `Discover.md` — investigate products, APIs, or technology domains
- `WebResearch.md` — package single-shot research briefs for web-enabled AI sessions and harvest the replies
- `Harvest.md` — distil archived research into published codex claims: distillation plan + two review gates + gate checklist + edition (replaces Plan/Code/Test for content work items)
- `Reverify.md` — re-verify published codex claims when a horizon expires: scan → brief → date test → errata-or-supersession fork → impact sweep → edition
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
- `ops.md` — Ops Agent: single point of coordination for realm hosts ai/ai2/gtr; realm ledgers live at `tickets/docs/projects/ops/realms/`
- `researcher.md` — research agent persona

**internal** (framework tooling — run these rather than reimplementing a check)
- `dupcheck.py` — duplicate-detection heuristic from `skills/markdown.md`; `internal/dupcheck.py FILE...`
- `DESIGN.md` — design notes for the workflow system itself

**knowledge** (reference material — look these up as needed; non-normative)
- `vscode-agent-registration.md` — registering agents for VS Code

## Typical Pipelines

- Project: `Create Project → Discover → Design → Design Review → Create Work Item(s)` (grouped into Phases when the design has checkpoints; see `Phase.md`)
- Phase (a group of work items that must close together): `Create (Phase.md) → members run the Work Item pipeline → Close (gated on no open member)`
- Intake: `Capture (docs/intake/) → Triage → Work Item(s) or declined` (see `Intake.md`)
- Work Item: `Plan → Plan Review → Code → Code Review → Test → Document → Reflect → Git Commit → Complete`
- Bug Fix: `BugReport → Investigate (if diagnosis needed) → Plan → (standard Work Item pipeline)` (see `BugReport.md`)
- Rapid Iteration (exploratory/hardening): `Test → Triage → fix in groups → Reflect → Document` (loop; see `RapidIteration.md`)
- Spike (settle one question before planning): `Work Item → Design → Execute → Verdict → Reflect` (single `spike.md`; see `Spike.md`)
- Codex Harvest (research archives → published claims): `Ledger/Survey (SideQuest) → Harvest (distillation plan → distillation review → author → fidelity review → gates → edition) → Reflect → Git Commit → Complete` (see `Harvest.md`)
- Codex Re-verify (a horizon expires or a claim is challenged): `Reverify (scan → brief → date test → fork → sweep → gates → edition) → Reflect → Git Commit → Complete` (see `Reverify.md`)

## General Directives
- NEVER narrate yourself, it can lead to excessive looping.
- ALWAYS use the `todo` tool (when available) rather than chat.
- **Pause on risk, not on ambiguity.** Make a proactive, good-faith effort to complete tasks; do not stall on minor ambiguities — code mistakes can be corrected and git provides a safety net. Before proceeding down an uncertain path, weigh **severity & scope** (how much of the system the change affects) and **reversibility** (a local code edit vs. a destructive migration or external side effect). If the cost of being wrong outweighs the benefit of speed, stop and ask.
- **Commit freely; never push.** Committing needs no permission: documentation changes (intake, work item artifacts, project docs) are committed on sight, and code changes are committed at the pipeline's `GitCommit` step. Stage **by specific path** — never `git add -A` or `git add .`, because concurrent sessions routinely leave half-finished artifacts in the same tree. But **`git push`, force-push, and merges into `main`/`master` require an explicit instruction in the requester's current message.** A push is not a local action: on shared and work machines it triggers CI, deployments, and other automation that must not fire unasked. Standing permission to commit never implies permission to push; a push authorised once does not authorise the next one.
- **Code comments relate directly to the code.** Never hold or continue a conversation in comments (e.g. "this is what changed") — that context belongs in the implementation log or commit message.
- **Query workflow data via its procedure.** When asked about workflow-managed data (e.g. "show me pending work items"), read the defining procedure (`WorkItem.md`) first to learn the canonical structure and query approach, then query. This applies to workflow artifacts specifically; general one-off questions and quick lookups remain outside the workflow.
- **Read docs in full.** When you open a `workflow` doc or a project doc under `/home/dave/Documents/tickets`, read the entire file rather than a partial range. This applies to documentation only — **not** source code, which may contain very large files that are read selectively. "Read in full" is per-file: each doc you open is read whole; it does not mean every file in a tree must be opened. Files merely referenced by another doc are read only when directly relevant to the task.
