### Go Tooling
- If the go module path is unknown, ask the user explicitly "What should the Go module path be?" (e.g., example.com/rimworld-mod-manager).
- Record the confirmed module path in this specification (add a line under "Programming Language(s)": "Go module path: [path]")
- Before running `go mod init`:
  - Check if a go.mod file already exists in the project root. If yes, do not run `go mod init` again; use the existing module.
  - If no go.mod exists, run `go mod init [confirmed-path]`
- Never create nested Go modules (only one go.mod at project root).
- Do not validate the module name format beyond basic sanity (human is responsible for correctness).
- All Go commands (go mod init, go build, go test, etc.) must be run with the current working directory set to the project root folder (where go.mod lives / will live).
- Before any Go tooling: verify the current directory is the individual project folder (e.g. rimworld-mod-manager/), not the parent projects/ workspace.
- When using VS Code multi-root workspace opened at projects/, ensure terminal or tasks are configured to cd into the specific project folder before running Go commands.

