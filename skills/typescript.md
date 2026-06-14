---
name: typescript
description: TypeScript conventions for all project types — hub document; see profiles for build-environment specifics
---
# TypeScript Language Guidelines

## Purpose
These guidelines ensure consistent, correct TypeScript code across all project types that use TypeScript. This document covers universally-true rules. Build environment, tooling, and project-type-specific conventions are defined in the profile documents listed in the **Profile Selection** section below.

## Core Principles
- Follow standard TypeScript idioms.
- Prefer simplicity, explicit types, and strict mode.
- Only constrain what is necessary for correctness or project consistency.
- Explicitly grant freedom on non-critical choices.

## Build Environment

**TypeScript projects use the Docker-based build environment defined in `skills/docker.md`.** Node.js, npm, and all related tooling run inside Docker containers — never on the host.

Key rules (see `skills/docker.md` for full details):
- Never run `npm install`, `npm run`, `npx`, `node`, or any Node.js tooling directly on the host.
- All build commands go through `make` targets that wrap Docker invocations.
- `node_modules/` is written to the host via volume mount so that editor tooling (IntelliSense, language servers) can use it.
- `Dockerfile.dev` defines the build image; `Makefile` defines the targets.

## Module & Project Setup

- **`package.json`** — the single source of truth for project metadata, dependencies, and scripts.
- **`tsconfig.json`** — use strict mode (`"strict": true`). One `tsconfig.json` at project root. Source in `src/`. Target version and output directory are profile-specific — see the applicable profile.
- Do not create nested tsconfigs unless the project has genuinely separate compilation targets.
- **Lock file** — `package-lock.json` is committed to the repo. Generated inside Docker via `make install`.

## Tooling & Build Behavior

- Run the profile's verification command (e.g., `make compile`) after every set of changes to verify correctness before moving on. Do not batch all implementation and verify once at the end.
- **Verification after Edits:** Always run the profile's build/verify step after any non-trivial automated file operation. This ensures that syntax errors introduced by automated edits are caught immediately before further implementation or testing.
- If a bundler (esbuild, webpack, vite) is needed, add it to `Dockerfile.dev` and wrap it in a Makefile target. Do not install it on the host.

## Testing Guidelines

- **Standard Tooling:** Projects should use established frameworks (e.g., `jest`, `mocha`, `vitest`). All test runs must be wrapped in a `make test` target.
- **String Manipulation Logic:** When testing code that involves truncation, splitting, or buffering of large strings:
    - **Structural Markers:** Ensure test data contains necessary structural markers (like newlines `\n` or delimiters) at expected intervals. Logic can fail silently or yield "zero-result" cases if the test string is a single monolithic block but the logic expects multi-line input.
    - **Marker Density:** Verify that the "density" of markers in test strings is sufficient to exercise boundary conditions (e.g., a newline exactly at the truncation limit).
    - **Helpers:** Use helper functions to generate structured test content (e.g., `"line\n".repeat(100)`) rather than hardcoding large strings.

## Coding Conventions (Defaults)

- **Strict mode always.** `"strict": true` in `tsconfig.json`.
- **Explicit return types** on exported functions. Inferred types are fine for internal/private functions.
- **No `any`** unless genuinely unavoidable and documented with a comment explaining why.
- **Prefer `const`** over `let`. Never use `var`.
- **Error handling:** Catch specific errors where possible. Do not silently swallow errors — log them or re-throw.
- **Imports:** Use named imports. Avoid `import *` unless the profile or project convention requires it.

## Security & Safety Invariants

- Never log secrets, tokens, passwords, or API keys at any log level.
- Validate all user-provided configuration paths before using them (check existence, handle missing gracefully).
- Use atomic writes (write to temp file, rename) when writing to user-owned files to avoid corruption on crash.

## Explicit AI Freedom

The AI has full discretion over:
- Internal variable/function naming (except user-visible strings)
- Exact file organization and module splitting within `src/`
- Choice of helper patterns (classes vs. functions, etc.)
- Whether to use `interface` or `type` for object shapes
- Test framework choice and test structure (within the profile's recommendation)
- Exact formatting (the project may adopt a formatter later)
- Minor refactoring for readability or performance unless constrained by the feature plan

## Profile Selection

Select the profile that matches your project type and read it alongside this hub document. Both documents together define the complete set of conventions for that project type.

| Profile | When to use |
|---|---|
| [VS Code Extension](typescript/vscode-extension.md) | Projects that produce a `.vsix` extension package published to the VS Code Marketplace |
| [SPA / Game / Web](typescript/spa.md) | Projects that produce a browser-hosted application — SPAs, browser games, Vite-based apps |

If a future project type does not fit either profile, add a new profile rather than stretching an existing one.

## Usage
Reference this file in feature plans when TypeScript is the target language. Always include the applicable profile in the reference.
Follow these rules automatically unless a feature plan explicitly overrides them.
