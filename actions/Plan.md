# Plan

## Purpose

Structured approach for deep human-AI collaboration on software projects. Human remains deeply involved throughout planning.

This document describes how to create feature plans for an AI agent, not a finished product other than those plans.

## Intent

Produce feature plans with enough clear, precise, descriptive detail that an AI can implement the feature correctly on the first attempt with minimal guesswork and maximum freedom for optimal implementation choices.

## Plan Structure

Every plan must include the sections below. Complete only what is genuinely necessary for unambiguous implementation; omit or mark optional sections that do not apply.

**Objective**
One clear sentence that captures the single desired purpose of the feature.
Example: Enable users to securely register, verify their email, and log in so they can access protected resources.

**Invariants & Hard Constraints**
Bullet list of non-negotiable truths that must always hold. Keep this list short and provable. Include only items that, if violated, break correctness, security, or compliance.
Examples:
- Passwords are never stored in plain text or reversible form.
- All authentication tokens expire and cannot be used after revocation.
- Personally identifiable data is encrypted at rest using AES-256 or stronger.
(For project-wide security rules — e.g., OWASP Top 10 mitigation, no plain-text secrets in logs — reference a central security.md or include critical ones here.)

**Required Behaviors & Verifications**
Concise descriptions of required behavior and verifiable success criteria. Organize by major concern (user-visible actions, data flows, security/privacy, etc.). Use SHALL statements for must-have outcomes and include focused scenarios (Gherkin-style or numbered steps) that define "done." Cover at least: one happy path, one key failure mode, one security-relevant case.
Example:
- SHALL allow new users to register with a valid email and strong password, then send a time-limited verification link.
- SHALL reject registration attempts with duplicate emails (return 409 Conflict).
Given valid email and strong password
When user submits registration
Then verification email is sent and account is created in unverified state
AI has freedom over: route patterns, validation libraries, exact HTTP status wording (unless security-critical), internal error handling structure, and non-functional optimizations unless listed below.

**Edge Cases & Required Error Responses**
Bullet list of significant exceptions and exactly how the system must respond (status code, user message intent, retryability, etc.).

**Non-Functional Constraints** (only when critical to the project)
List only project-wide or feature-specific requirements that affect correctness or viability.

**Data & State Changes** (when the feature affects persistent state)
Simple description of new/updated entities and allowed transitions — no schema syntax or implementation detail.

**Explicit AI Freedom**
Mandatory closing section that lists what is intentionally **not** constrained. Tailor this list to reflect the actual project tech stack (e.g., specify allowed frameworks).
Example:
The AI has full discretion over:
- Choice of libraries and patterns within the approved tech stack
- File and directory organization
- Naming conventions (except where names are user-visible or constrained)
- Internal code structure and optimizations
- Exact phrasing of non-security-critical user messages

**Dependencies & Context**
Reference related documents or prior features only when order or shared invariants matter.

## Style Guide

- Plaintext Markdown only
- Concise, objective, precise language
- No code (structs, functions, declarations) appears in any planning document
- Headings for structure (# Phase, ## Step)
- Bullets for lists; numbered for sequences
- Strong descriptive text of expected behavior, data flows, edge cases, invariants — enough to eliminate ambiguity for implementation
- Invariant section must contain: each invariant provably true given fundamental constraints, no unstated assumptions or dependencies, no implicit contradictions
- This framework assumes invariants will be scrutinized during the Critically Assess step

## Document Storage & Naming

Feature plans live inside the ticket folder that originated them. When a ticket is promoted to a plan, create `plan.md` in the ticket's folder:

- `docs/pending/07-investigate-pipeline-jobs/plan.md`
- `docs/pending/PROJ-123-investigate-pipeline-jobs/plan.md`

The presence of `plan.md` in a ticket folder indicates the ticket has been planned. The absence of `plan.md` indicates it has not.

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

Complete only sections genuinely needed for unambiguous implementation. Acceptance scenarios should focus on what constitutes sufficient completeness for human acceptance, rather than an exhaustive catalog of test cases.

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
- Refine framework iteratively via phase mini-retrospectives