# Workflow

A structured framework for defining and executing software features using precise, unambiguous language. Designed to be operated by AI coding agents (Claude Code, Copilot, etc.) under human direction.

## What It Is

This repository contains the meta-instructions that govern how features are architected and built. It is the operational manual for the development process itself — not a code repository.

## How It Works

**`AGENTS.md`** is the entry point for AI agents. It contains the authoritative directives, procedure index, and pipeline definitions that agents must follow.

Point your agent at it by adding to your `CLAUDE.md` (or equivalent):

```
@/path/to/workflow/AGENTS.md
```

The agent reads `AGENTS.md` at the start of each session and consults the referenced procedures as work progresses.

## Directory Layout

| Directory | Contents |
|-----------|----------|
| `procedures/` | Step-by-step process documents (Plan, Code, Review, etc.) |
| `agents/` | Agent personas to attach when dispatching a specialized session |
| `skills/` | Language and tooling conventions (Go, TypeScript, SQL, etc.) |
| `knowledge/` | Reference material (architecture diagrams, integration guides) |
| `internal/` | Design docs and tooling for the workflow system itself |

## Typical Pipelines

**New project:** Create Project → Discover → Design → Design Review → Create Work Items

**Intake:** Capture (`docs/intake/`) → Triage → Work Item(s) or declined

**Work item:** Plan → Plan Review → Code → Code Review → Test → Document → Reflect → Git Commit → Complete

**Quick chore:** SideQuest (single execution + audit doc, no planning phase)

**Bug fix:** BugReport → Investigate (if diagnosis needed) → Plan → the work item pipeline

**Rapid iteration (exploratory/hardening):** Test → Triage → fix in groups → Reflect → Document, looped

**Spike (settle one question before planning):** Work Item → Design → Execute → Verdict → Reflect, in one `spike.md`

**Codex harvest (`Harvest.md`):** Ledger/Survey → Harvest (distillation plan → distillation review → author → fidelity review → gates → edition) → Reflect → Git Commit → Complete

**Codex re-verify (`Reverify.md`):** a horizon expires or a claim is challenged → Reverify (scan → brief → date test → fork → sweep → gates → edition) → Reflect → Git Commit → Complete

## License

UNLICENSE — see `UNLICENSE`.
