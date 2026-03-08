# Project Planning Framework

## Purpose

This framework provides a structured approach for documenting project plans and feature descriptions with precise, unambiguous language that enables correct implementation on first attempt.

The goal is to produce plans and descriptions so detailed and clear that an AI (or another human) can implement features correctly without guesswork or misalignment, while leaving non-critical decisions open for optimal choices.

## About

Important: This repository contains meta-instructions. It is a guide for creating project plans and feature descriptions, not a finished software product. We are currently refining this framework to ensure AI agents can understand and implement features correctly from the outset. Think of it like building the instruction manual before assembling the machine. At this stage, we are concerned with defining a consistent, unambiguous process — not specific feature requirements yet.

## Document Structure

This framework includes guidelines and core documents for creating plans and descriptions:

- **This README** — Overview of the entire system
- `Plan.md` — Complete workflow instructions and methodology
- `work/Feature.md` — Instructions for writing lean, outcome-oriented feature plans and descriptions
- `language/Go.md` — Go-specific guidelines (module setup, tooling, conventions)
- `work/00_Project.md` — (created per project) top-level project plan
- `work/01_authentication.md`, etc. — (created per feature) feature descriptions
- `Build.md` — Tooling guidelines (currently empty)

## Using This Framework

### For Project Documentation

When documenting an actual project's plans:

1. **Start with the project-level plan**  
   Create `work/00_Project.md` with overall goals, key features, invariants, non-functional constraints, and phase breakdown.  
   Use plain Markdown with precise, objective language.

2. **Create feature descriptions**  
   For each feature, create a file in `work/` (e.g., `work/01_authentication.md`).  
   Follow the guidance in `work/Feature.md` to include only what is necessary: objective, invariants, behaviors & verifications, edge cases, explicit AI freedom, etc.  
   Avoid code; describe outcomes and constraints clearly while granting freedom on non-critical decisions.

3. **Follow the workflow**  
   Research & elaborate → draft plan → test descriptively → critically assess.  
   Refine until the Critical Assess step confirms the document is unambiguous and complete.

## Plan Style

### Language & Tone

- Plain Markdown only
- Concise, objective, strictly descriptive
- Minimal rhetorical flourish
- No code blocks unless explaining plan format
- Explicitly grant AI freedom in non-critical areas (see `work/Feature.md`)

## Expected Output Quality

A healthy project plan or feature description satisfies:

- Clear objective and non-negotiable invariants
- Behaviors and verifications sufficient to confirm correctness without guesswork
- Edge cases and error responses covered where significant
- No unstated assumptions or contradictions
- Critical decisions stated; non-critical ones left open
- Human and AI remain collaboratively involved throughout refinement

## Current State

This framework is evolving:

- `Build.md` empty (tooling documentation)
- `work/Feature.md` newly added as the single source of truth for feature plans and descriptions
- No full example projects yet demonstrating the workflow end-to-end
- No retrospective documenting lessons learned

The framework can be used ad hoc, but its full value requires committed application with iteration.

## License

This project is released into the public domain under the [Unlicense](https://unlicense.org/).  
You are free to use, modify, distribute, and do whatever you want with it — no restrictions, no attribution required.