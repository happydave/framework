# Go Language Guidelines

## Purpose
These guidelines ensure consistent, idiomatic Go code when the project uses Go. They apply whenever a feature plan targets Go.

The rules focus on unambiguous setup and tooling behavior so AI-generated code remains correct and maintainable without unnecessary decisions being forced.

## Core Principles
- Follow official Go idioms (Effective Go, Go Proverbs) unless explicitly overridden here.
- Prefer simplicity, explicitness, and standard practices.
- Only constrain what is necessary for correctness or project consistency.
- Explicitly grant freedom on non-critical choices.

## Module & Project Setup
- **Module path**  
  If the Go module path is unknown, ask the user:  
  "What should the Go module path be? (e.g., github.com/yourname/project-name)"  
  Record the confirmed path in the ticket's `plan.md` under "Programming Language(s)":  
  "Go module path: [confirmed-path]"

- **go.mod handling**  
  - Check if `go.mod` already exists in the project root.  
  - If it exists → do not run `go mod init`; use the existing module.  
  - If it does not exist → run `go mod init [confirmed-path]`.  
  - Never create nested Go modules (only one `go.mod` at project root).

- **Module name validation**  
  Perform only basic sanity checks (non-empty, no illegal characters).  
  User is responsible for semantic correctness of the path.

## Tooling & Build Behavior
- Always run `gofmt` (or `go fmt`) on generated code.
- Use `go mod tidy` after adding or removing dependencies.
- Build with: `go build -trimpath -ldflags="-s -w"` (produces smaller, cleaner binaries).
- Run `go vet` and consider `golangci-lint` (default config) before marking code complete.

## Coding Conventions (Defaults)
- Package names: lowercase, single word, no underscores.
- Exported identifiers: UpperCamelCase.
- Error handling: Use `errors.Is`/`errors.As`; wrap with `fmt.Errorf("%w", err)` when adding context.
- Testing: Prefer table-driven tests for logic with multiple cases.
- Dependencies: Minimize external packages; prefer standard library when reasonable.

## Security & Safety Invariants
- Never use the `unsafe` package unless explicitly required in a feature plan.
- Validate all untrusted input (use `net/http`, middleware, or approved libraries).
- Default to `math/rand` for general-purpose randomness. Use `crypto/rand` only when the feature plan explicitly requires cryptographic randomness (e.g., token generation, secret keys). Security-sensitive usage of either package is reviewed by security specialists.

## Explicit AI Freedom
The AI has full discretion over:
- Internal variable/function naming (except user-visible APIs)
- Exact file organization and package splitting (within idiomatic Go)
- Choice of standard-library helpers vs minimal third-party packages
- Minor refactoring for readability or performance (unless constrained by non-functional requirements)
- Test structure details (table-driven vs simple) unless a feature plan requires specific coverage

## Usage
Reference this file in feature plans when Go is the target language.  
Follow these rules automatically unless a feature plan explicitly overrides them.
