---
name: go
description: Go language conventions, tooling, and testing rules
---
# Go Language Guidelines

## Purpose
These guidelines are intended to ensure consistent, idiomatic Go code.

The rules focus on unambiguous setup and tooling behavior so AI-generated code remains correct and maintainable without unnecessary decisions being forced.

## Core Principles
- Follow official Go idioms (Effective Go, Go Proverbs) unless explicitly overridden here.
- Prefer simplicity, explicitness, and standard practices.
- Prefer writing base library code over importing libraries for trivial functions.
- Only constrain what is necessary for correctness or project consistency.
- Explicitly grant freedom on non-critical choices.

## Testing
- *NEVER* use `-short` with `go test`. There is no plan-level override for this.
- *NEVER* run `go build` to test; use `go test` (or `go run` if you want to interact with a running instance).
- Always run `go test ./...` before making changes to verify the state of the project.
- Always run `go test ./...` after all changes are made for final verification.
- **Run the documented gate, not a faster decomposition of it.** If the project documents one whole-module command as its gate, run that command. Splitting it into parallel halves changes what is tested — inter-package contention is part of what the combined run exercises, and a split has hidden a real regression for a whole session. If the combined command is too slow, record that fact; it is not a licence to substitute the halves.
- `TestMain` must live in a `_test.go` file. A `TestMain` in a regular file compiles without complaint and never runs.
- **A benchmark's parallelism is part of its claim.** `-cpu` and `b.RunParallel` set the concurrency
  the result is *about*. Go weights mutex profiles by the number of blocked goroutines precisely
  because a lock with 100 waiters dominates one with 1 — so a change to lock scope measured at tens
  of goroutines says nothing about thousands, and "neutral in the benchmark" has shipped a change
  that stopped a system's connect path completing at all. Measure at the concurrency the system
  reaches, or record that you did not.
- **Concurrent test harnesses need production-grade discipline.** Collectors, fakes, and recorders shared between the code under test and the test itself must be locked like any shared state. Run a new concurrent package with `-race -count=5` before calling it stable — a single green `-race` run is one schedule, not evidence.

## Module & Project Setup
- **Module path**
  If the Go module path is unknown, stop and ask:
  "What should the Go module path be? (e.g., github.com/yourname/project-name)"
  Record the confirmed go path in `plan.md`.

- **go.mod handling**
  - Check if `go.mod` already exists in the project root.
  - If `go.mod` exists do not run `go mod init`; use the existing module.
  - If `go.mod` does not exist run `go mod init [path]` using the go path specified in the plan.
  - Never create nested Go modules (only one `go.mod` at project root).

- **Module name validation**
  Perform only basic sanity checks (non-empty, no illegal characters).
  User is responsible for semantic correctness of the go path.

- **vendor/ directory**
  Never edit files inside `vendor/` directly. The directory is fully managed by `go mod vendor`, which overwrites it entirely on every run. Any manual changes are invisible to the build server and will cause build failures.

## Tooling & Build Behavior
- Always run `gofmt` (or `go fmt`) on generated code.
- Use `go mod tidy` after adding or removing dependencies.
- Test using `go test` (`go test ./...` or a more targeted path for specific changes).
- Run `go vet` after all changes.
- **Verification after Edits:** Always run `go vet` (or the project's equivalent build/verification step) after any non-trivial `replace_string_in_file` operation. This ensures that syntax errors introduced by automated edits (e.g., shell interpolation issues) are caught immediately before further implementation or testing.
- If available run `golangci-lint` before considering changes complete.
- Always run `go mod tidy` and `go mod vendor` before `go generate`.
- Always use `go generate` to generate code, never use `generate.sh` or similar.
- A `go:generate` directive runs with the working directory of the file that carries it. A generator that inspects the module (walking sources, reading `go.mod`) must locate the module root itself — `go env GOMOD` — rather than assuming the current directory is it.
- **errcheck and `io.Writer`:** errcheck's default exclusions silence unchecked writes to the concrete `os.Stdout`/`os.Stderr`, but *not* writes to an `io.Writer` value. A testable CLI whose core takes writer parameters (e.g. `run(args []string, stdout, stderr io.Writer) int`) will therefore be flagged on every `fmt.Fprintln`/`Fprintf` even though the equivalent code writing to `os.Stderr` directly passes. Prefer routing output through small helpers that explicitly discard the unrecoverable write error — e.g. `func fprintln(w io.Writer, a ...any) { _, _ = fmt.Fprintln(w, a...) }` — which centralizes the discard rather than scattering `_, _ =` or `//nolint` across call sites.

## Coding Conventions (Defaults)
- Package names: lowercase, single word, no underscores.
- Exported identifiers: UpperCamelCase.
- Error handling: Use `errors.Is`/`errors.As`; wrap with `fmt.Errorf("%w", err)` when adding context.
- Testing: Prefer table-driven tests for logic with multiple cases.
- Dependencies: Minimize 3rd party imports; prefer writing standard library code when reasonable.
- JSON slice initialization: When a function returns a slice that will be marshalled to JSON, initialize it with `make([]T, 0)` rather than `var s []T`. An uninitialized slice marshals to JSON `null`; `make([]T, 0)` marshals to `[]`, which is the expected form for JSON arrays in MCP tool responses and most API contracts.
- SQL embedded in Go code: follow `skills/sql.md`. Add it to the plan's Applicable Guidelines alongside this file whenever the work touches queries, schema, or migrations.
- Comments: a comment stating a fact about *other* code's behavior ("the caller never passes nil", "X is already replicated by the time this runs") is a liability — it goes stale silently. Prefer deriving the fact locally, testing it, or asserting it so a violation fails loudly; reserve prose for constraints the code cannot express.

## Security & Safety Invariants
- Never use the `unsafe` package unless explicitly required in a feature plan.
- Validate all untrusted input (use `net/http`, middleware, or approved libraries).
- Default to `math/rand` for general-purpose randomness. Use `crypto/rand` only when the feature plan explicitly requires cryptographic randomness (e.g., token generation, secret keys). Security-sensitive usage of either package is reviewed by security specialists.

## Explicit AI Freedom
The AI has full discretion over:
- Internal variable/function naming (except user-visible APIs)
- Exact file organization and package splitting (within idiomatic Go)
- Minor refactoring for readability or performance (unless constrained by non-functional requirements)
- Test structure details (table-driven vs simple) unless the plan specifies specific coverage

## Usage
Reference this file in plan document when Go is the target language.
Follow these rules automatically unless a plan explicitly overrides them.
