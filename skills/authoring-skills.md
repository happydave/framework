---
name: authoring-skills
description: Use when creating or revising a skill — a reusable reference/technique/convention guide — deciding its format, what to include, and how to verify it before calling it done.
---

# Authoring Skills

## Overview

A skill is a **directive** reference guide for a technique, tool, or convention we have actually used, so
future sessions apply it without re-deriving it. Ours are almost all **Reference / Technique / Convention**
skills — not discipline-enforcing gates.

**Sources:** synthesizes `writing-skills` (superpowers — the format authority) and `creating-skills`
(tickets). Take what works; don't mold our skills to them 100%.

## When to write one

- A technique/tool/convention you would reference again across sessions.
- **Evidence-first:** skill something you have actually used — findings/code before the skill; a guide
  written ahead of real use is invented guidance. (For a ubiquitous standard tool, hands-on use + `--help`
  is enough.)
- **Not for:** one-off solutions; project-specific facts (→ `CLAUDE.md` / repo docs); anything a
  validation script enforces better than prose.

## Format

- A directory with `SKILL.md` (or a single `.md` under `workflow/skills/`, matching neighbours).
- YAML `---` frontmatter, keys `name` (hyphenated) + `description` only. `description` = **triggering
  conditions only** ("Use when …"), never a workflow summary — agents follow the summary and skip the body.
- Body: **directive, keyword-rich, aim under ~500 words** (whole-file `wc -w`; a target, not a gate — a
  runnable example may push a dense skill over).
- **Lead with the recipe. One runnable example** (flags/args stacking on a real invocation) **beats prose;**
  the table is the exhaustive reference. Add a **Common Mistakes** table only when you have real mistakes to
  counter — never invent them.

## Our two rules

- **Directive, not narrative.** No "we found / WI-123 proved / owner-confirmed" in the body — that's a
  ballad, not a guide. Provenance → a **one-line Source pointer** to the findings/code.
- **Separate the portable core from our-setup specifics** (recipe, hardware) so the reusable part travels.

## Verify before done (required)

**Application-test with a fresh subagent:** give it *only* the skill + a realistic task; confirm it produces
the right result **and** ask it to surface gaps. **Pass = a correct result and every correctness gap fixed**
(threshold/cosmetic nits optional). It catches missing examples, contradictions, and undocumented inputs
that self-review misses. This is a reference-level test — **not** the superpowers Iron-Law /
RED-GREEN-REFACTOR ceremony, which is for skills that enforce discipline under pressure.

## Where skills live

- Cross-cutting conventions → `workflow/skills/` (list in `AGENTS.md`); repo-specific guides → that repo's
  `skills/` (discoverable via its README); general techniques → `tickets/skills` or superpowers.

## Common mistakes

| Mistake | Correct approach |
|---|---|
| Narrative / WI-archaeology in the body | Directive; provenance → a Source line |
| `description` summarizes the workflow | Triggering conditions only |
| Skilling a tool you haven't used | Evidence-first — use it, then skill it |
| Shipping untested | Application-test with a subagent first |
| Inventing a Common Mistakes table to look complete | Include one only with real, earned entries |
| Full TDD ceremony on a reference skill | Reference-level application test |

## Explicit AI freedom

Choose section layout, the example, and which existing skill to model — no need to ask.
