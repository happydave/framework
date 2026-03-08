# Project Planning Framework

## Purpose

Structured approach for deep human-AI collaboration on software projects.

Human remains deeply involved throughout planning.

Note: This document describes how to build project plans and feature descriptions for an AI agent, not a finished product other than those plans and descriptions.

## Intent

Produce project plans and feature descriptions with enough clear, precise, descriptive detail that an AI can implement the product correctly on the first attempt with minimal guesswork and maximum freedom for optimal implementation choices.

## Style Guide

- Plaintext Markdown only
- Concise, objective, precise language
- No code (structs, functions, declarations) appears in any planning document
- Headings for structure (# Phase, ## Step)
- Bullets for lists; numbered for sequences
- Strong descriptive text of expected behavior, data flows, edge cases, invariants — enough to eliminate ambiguity for implementation
- Invariant section must contain: each invariant provably true given fundamental constraints, no unstated assumptions or dependencies, no implicit contradictions
- Explicitly grant AI freedom in non-critical decisions (see work/Feature.md)
- This framework assumes invariants will be scrutinized for these qualities during the Critically Assess step

## Document Storage & Naming

- All planning documents live in the work/ folder at the root of the project
- work/00_Project.md — top-level project plan / overall description
- work/01_authentication.md, work/02_user-profile.md, etc. — feature-specific descriptions
- Sequential numbering from 00; descriptive kebab-case names after number

## Completion Statuses

- **Pending** — not started or incomplete
- **Complete** — finished, reviewed, approved by human
- Update status only on completion (no "In Progress")

## Feature Description Instructions

For each feature, create a document in `work/` (e.g., `work/01_authentication.md`) following the guidance in `work/Feature.md`.

That file provides:
- Core principles (outcome focus, minimal constraints, explicit AI freedom)
- Required sections (Objective, Invariants & Hard Constraints, Required Behaviors & Verifications, etc.)
- Emphasis on unambiguous yet non-prescriptive detail sufficient for correct first-pass AI implementation

## General Guidelines

### Language-Specific Guidelines

- When this framework is used with a specific programming language, guidelines from language/[language].md apply when present.
- For Go projects: follow language/Go.md (module setup, tooling, conventions, invariants).

### Cross-Feature Relationships

- Cross-feature dependencies and ordering principles are introduced when they become ambiguity sources; these may be deferred if not genuinely necessary for understanding individual features

## Project Workflow

### Phase 0: Research & Planning

**Product**: Project planning document `work/00_Project.md`

**Scope**: Establish high-level goals, key features, non-functional requirements, invariants, feasibility assessment, and phase breakdown. Produce precise descriptive requirements only. No implementation details or code.

**Process**:

1. **Assess** — review problem domain, stakeholder needs, known constraints
2. **Research & Elaborate** — investigate technical feasibility, resource needs, risks, non-functional requirements; draft high-level invariants and goals. This step is intended as deep scrutiny to ensure each feature description has sufficient detail to implement confidently and correctly.
3. **Draft Plan** — define project goals, key features, backlog, phase boundaries, and scope exclusions using descriptive language
4. **Test (Descriptive)** — describe validation approaches for feasibility and scope (e.g., thought experiments, constraint checks)
5. **Critically Assess** — check for gaps, contradictions, over- or under-scoping
   - Invariants are provably true, contain no unstated assumptions, and don't implicitly contradict other invariants

- Repeat steps 1–5 as needed until the Critical Assess step confirms the document is unambiguous and complete.
- This process is conducted closely with a human; if scrutiny reveals intractable ambiguity, the human should determine whether to revise scope, simplify descriptions, or defer the feature.

**After refinement complete (work/00_Project.md ready):**
- Record any major decisions or adjustments in the relevant document(s)
- Mark as **Complete**
- Use this document as the baseline for all Phase 1+ feature refinement

**Phase Mini-Retrospective**  
List significant problems, research gaps, unnecessary resource usage, extra iterations, unplanned human interventions, or items warranting framework changes.

**Status**: [Pending/Complete]

### Phase 1+: Feature Refinement

**Product**: Feature description (work/xx_feature.md)

**Scope**: Deepen and finalize detailed descriptive documents for each feature identified in `work/00_Project.md`. Preserve high-level scope and boundaries; add precision through research, invariants, edge cases, and scenarios only where ambiguity exists. No implementation or code.

**Process**:

1. **Assess** — review high-level scope from `work/00_Project.md`, current knowledge gaps, constraints
2. **Research & Elaborate** — investigate domain details, data flows, security/privacy needs, performance invariants; draft/refine descriptive outcomes (no code)
3. **Draft Plan**
   - Follow the Required Content & Guidance in `work/Feature.md`. Complete only sections genuinely needed for unambiguous implementation.
   - Acceptance scenarios should focus primarily on what constitutes sufficient completeness for human acceptance of the current document state, rather than an exhaustive catalog of test cases.
4. **Test (Descriptive)** — define verification approaches: describe test cases, expected behaviors, failure modes (still no code/tests written)
5. **Critically Assess** — check for ambiguity, completeness, contradictions

- Repeat steps 1–5 as needed until the Critical Assess step confirms the document is unambiguous and complete.
- This process is conducted closely with a human; if scrutiny reveals intractable ambiguity, the human should determine whether to revise scope, simplify descriptions, or defer the feature.

**After refinement complete (feature document ready):**
- Record any major decisions or adjustments in the relevant document(s)
- Mark as **Complete**
- Optionally update `work/00_Project.md` with cross-feature insights or scope adjustments
- Proceed to implementation in a separate session/tool (outside this planning framework)

**Phase Mini-Retrospective**  
List significant problems, research gaps, extra iterations, unplanned human interventions, or items warranting framework changes.

**Status**: [Pending/Complete] per feature document

### Final Phase: Retrospective

**Product**: Retrospective document (`work/99_Retrospective.md`)

**Scope**: Holistic review of process, collaboration, output quality, and framework effectiveness

**Steps**:
1. What worked well (framework, human-AI collaboration, output precision)
2. What did not work well (pain points, ambiguity sources, bottlenecks)
3. Critical assessment of process and this framework
4. Concrete improvements for next project/framework version

**Status**: [Pending/Complete]

## Unplanned / Out-of-Scope Work

List explicitly in `work/00_Project.md` (and feature documents if relevant):
- Features/capabilities deliberately excluded
- Work outside current scope
- Desired features deferred to future projects

## Notes
- Human deeply involved in planning and review
- Planning documents must be unambiguous and detailed enough for correct first-pass implementation by AI
- Use `work/Feature.md` as the canonical guide for feature documents to keep them lean and outcome-oriented
- Refine framework iteratively via phase mini-retrospectives and final retrospective