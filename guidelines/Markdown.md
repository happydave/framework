# Markdown Guidelines

## Purpose
These guidelines define quality gates for Markdown artifacts produced by the workflow framework — plans, tickets, documentation, and other `.md` files that form the primary language of the framework itself.

The checks fall into two categories: **build** procedures (deterministic pass/fail gates) and **test** procedures (advisory quality signals). Build failures block ticket closure; test results flag issues for human review.

## Core Principles
- Markdown is the native artifact format of this framework; quality checks are directly applicable to the framework's own output.
- Distinguish clearly between hard gates (build) and advisory signals (test).
- Prefer simple, automatable procedures over manual inspection where possible.
- Explicitly grant freedom on non-critical choices to avoid unnecessary decision overhead during implementation.

## Build Procedures — Link Checking
Internal link validation is a mandatory build gate: every `#heading` reference and relative file path in Markdown must resolve to an existing target within the workspace.

**Scope:**
- **Internal links** (relative paths, heading anchors) MUST be verified on every run. Broken internal links are a hard failure — the artifact does not pass build until all links are resolved or removed.
- **External links** (URLs) SHOULD be checked optionally. External link checking is noted as advisory rather than mandatory to avoid CI fragility from upstream URL rot. When external links are included in scope, only check links within this project's own repository (e.g., references to `procedures/Plan.md`) — treat them as internal cross-references that must resolve.

**Placeholder handling:**
Generated or templated Markdown may contain placeholder markers such as `#TODO` or section headers left for later filling-in during active drafting. These are acceptable while a document is in progress but MUST be removed before ticket close. A link checker should treat known placeholder patterns (e.g., paths containing `TODO`, `FIXME`, `REPLACE`) as non-fatal only when the artifact has not yet been marked complete.

**Cross-references to pending tickets:**
A plan may reference a ticket whose `plan.md` does not yet exist because the referenced ticket is still in `docs/pending/`. Internal link checks should verify that the *path* resolves, not whether the target content is complete or correct. A broken path (file does not exist) is a failure; an existing but empty or partially written target is acceptable.

## Build Procedures — Structure Verification
Structural requirements ensure every framework artifact contains the sections needed for it to function as intended by the workflow process. Structural failures are hard gates.

**`ticket.md` required sections:**
- An `Objective` or `Description` section (title of what the work item is).
- A `Proposed Changes` section (what will be created, modified, or removed).
- An `Acceptance Criteria` section (concrete conditions for closure).

**`plan.md` required sections:**
- `Objective` — states the goal concisely.
- `Invariants & Hard Constraints` — non-negotiable rules.
- `Required Behaviors & Verifications` — specific checks to perform.
- `Explicit AI Freedom` — discretionary areas where the implementer has latitude (per Plan.md action requirements).

**General documentation artifacts:**
Should include a heading hierarchy that starts with `#` for the title and uses `##` for major sections, descending logically from there. This ensures consistent structure across all framework output.

When structural verification is automated, missing required sections should produce a clear pass/fail result identifying which sections are absent.

## Test Procedures — Spell Checking
Spell checking is recommended as an advisory quality signal to help catch typos in technical terminology where dictionary coverage may be limited.

**Recommendations:**
- Maintain or reference a project-specific word list for domain terms that standard spell checkers will flag (e.g., "planreview", "kebab-case", "PascalCase", "markdownlint"). This reduces false positives significantly.
- Configure the spell checker's dictionary rather than suppressing non-English words entirely — non-ASCII content in tickets or documentation should be handled by dictionary configuration, not blanket exclusions.

Spell checking is advisory: flagged items are potential issues for human review, not automatic failures.

## Test Procedures — Duplicate Detection
Identifying duplicated or near-duplicated text blocks across Markdown artifacts helps catch copy-paste errors and stale content that often accumulates during iterative drafting.

**Heuristic:**
Any block of 8 or more consecutive words that appears more than once within the same document should be flagged for review. This simple word-count approach is sufficient to surface most problematic duplications without requiring complex n-gram analysis.

Focus on plan and ticket documents where repetition often indicates content that was copied from one section without updating, or from a previous iteration of the same document.

## Test Procedures — Grammar & Readability
Lightweight grammar and readability checks are optional advisory quality signals. The goal is clarity, not stylistic perfection.

**Guidance:**
- Short, direct sentences are preferred over complex constructions in technical writing.
- Over-correction can harm communication: automated grammar tools often suggest changes that are technically correct but obscure meaning or alter intent. Use flagged suggestions with judgment.
- Readability metrics (e.g., sentence length averages) may be checked optionally to flag documents that have become unwieldy, but no specific grade-level target is mandated.

## When to Apply Checks
**Build procedures** (link checking, structure verification) SHOULD run after every implementation step that modifies Markdown files and MUST pass before closing a ticket. These are fast, deterministic checks with clear outcomes.

**Test procedures** (spell check, duplicate detection, grammar checks) SHOULD run periodically or at ticket close time — not necessarily after each small incremental change, as they can produce noise during active writing and may flag issues that resolve themselves in subsequent edits.

## Explicit AI Freedom
The AI has full discretion over:
- Which specific tools to reference as examples for each check type (link checkers, spell checkers, linters) — if any are named at all
- The exact ordering of sections within this document, provided the build/test distinction is clear
- Whether duplicate detection is described using a word-count or character-n-gram approach
- How placeholder markers are identified (pattern list vs. metadata flag)

## Usage
Reference this file in plan documents when Markdown artifacts are produced, modified, or reviewed as part of implementation. Follow these rules automatically unless a plan explicitly overrides them.
