---
name: typescript-vscode-extension
description: Build environment and VS Code-specific conventions for TypeScript VS Code extension projects
---
# TypeScript: VS Code Extension Profile

Extends [`skills/typescript.md`](../typescript.md) with VS Code extension-specific build, tooling, and convention rules. Read both documents — this profile does not repeat hub content.

## Standard Makefile Targets

| Target | Command inside Docker | Description |
|---|---|---|
| `make install` | `npm install` | Install dependencies |
| `make compile` | `npx tsc -p .` | One-shot TypeScript compile |
| `make watch` | `npx tsc -watch -p .` | Continuous rebuild (interactive) |
| `make package` | `npx vsce package --no-dependencies` | Build VSIX |
| `make clean` | *(runs on host)* `rm -rf node_modules dist out *.vsix` | Remove build artifacts |

## Dockerfile.dev (typical)

```dockerfile
FROM node:lts-alpine
RUN npm install -g @vscode/vsce
WORKDIR /workspace
```

Adapt as needed: add global tools the project requires (e.g., `esbuild`, test runners). Keep the image small.

## TypeScript Configuration

- `tsconfig.json`: Target `ES2022` or later. Output to `dist/`.
- Use `@types/vscode` and `@types/node` as dev dependencies.
- Compile with `tsc` (via `make compile` or `make watch`).
- Run `make compile` after every set of changes to verify correctness before moving on.

## Dependencies

- Minimize external dependencies. Prefer the Node.js standard library and VS Code API.
- No native binary dependencies (`better-sqlite3`, etc.) — they cause VS Code Marketplace distribution problems. Use pure JS/WASM alternatives (e.g., `sql.js`).
- Dev dependencies (`@types/*`, `typescript`, build tools) are fine in any quantity.

## VS Code Extension Conventions

- **Activation:** Use the narrowest activation events possible (`onCommand:`, `workspaceContains:`, `onLanguage:`). Use `onStartupFinished` only when the extension must be available unconditionally (e.g., chat participants).
- **Disposal:** Register all resources (views, watchers, channels, providers) on `context.subscriptions` in `activate()`. Do not rely on `deactivate()` for cleanup of VS Code-managed resources.
- **Diagnostics:** Use `vscode.window.createOutputChannel(name, { log: true })` to create a `LogOutputChannel`. Initialize it as the first statement in `activate()`. Use `log().info/debug/warn/error/trace()` throughout. Verbosity is controlled by the built-in "Developer: Set Log Level..." command — no custom settings needed.
- **Logging:** Do not use `console.log`, `console.warn`, or `console.error` in VS Code extension source code. Use a `LogOutputChannel`.
- **Imports:** The `vscode` namespace is an exception to the named-import rule: `import * as vscode from "vscode"` is the standard pattern.
- **Configuration:** Contribute settings via `contributes.configuration` in `package.json`. Use `vscode.workspace.getConfiguration()` to read them.
- **Configuration Scoping:** Before declaring a new variable to hold configuration (e.g., `const config = ...`), check the current function or method scope for existing configuration variables (like `config`, `configuration`, `settings`). Reuse the existing object if present to avoid redeclaration errors and ensure consistency.
- **Commands:** Prefix all command IDs with the extension name (e.g., `cogpress.refreshBuckets`).

## Usage
Reference this profile in feature plans for VS Code extension projects alongside `skills/typescript.md`.
