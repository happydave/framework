# Project Planning Framework

## Purpose
Structured approach for deep human-AI collaboration on software projects.  
Human remains deeply involved throughout planning.  

Note: This document describes how to build specifications for an AI agent, not a finished product other than those specifications.

## Intent
Produce planning and feature specifications with enough clear, precise, descriptive detail that an AI can implement the product correctly on the first attempt with minimal guesswork and no risk of incorrect features or behavior.

## Spec Style Guide
- Plaintext Markdown only
- Concise, objective, precise language
- No code (structs, functions, declarations) appears in any planning specification
- Headings for structure (# Phase, ## Step)
- Bullets for lists; numbered for sequences
- Strong descriptive text of expected behavior, data flows, edge cases, invariants — enough to eliminate ambiguity for implementation
- Invariant section must contain: each invariant provably true given fundamental constraints, no unstated assumptions or dependencies, no implicit contradictions
- This framework assumes invariants will be scrutinized for these qualities during the Critically Assess step

## Document Storage & Naming
- All planning specifications live in the `specs/` folder at the root of the project
- `00_Project.spec` — top-level project plan / overall specification
- `01_Authentication.spec`, `02_User-Profile.spec`, etc. — phase- or feature-specific specifications
- Sequential numbering from 00; descriptive kebab-case names after number

## Completion Statuses
- **Pending** — not started or incomplete
- **Complete** — finished, reviewed, approved by human
- Update status only on completion (no "In Progress")

## Feature Specification Template
When a feature requires precise, unambiguous descriptive requirements for implementation, copy and adapt the template from:
`template/Feature.spec`

The template includes these required sections (all must be completed when relevant to the feature):
- **Objective** — One-sentence goal description
- **Invariants** — Non-negotiable truths about system behavior or constraints (with optional rationale)
- **Functional Requirements** — SHALL statements with trigger → behavior → outcome structure, organized by:
  - User-Visible Behaviors
  - Data Requirements
  - Security & Privacy (if applicable)
- **Acceptance Scenarios** — Gherkin-style scenarios describing what constitutes sufficient completeness for human approval
- **Edge Cases & Error Handling** — Required documentation of significant exception conditions and expected responses
- **Non-Functional Requirements** — Performance, scalability, reliability, and compatibility constraints
- **Data Model & State Changes** — Description of affected data entities and state transitions (no implementation details)
- **Known Constraints & Assumptions** — Explicit documentation of limiting conditions and verified assumptions
- **Validation Approach** — Descriptive methods for verifying correctness without code
- **Completion Checklist** — Self-check before marking Complete

Use all sections as needed; every section that applies to the feature must be completed.

## General Guidelines

### Language-Specific Guidelines
- When this framework is used with a specific programming language, guidelines from `language/[language].spec` apply when present.

### Cross-Feature Relationships
- Cross-feature dependencies and ordering principles are introduced when they become ambiguity sources; these may be deferred if not genuinely necessary for understanding individual features

## Project Workflow

### Phase 0: Research & Planning
**Product**: Project planning spec `specs/00_Project.spec`

**Scope**: Establish high-level goals, key features, non-functional requirements, invariants, feasibility assessment, and phase breakdown. Produce precise descriptive requirements only. No implementation details or code.

**Process**:

1. **Assess** — review problem domain, stakeholder needs, known constraints
2. **Research & Elaborate** — investigate technical feasibility, resource needs, risks, non-functional requirements; draft high-level invariants and goals. This step is intended as deep scrutiny to ensure each feature spec has sufficient detail to implement confidently and correctly.
3. **Create Spec** — define project goals, key features, backlog, phase boundaries, and scope exclusions using descriptive language
4. **Test (Descriptive)** — describe validation approaches for feasibility and scope (e.g., thought experiments, constraint checks)
5. **Critically Assess** — check for gaps, contradictions, over- or under-scoping
   - Invariants are provably true, contain no unstated assumptions, and don't implicitly contradict other invariants

- Repeat steps 1–5 as needed until the Critical Assess step confirms the spec is unambiguous and complete.
- This process is conducted closely with a human; if scrutiny reveals intractable ambiguity, the human should determine whether to revise scope, simplify specs, or defer the feature.
- Limit to a maximum of 3 total cycles (initial + up to 2 repeats).

**After refinement complete (00_Project.spec ready):**
- Record any major decisions or adjustments in the relevant spec(s)
- Mark as **Complete**
- Use this specification as the baseline for all Phase 1+ feature refinement

**Phase Mini-Retrospective**  
List significant problems, research gaps, unnecessary resource usage, extra iterations, unplanned human interventions, or items warranting framework changes.

**Status**: [Pending/Complete]

### Phase 1+: Feature Refinement

**Product**: Feature specification (specs/xx_Feature.spec)

**Scope**: Deepen and finalize detailed descriptive specifications for each feature identified in `00_Project.spec`. Preserve high-level scope and boundaries; add precision through research, invariants, edge cases, and scenarios only. No implementation or code.

**Process**:

1. **Assess** — review high-level scope from 00_Project.spec, current knowledge gaps, constraints
2. **Research & Elaborate** — investigate domain details, data flows, security/privacy needs, performance invariants; draft/refine descriptive outcomes (no code)
3. **Create Spec**
  - Complete all relevant sections from the Feature-Spec-Template:
    - Objective (one-sentence goal)
    - Invariants (non-negotiable truths with optional rationale)
    - Functional Requirements (SHALL statements organized by user-visible behaviors, data requirements, security/privacy)
    - Acceptance Scenarios (Gherkin-style scenarios for human approval criteria)
    - Edge Cases & Error Handling (significant exception conditions and expected responses)
    - Non-Functional Requirements (performance, scalability, reliability, compatibility constraints)
    - Data Model & State Changes (affected entities and transitions without implementation details)
    - Known Constraints & Assumptions (limiting conditions and verified assumptions)
    - Validation Approach (descriptive methods for verifying correctness without code)
  - Acceptance scenarios should focus primarily on what constitutes sufficient completeness for human acceptance of the current spec state, rather than an exhaustive catalog of test cases.
4. **Test (Descriptive)** — define verification approaches: describe test cases, expected behaviors, failure modes (still no code/tests written)
5. **Critically Assess** — check for ambiguity, completeness, contradictions

- Repeat steps 1–5 as needed until the Critical Assess step confirms the spec is unambiguous and complete.
- This process is conducted closely with a human; if scrutiny reveals intractable ambiguity, the human should determine whether to revise scope, simplify specs, or defer the feature.
- Limit to a maximum of 3 total cycles (initial + up to 2 repeats).

**After refinement complete (feature spec ready):**
- Record any major decisions or adjustments in the relevant spec(s)
- Mark as **Complete**
- Optionally update `00_Project.spec` with cross-feature insights or scope adjustments
- Proceed to implementation in a separate session/tool (outside this planning framework)

**Phase Mini-Retrospective**  
List significant problems, research gaps, extra iterations, unplanned human interventions, or items warranting framework changes.

**Status**: [Pending/Complete] per feature specification

### Final Phase: Retrospective

**Product**: Retrospective document (`specs/99_Retrospective.spec`)

**Scope**: Holistic review of process, collaboration, output quality, and framework effectiveness

**Steps**:
1. What worked well (framework, human-AI collaboration, output precision)
2. What did not work well (pain points, ambiguity sources, bottlenecks)
3. Critical assessment of process and this framework
4. Concrete improvements for next project/framework version

**Status**: [Pending/Complete]

## Unplanned / Out-of-Scope Work
List explicitly in `specs/00_Project.spec` (and phase/feature specs if relevant):
- Features/capabilities deliberately excluded
- Work outside current scope
- Desired features deferred to future projects

## Notes
- Human deeply involved in planning and review
- Planning specifications must be unambiguous and detailed enough for correct first-pass implementation by AI
- Refine framework iteratively via phase mini-retrospectives and final retrospective
