# TypeScript Language Guidelines

## Purpose
These guidelines ensure consistent, correct TypeScript code when the project uses TypeScript — particularly for VS Code extensions and Node.js tooling. They apply whenever a feature plan targets TypeScript.

## Core Principles
- Follow standard TypeScript idioms and VS Code extension conventions.
- Prefer simplicity, explicit types, and strict mode.
- Only constrain what is necessary for correctness or project consistency.
- Explicitly grant freedom on non-critical choices.

## Build Environment

**TypeScript projects use the Docker-based build environment defined in `guidelines/Docker.md`.** Node.js, npm, and all related tooling run inside Docker containers — never on the host.

Key rules (see `guidelines/Docker.md` for full details):
- Never run `npm install`, `npm run`, `npx`, `node`, or any Node.js tooling directly on the host.
- All build commands go through `make` targets that wrap Docker invocations.
- `node_modules/` is written to the host via volume mount so that editor tooling (IntelliSense, language servers) can use it.
- `Dockerfile.dev` defines the build image; `Makefile` defines the targets.

### Standard Makefile Targets

| Target | Command inside Docker | Description |
|---|---|---|
| `make install` | `npm install` | Install dependencies |
| `make compile` | `npx tsc -p .` | One-shot TypeScript compile |
| `make watch` | `npx tsc -watch -p .` | Continuous rebuild (interactive) |
| `make package` | `npx vsce package --no-dependencies` | Build VSIX (VS Code extensions) |
| `make clean` | *(runs on host)* | `rm -rf node_modules dist out *.vsix` |

### Dockerfile.dev (typical)

```dockerfile
FROM node:lts-alpine
RUN npm install -g @vscode/vsce
WORKDIR /workspace
```

Adapt as needed: add global tools the project requires (e.g., `esbuild`, test runners). Keep the image small.

## Module & Project Setup

- **`package.json`** — the single source of truth for project metadata, dependencies, scripts, and VS Code extension contributions.
- **`tsconfig.json`** — use strict mode (`"strict": true`). Target `ES2022` or later. Output to `dist/`. Source in `src/`.
- **One `tsconfig.json` at project root.** Do not create nested tsconfigs unless the project has genuinely separate compilation targets.
- **Lock file** — `package-lock.json` is committed to the repo. It is generated inside Docker via `make install`.

## Tooling & Build Behavior

- Compile with `tsc` (via `make compile` or `make watch`).
- Use `@types/vscode` and `@types/node` as dev dependencies for VS Code extension projects.
- Run `make compile` after every set of changes to verify correctness before moving on. Do not batch all implementation and compile once at the end.
- If a bundler (esbuild, webpack) is needed, add it to `Dockerfile.dev` and wrap it in a Makefile target. Do not install it on the host.

## Coding Conventions (Defaults)

- **Strict mode always.** `"strict": true` in `tsconfig.json`.
- **Explicit return types** on exported functions. Inferred types are fine for internal/private functions.
- **No `any`** unless genuinely unavoidable and documented with a comment explaining why.
- **Prefer `const`** over `let`. Never use `var`.
- **Error handling:** Catch specific errors where possible. Do not silently swallow errors — log them or re-throw.
- **Imports:** Use named imports. Avoid `import *` except for the `vscode` namespace (`import * as vscode from "vscode"`).
- **No `console.log` / `console.warn` / `console.error`** in VS Code extension source code. Use a `LogOutputChannel` (see Diagnostics section below).

## VS Code Extension Conventions

- **Activation:** Use the narrowest activation events possible (`onCommand:`, `workspaceContains:`, `onLanguage:`). Use `onStartupFinished` only when the extension must be available unconditionally (e.g., chat participants).
- **Disposal:** Register all resources (views, watchers, channels, providers) on `context.subscriptions` in `activate()`. Do not rely on `deactivate()` for cleanup of VS Code-managed resources.
- **Diagnostics:** Use `vscode.window.createOutputChannel(name, { log: true })` to create a `LogOutputChannel`. Initialize it as the first statement in `activate()`. Use `log().info/debug/warn/error/trace()` throughout. Verbosity is controlled by the built-in "Developer: Set Log Level..." command — no custom settings needed.
- **Configuration:** Contribute settings via `contributes.configuration` in `package.json`. Use `vscode.workspace.getConfiguration()` to read them.
- **Commands:** Prefix all command IDs with the extension name (e.g., `cogpress.refreshBuckets`).

## Security & Safety Invariants

- Never log secrets, tokens, passwords, or API keys at any log level.
- Validate all user-provided configuration paths before using them (check existence, handle missing gracefully).
- Use atomic writes (write to temp file, rename) when writing to user-owned files to avoid corruption on crash.

## Dependencies

- Minimize external dependencies. Prefer the Node.js standard library and VS Code API.
- No native binary dependencies (`better-sqlite3`, etc.) — they cause VS Code Marketplace distribution problems. Use pure JS/WASM alternatives (e.g., `sql.js`).
- Dev dependencies (`@types/*`, `typescript`, build tools) are fine in any quantity.

## Explicit AI Freedom

The AI has full discretion over:
- Internal variable/function naming (except user-visible strings)
- Exact file organization and module splitting within `src/`
- Choice of helper patterns (classes vs. functions, etc.)
- Whether to use `interface` or `type` for object shapes
- Test framework choice and test structure
- Exact formatting (the project may adopt a formatter later)
- Minor refactoring for readability or performance unless constrained by the feature plan

## Usage
Reference this file in feature plans when TypeScript is the target language.
Follow these rules automatically unless a feature plan explicitly overrides them.
