# Bug Report

## Intent

Guide a reporter through capturing a defect as a structured work item. Every bug report produced by this procedure contains the minimum information needed to reproduce, triage, and plan a fix.

Follow this procedure from start to finish. It produces a work item folder and `workitem.md` — you do not need to read `WorkItem.md` separately.

## Required Fields

Every bug report must include these three fields. Do not skip them.

- **Product** — which system, service, or component exhibits the defect (e.g., `lmstudio-copilot`, `raji`, `piper-voice`).
- **Experienced behavior** — what actually happens. Include exact error messages, unexpected output, or observable state. Be specific; avoid "it doesn't work."
- **Expected behavior** — what should happen instead, and why that is the correct outcome.

## Optional Fields

Include these when known. Explicitly record "unknown" or "not yet available" rather than silently omitting them — a noted gap is more useful than a blank.

- **What is not working** — a one-line summary of the broken behavior, distinct from the detailed experienced/expected descriptions (useful as a title or triage label).
- **Available evidence** — logs, stack traces, metrics, screenshots, or other diagnostic artifacts. State where they can be found if not included inline.
- **Reproduction steps** — the minimal sequence to trigger the defect. If not known yet, write "reproduction steps unknown."
- **Severity or impact** — how badly this affects users or operations (e.g., blocks critical workflow, cosmetic only, intermittent data loss). Useful for triage priority.

## Procedure

### 1. Assign an ID

Read `docs/pending/next` to obtain the next available ID `N`. Write `N + 1` back to `docs/pending/next` before creating any files. If `docs/pending/next` does not exist, find the highest-numbered existing folder in `docs/pending/` and add one; write that value plus one back to `docs/pending/next`.

### 2. Create the Work Item Folder

Create `docs/pending/<N>-<short-name>/` where `<short-name>` is a brief kebab-case label for the defect (e.g., `lmstudio-timeout-on-cancel`).

### 3. Write `workitem.md`

Create `docs/pending/<N>-<short-name>/workitem.md` using the structure below. Fill in all required fields. For optional fields, include them if known; write "unknown" or "not yet available" rather than omitting the heading.

```
---
title: <short description of the defect>
status: pending
project: <project slug>
---

# Work Item: <short description of the defect>

## Description

<Product>: <what is not working — one sentence>.

Experienced behavior: <what actually happens, including error text or observable state>.

Expected behavior: <what should happen and why>.

## Evidence

<Paste logs, stack traces, or screenshots inline, or state where they can be found.
If not yet available, write: "Not yet available — will be captured at <location>.">

## Reproduction Steps

<Numbered list of the minimal steps to trigger the defect.
If unknown, write: "Reproduction steps unknown.">

## Severity

<Impact statement, e.g.: "Blocks copilot completions entirely for gtr host." or "Cosmetic — incorrect label in UI.">

## Acceptance Criteria

- The experienced behavior no longer occurs.
- The expected behavior is confirmed by manual verification or automated test.
- No regression in related functionality.
```

### 4. Capture Quickly

A work item written now is more valuable than a perfect one never written. Fill in what you know; mark gaps explicitly. Additional context can be added before or during planning.

## Output

A folder at `docs/pending/<N>-<short-name>/` containing `workitem.md`. This folder is the home for all future artifacts (plan, implementation log, review) as the work item progresses through the pipeline.
