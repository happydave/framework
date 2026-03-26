# Plan

## Purpose

Structured approach for deep human-AI collaboration on software projects.

Human remains deeply involved throughout planning.

Note: This document describes how to create feature plans for an AI agent, not a finished product other than those plans.

## Intent

Produce feature plans with enough clear, precise, descriptive detail that an AI can implement the feature correctly on the first attempt with minimal guesswork and maximum freedom for optimal implementation choices.

## Style Guide

- Plaintext Markdown only
- Concise, objective, precise language
- No code (structs, functions, declarations) appears in any planning document
- Headings for structure (# Phase, ## Step)
- Bullets for lists; numbered for sequences
- Strong descriptive text of expected behavior, data flows, edge cases, invariants — enough to eliminate ambiguity for implementation
- Invariant section must contain: each invariant provably true given fundamental constraints, no unstated assumptions or dependencies, no implicit contradictions
- Explicitly grant AI freedom in non-critical decisions (see templates/feature.md)
- This framework assumes invariants will be scrutinized for these qualities during the Critically Assess step

## Document Storage & Naming

Feature plans live inside the ticket folder that originated them. When a ticket is promoted to a plan, create `plan.md` in the ticket's folder:

- `docs/pending/07-investigate-pipeline-jobs/plan.md`
- `docs/pending/PROJ-123-investigate-pipeline-jobs/plan.md`

The presence of `plan.md` in a ticket folder indicates the ticket has been planned. The absence of `plan.md` indicates it has not.

## Feature Plan Instructions

For each feature, create `plan.md` in the ticket's folder following the guidance in `templates/feature.md`.

That file provides:
- Core principles (outcome focus, minimal constraints, explicit AI freedom)
- Required sections (Objective, Invariants & Hard Constraints, Required Behaviors & Verifications, etc.)
- Emphasis on unambiguous yet non-prescriptive detail sufficient for correct first-pass AI implementation

## General Guidelines

### Language-Specific Guidelines

- When this framework is used with a specific programming language, guidelines from guidelines/[language].md apply when present.
- For Go projects: follow guidelines/Go.md (module setup, tooling, conventions, invariants).

### Cross-Feature Relationships

- Cross-feature dependencies and ordering principles are introduced when they become ambiguity sources; these may be deferred if not genuinely necessary for understanding individual features

## Planning Workflow

**Product**: Feature plan (`plan.md` in the ticket's folder)

**Scope**: Produce a detailed descriptive document for a feature or work item. Define precise outcomes through research, invariants, edge cases, and scenarios. No implementation or code.

### Planning Aspects

These are not sequential phases — they are aspects of planning that apply throughout the process, revisited as understanding deepens.

**Assess** — review the ticket, problem domain, stakeholder needs, known constraints, and current knowledge gaps. Assessment happens at the start and again whenever new information changes the picture.

**Research & Elaborate** — investigate technical feasibility, domain details, data flows, security/privacy needs, resource needs, risks, and non-functional requirements. Draft high-level invariants and goals. Refine descriptive outcomes (no code). This is intended as deep scrutiny to ensure the feature plan has sufficient detail to implement confidently and correctly.

**Test (Descriptive)** — describe validation approaches: expected behaviors, failure modes, edge case scenarios, and thought experiments that confirm the plan is sound. No code or tests written — this is descriptive verification of the plan itself.

**Critically Assess** — check for gaps, ambiguity, contradictions, over- or under-scoping.
- Invariants are provably true, contain no unstated assumptions, and don't implicitly contradict other invariants
- Behaviors and verifications are sufficient to confirm correctness without guesswork

**Refine** — after any significant decisions, discoveries, or plan changes, apply another round of assessment and critical assessment to ensure the whole plan remains cohesive and consistent. Planning is not a single pass — it converges through iteration.

### Writing the Plan

Follow the Required Content & Guidance in `templates/feature.md`. Complete only sections genuinely needed for unambiguous implementation. Acceptance scenarios should focus on what constitutes sufficient completeness for human acceptance, rather than an exhaustive catalog of test cases.

This process is conducted closely with a human. If scrutiny reveals intractable ambiguity, the human should determine whether to revise scope, simplify descriptions, or defer the feature.

**After refinement complete (feature plan ready):**
- Record any major decisions or adjustments in the plan
- Proceed to implementation via the Implement action

**Planning Mini-Retrospective**  
A brief, lightweight note on the planning process itself — not a full reflection (that happens after implementation via the Reflect action). List significant problems, research gaps, extra iterations, unplanned human interventions, or items warranting framework changes. A few bullet points is sufficient.

## Unplanned / Out-of-Scope Work

List explicitly in feature plans if relevant:
- Features/capabilities deliberately excluded
- Work outside current scope
- Desired features deferred to future tickets

## Notes
- Human deeply involved in planning and review
- Planning documents must be unambiguous and detailed enough for correct first-pass implementation by AI
- Use `templates/feature.md` as the canonical guide for feature plans to keep them lean and outcome-oriented
- Refine framework iteratively via phase mini-retrospectives