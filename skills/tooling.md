---
name: tooling
description: Tool-selection policy and credential handling for external tools
---
# Tooling Guidelines

## Purpose
These guidelines govern how external tools — CLIs, MCP servers, editor extensions — are chosen and used during workflow execution. They exist because the same operation is usually reachable several ways (a purpose-built CLI, a raw API call, a hand-rolled script), and picking inconsistently produces work that cannot be reproduced or reviewed.

This document is **normative**: it defines policy. Tool-specific reference material — flags, endpoints, auth setup, known gaps — lives in `knowledge/tools/` and is non-normative.

## Core Principles
- Prefer a purpose-built tool over a hand-rolled equivalent. A wrapper that already handles auth, pagination, and error reporting is more reliable than a fresh script.
- Prefer the framework's own tooling over reimplementing a check (see the `internal` section of `AGENTS.md`).
- Verify a tool works before depending on it. Report what failed rather than silently routing around it.
- Never widen a tool's blast radius beyond what the task requires.

## Authoritative Tools
When more than one path exists, use the tool named here. Deviations must be justified in the plan.

| Domain | Tool | Notes |
| :--- | :--- | :--- |
| Markdown duplicate detection | [`internal/dupcheck.py`](../internal/dupcheck.py) | Per `skills/markdown.md`; do not reimplement the heuristic. |
| Observability evidence | See `skills/evidence.md` | Defines which source proves what. |

Raw `curl` against an API that has a supported CLI is a deviation, not a shortcut. It bypasses auth handling and produces commands that only work in the session that wrote them.

## Credential Handling
Credentials are never content to be read, quoted, or summarized.

- **Do not read secrets into context.** Never `cat` a credential file, echo a token, or include one in a document, log, or commit. This includes `~/.netrc`, keyring exports, `.env` files, and CI variables.
- **Using a credential via a tool that reads it itself is correct.** A CLI reading its own keyring or config entry is fine; extracting the token to pass along by hand is not.
- **Pipe, never print.** When a secret must move between tools, stream it (`... | tool --stdin`) so it never lands in output, shell history, or a transcript.
- **Inspect structure, not values.** Checking that a credential entry exists is legitimate; reading its value to confirm is not.
- **Re-authentication is a human step.** When auth fails, report the failure and the command that fixes it. Do not attempt to mint, refresh, or reconstruct credentials.

## Verifying Tool Availability
Before a procedure depends on a tool, confirm it is present and authenticated. A tool that is installed but unauthenticated fails in ways that read like bugs in the work.

1. Confirm the tool exists on `PATH`.
2. Confirm auth succeeds against the specific host or project in scope.
3. Exercise one read-only call representative of the intended use.

Record the outcome. If verification fails, that is a finding to report — not a reason to substitute an unverified alternative.

## Destructive Operations
Tools that expose write and delete operations alongside reads require deliberate narrowing.

- Read-only operations may be performed as needed.
- Write operations (comment, approve, merge, push, tag) require the request to be explicit in the user's current instruction.
- Delete and revoke operations require confirmation before execution, regardless of prior authorization in the session.
- An MCP server or CLI that exposes destructive subcommands should be constrained by permission rules rather than by intention alone.

## Recording Tool Knowledge
Tool findings decay. When work turns up something non-obvious about a tool — a missing flag, a surprising default, an auth quirk — record it:

- **Reference detail** → add or update `knowledge/tools/<tool>.md`.
- **Policy change** (a different tool becomes authoritative, a new credential rule) → update this file and the Authoritative Tools table.

Adding a new tool dependency to a project means adding its reference doc in the same change.

## Explicit AI Freedom
The AI has full discretion over:
- Which specific subcommands or flags accomplish a given operation, provided the authoritative tool is used
- Output formatting choices (`--output json`, `jq` filters, field selection)
- Whether to verify tool availability inline or as a separate preliminary step
- How to structure a `knowledge/tools/<tool>.md` document, provided it is reference material rather than policy

## Usage
Reference this file in plan documents whenever implementation or investigation depends on an external tool. Follow these rules automatically unless a plan explicitly overrides them.
