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
| `skills/` | Language and tooling conventions (Go, TypeScript, SQL, etc.) |
| `knowledge/` | Reference material (architecture diagrams, integration guides) |
| `internal/` | Design docs for the workflow system itself |

## Typical Pipelines

**New project:** Create Project → Discover → Design → Design Review → Create Work Items

**Work item:** Plan → Plan Review → Code → Code Review → Test → Document → Reflect → Git Commit → Complete

**Quick chore:** SideQuest (single execution + audit doc, no planning phase)

## License

UNLICENSE — see `UNLICENSE`.
