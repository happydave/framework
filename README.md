# Project Planning Framework

## Purpose

This framework provides a structured approach for documenting project plans and feature specifications with precise, unambiguous language that enables correct implementation on first attempt.

The goal is to produce specifications so detailed and clear that an AI (or another human) can implement features correctly without guesswork or misalignment.

## Document Structure

This framework includes templates and guidelines for creating specification documents:

- **This README** — Overview of the entire system
- `Plan.md` — Complete workflow instructions and methodology
- `template/Feature.spec` — Template for feature-level specifications
- `Build.md` — Tooling guidelines (currently empty)

## Using This Framework

### For Project Documentation

When documenting an actual project's plans:

1. **Start with project-level specs**
   - Write `00_Project.spec` with overall goals, invariants, features, and phases
   - Use plain Markdown with precise, objective language
   - Include invariants, functional requirements (SHALL statements), acceptance scenarios, edge cases

2. **Create feature specifications**
   - Copy `template/Feature.spec`
   - Fill objectives, invariants, requirements, scenarios for each feature
   - Avoid code; describe behavior completely

3. **Follow the workflow**
   - Research and elaborate → create spec → test descriptively → critically assess
   - Maximum 3 refinement cycles before marking complete

## Specification Style

### Language & Tone

- Plain Markdown only
- Concise, objective, strictly descriptive
- Minimal rhetorical flourish
- No code blocks unless explaining specification format

## Expected Output Quality

A healthy project specification satisfies:
- Every requirement has clear trigger conditions and outcomes
- Invariants eliminate ambiguity on fundamental constraints
- Acceptance scenarios provide concrete validation points
- Edge cases document behavior across all exceptions
- No dependencies on unstated assumptions or context
- Human and AI remain collaboratively involved throughout refinement

## Current State

This framework is incomplete:
- `Build.md` empty (tooling documentation)
- No example specifications demonstrating full workflow
- No retrospective documenting lessons learned

The framework can be used ad hoc, but its full value requires committed application with iteration.

## License

This project is released into the public domain under the [Unlicense](https://unlicense.org/).  
You are free to use, modify, distribute, and do whatever you want with it — no restrictions, no attribution required.
