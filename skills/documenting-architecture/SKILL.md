---
name: documenting-architecture
description: Use when creating or updating ARCHITECTURE.md in a repository — new project setup, structural refactors, addition or removal of packages or services, or when Document.md identifies architecture drift. Generates LLM-optimized codebase maps with absolute paths, key-value component indexes, and explicit data flow sequences.
---

# Architecture Documentation

## Purpose
Produces `ARCHITECTURE.md` files optimized for LLM consumption: absolute path mappings, key-value component indexes, no visual diagrams. Enables a cold AI session to orient itself without exploratory reads.

## When to Use
- New repository or project setup — before first implementation
- Structural change: package added/removed, service boundary shifted, data flow path changed
- After any work item that alters the import graph
- When `Document.md` identifies architecture drift

**Not for:** API reference, README setup steps, inline code comments.

## Scope
One `ARCHITECTURE.md` per repository root. For monorepos with distinct services, one per service directory. Never per-package.

## Generation Process

### 1. Survey the Repository
```bash
find . -name "go.mod" -o -name "package.json" -o -name "pyproject.toml"  # module roots
find . -type f -name "*.go" | grep -E "main\.go|cmd/" | head -20          # entry points
```
Read entry points first (`main.go`, `cmd/`, `index.ts`), then work outward following imports.

### 2. Collect Version Context
Read version declarations from `go.mod`, `package.json`, `pyproject.toml`, and `FROM` lines in any Dockerfile.

### 3. Identify Architectural Boundaries
Determine what is explicitly forbidden to cross: which packages may not import others, which layer owns each external I/O surface (HTTP, database, filesystem), which state is global vs. component-local.

### 4. Build the Component Index
For each meaningful component (package, service, or module — not individual files unless the repo is small):
- **Name:** package or service name
- **Path:** absolute repository path
- **Inputs:** types, events, or requests it receives
- **Outputs:** types, responses, or side-effects it produces

Granularity: one entry per Go package, Node module, or Python package — not per file.

### 5. Trace Data Flow
Follow the primary request or data lifecycle from entry point to persistence or response. Write as a numbered linear sequence.

### 6. Write and Verify
Apply format rules below. After writing, confirm every path exists in the repository:
```bash
find . -path "<path>" | head -1
```
A path that does not resolve is a hard error — correct it before finishing.

## ARCHITECTURE.md Format Rules
- Markdown only — no Mermaid, C4 diagrams, or ASCII art
- Key-value lists over paragraphs
- Absolute repository paths (`/internal/auth/`, not "the auth package")
- No introduction, history, or motivation sections
- Begin immediately with `## Version Context`

## Required Sections

**Version Context**
Exact versions of primary languages and frameworks, sourced from module files.

**Architectural Boundaries**
State as explicit `Forbidden:` / `Required:` rules:
```
Forbidden: packages under /internal/ importing from /cmd/
Required: all database access routes through /internal/store/
```

**Component Index**
```
- **AuthService** `/internal/auth/`
  - Inputs: LoginRequest, TokenRefreshRequest
  - Outputs: SessionToken, side-effect: writes to /internal/store/sessions/
```

**Dependency Chains**
Direct statements of internal module reliance:
```
/api/ types derive from /internal/domain/types.go
/cmd/worker/ depends on /internal/queue/ and /internal/store/
```

**Linear Data Flow**
Numbered sequence for the primary lifecycle:
```
1. HTTP request arrives at /api/handler.go
2. Validated and parsed into domain.Request (/internal/domain/)
3. Business logic applied in /internal/service/
4. Persisted via /internal/store/
5. Response serialized and returned
```

## Maintenance Triggers
Update `ARCHITECTURE.md` when any of the following change:
- A package or service is added, removed, or renamed
- An import dependency is added or removed between packages
- A data flow step is added or removed
- The primary runtime version changes in `go.mod` / `package.json`

## Explicit AI Freedom
The AI has full discretion over:
- Which components to include vs. group (judgment call on granularity)
- Exact wording of boundary rules (as long as stated as constraints, not descriptions)
- Ordering of Component Index entries
- Whether to add a `## Known Gaps` section for areas not fully traced

## Usage
Reference this skill in `plan.md` when a work item creates a new repository, adds or removes packages, changes service structure, or alters data flow. Include `ARCHITECTURE.md` in the scope of every `Document.md` pass.
