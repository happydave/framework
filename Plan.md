# Project Planning Framework

## Purpose
Structured approach for deep human-AI collaboration on software projects.  
Human remains deeply involved throughout planning.  

## Intent
Produce planning and feature specifications with enough clear, precise, descriptive detail that an AI can implement the product correctly on the first attempt with minimal guesswork and no risk of incorrect features or behavior.

## Spec Style Guide
- Plaintext Markdown only
- Concise, objective, precise language
- No code (structs, functions, declarations) appears in any planning specification
- Headings for structure (# Phase, ## Step)
- Bullets for lists; numbered for sequences
- Strong descriptive text of expected behavior, data flows, edge cases, invariants — enough to eliminate ambiguity for implementation

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

Use only the sections needed; skip others when not relevant.

## General Guidelines

### Go Tooling
- Ask the human explicitly: "What should the Go module path be? ( e.g., example.com/rimworld-mod-manager )"
- Record the confirmed module path in this specification (add a line under "Programming Language(s)": "Go module path: [path]")
- Before running `go mod init`:
  - Check if a go.mod file already exists in the project root. If yes, do not run `go mod init` again; use the existing module.
  - If no go.mod exists, run `go mod init [confirmed-path]`
- Never create nested Go modules (only one go.mod at project root).
- Do not validate the module name format beyond basic sanity (human is responsible for correctness).
- All Go commands (go mod init, go build, go test, etc.) must be run with the current working directory set to the project root folder (where go.mod lives / will live).
- Before any Go tooling: verify the current directory is the individual project folder (e.g. rimworld-mod-manager/), not the parent projects/ workspace.
- When using VS Code multi-root workspace opened at projects/, ensure terminal or tasks are configured to cd into the specific project folder before running Go commands.

## Project Workflow

### Phase 0: Research & Planning
**Product**: Project planning spec `specs/00_Project.spec`

**Scope**: Establish high-level goals, key features, non-functional requirements, invariants, feasibility assessment, and phase breakdown. Produce precise descriptive requirements only. No implementation details or code.

**Process**:

1. **Assess** — review problem domain, stakeholder needs, known constraints
2. **Research & Elaborate** — investigate technical feasibility, resource needs, risks, non-functional requirements; draft high-level invariants and goals
3. **Create Spec** — define project goals, key features, backlog, phase boundaries, and scope exclusions using descriptive language
4. **Test (Descriptive)** — describe validation approaches for feasibility and scope (e.g., thought experiments, constraint checks)
5. **Critically Assess** — check for gaps, contradictions, over- or under-scoping

- Repeat steps 1–5 as needed until the Critical Assess step confirms the spec is unambiguous and complete.
- Limit to a maximum of 3 total cycles (initial + up to 2 repeats).
- If still not ready after 3 cycles, stop and consult human.

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
3. **Create Spec** — write or update Functional Requirements (SHALL statements), Invariants, Edge Cases, and Acceptance Scenarios using the Feature-Spec-Template
4. **Test (Descriptive)** — define verification approaches: describe test cases, expected behaviors, failure modes (still no code/tests written)
5. **Critically Assess** — check for ambiguity, completeness, contradictions

- Repeat steps 1–5 as needed until the Critical Assess step confirms the spec is unambiguous and complete.
- Limit to a maximum of 3 total cycles (initial + up to 2 repeats).
- If still not ready after 3 cycles, stop and consult human.

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