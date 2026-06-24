---
name: rust
description: Rust language + Bevy conventions, cargo tooling, headless-crate rule, feature gating
---
# Rust Language Guidelines

## Purpose
These guidelines ensure consistent, idiomatic Rust, and capture the Bevy-specific conventions needed for projects in this framework (notably the Sounding game). The rules focus on unambiguous tooling and a small number of load-bearing architectural conventions, leaving non-critical choices to the implementer.

## Core Principles
- Follow official Rust idioms (the Rust API Guidelines, `clippy` defaults) unless explicitly overridden here.
- Prefer simplicity, explicitness, and the standard library; add a dependency only when it earns its place.
- Use cargo's native tooling directly. **Do not introduce a Makefile** (Makefiles are for node/npm-style projects, not Rust — same convention as Go here).
- Only constrain what is necessary for correctness or project consistency; grant freedom on the rest.

## Toolchain
- Use **rustup** with a `stable` toolchain; a distro-packaged `rustc` is frequently too old for modern engine crates.
- **Verify the toolchain meets a dependency's MSRV before implementing against it.** For a new language/engine dependency (e.g., a Bevy major version), check the required Rust version first — a too-old compiler is a planning prerequisite, not a mid-implementation surprise. Installing or upgrading a toolchain is an environment action: flag it for the human (or obtain authorization) rather than assuming it.

## Testing & Verification
These are the **build** and **test** steps the Code and Document actions rely on:

- **Build:** `cargo build`. When a crate has meaningful cargo features (e.g., a `dev` feature), build each relevant configuration (`cargo build`, `cargo build --features dev`).
- **Test:** `cargo test` (whole workspace) or `cargo test -p <crate>` for a targeted crate.
- **Format gate (build):** `cargo fmt --all --check` must pass with no diff.
- **Lint gate (build):** `cargo clippy --all-targets` must be clean; lint each meaningful feature configuration too (e.g., `cargo clippy -p <crate> --features dev`).
- Run the format and lint gates before considering changes complete. Prefer running a targeted `cargo test -p <crate>` after non-trivial edits to catch errors early.

## Workspace & Project Setup
- Prefer a **cargo workspace** (a virtual root manifest with `members`) once a project has more than one crate. Share versions and dependency versions via `[workspace.package]` and `[workspace.dependencies]`; member crates use `version.workspace = true` and `<dep> = { workspace = true }`.
- One lockfile at the workspace root. Do not nest workspaces.
- Crate and binary names are the implementer's choice unless user-visible or specified in the plan.

## Architecture Documentation
- Maintain a repo-root `ARCHITECTURE.md` (per `skills/documenting-architecture`): the LLM-oriented code map — version context, `Forbidden:`/`Required:` boundaries, a component index, and the primary data flow.
- **Update it on structural change** — a crate added/removed/renamed, a cross-crate dependency or boundary changed, or a data-flow step added/removed — and include it in the **Document** pass of such work items, the same way the version bump is part of the **Code** pass. A stale architecture map is worse than none.

## Bevy Conventions
- **Headless-crate rule (load-bearing).** A crate that must build and run without rendering — a simulation core, a headless server, anything intended for display-less environments — depends on the **Bevy sub-crates** it actually needs (`bevy_app`, `bevy_ecs`, `bevy_time`, `bevy_state`, ...), **never the `bevy` umbrella crate.**
  - Rationale: a workspace has a single instance of the umbrella `bevy`, and the resolver **unifies features across workspace members**. If any member (e.g., the windowed app) enables rendering, the umbrella gains `bevy_winit`/`bevy_render`/`wgpu`, and *every* crate depending on the umbrella inherits them — even under `cargo build -p <headless-crate>`. Depending on sub-crates keeps the headless crate's graph free of rendering regardless of what other members enable.
  - Cross-composition is safe: `bevy::app::App` is a re-export of `bevy_app::App`, so a `bevy_app::Plugin` defined in a sub-crate plugs into an umbrella-based application unchanged.
  - **Verify, don't assume:** `cargo tree -p <crate>` must show no `bevy_render`, `bevy_winit`, or `wgpu` for a crate claimed to be headless. Treat this as a runnable invariant.
- **Organize simulation logic as Bevy `Plugin`s** so the same logic composes into headless and windowed apps.
- **Scene/mode teardown: tag only the root.** For entities spawned for a transient scope (a UI panel, a render set, a game mode), put the despawn marker component on the **root** of each spawned tree only. `Children` is a `linked_spawn` relationship, so a recursive `despawn` of the root already removes its descendants; tagging children with the same marker makes the teardown system re-despawn already-dead entities and log a double-despawn warning on every transition.
- **Gate dev-only tooling behind a cargo feature** (e.g., `dev`) so it is absent from default and release builds — applies to the Bevy Remote Protocol and any other debug/inspection plugins.
- **Verify Cargo feature flags against source or examples, not by name.** Feature names collide across crates (e.g., a `http` feature may mean a web asset source in one crate and nothing to do with the remote-protocol transport you intended). Confirm the feature's actual effect from the dependency's `Cargo.toml`/examples before relying on it.

## Coding Conventions (Defaults)
- Modules and functions: `snake_case`; types and traits: `UpperCamelCase`; constants: `SCREAMING_SNAKE_CASE`.
- Prefer `?` and typed errors; reach for `thiserror` (libraries) or `anyhow` (binaries) only when std errors become unwieldy — not by default.
- Document public items with `///` doc comments; keep them accurate to current behavior.
- Keep modules small and cohesive; file/module organization is otherwise the implementer's discretion.

## Security & Safety Invariants
- **Never use `unsafe`** unless a feature plan explicitly requires it; if used, isolate and document the invariant it upholds.
- Validate untrusted input at boundaries (network, file, IPC).
- Default to non-cryptographic randomness for gameplay; use a cryptographic RNG only when a plan explicitly requires it.

## Explicit AI Freedom
The AI has full discretion over:
- Internal variable/function naming (except user-visible APIs).
- File and module organization within idiomatic Rust.
- Crate and binary names unless user-visible or specified in the plan.
- The precise set of Bevy sub-features per crate, provided the headless-crate rule holds.
- Minor refactoring for readability or performance unless constrained by non-functional requirements.

## Usage
Reference this file in plan documents when Rust is the target language (and note the Bevy conventions when Bevy is used). Follow these rules automatically unless a plan explicitly overrides them.
