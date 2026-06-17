---
name: typescript-spa
description: Build environment and conventions for Vite-based SPA, game, and web projects
---
# TypeScript: SPA / Game / Web Profile

Extends [`skills/typescript.md`](../typescript.md) with Vite-based SPA, browser game, and web application build conventions. Read both documents — this profile does not repeat hub content.

## Standard Makefile Targets

| Target | Command | Description |
|---|---|---|
| `make image` | `docker build -t $(IMAGE) -f Dockerfile.dev .` | Build the dev image |
| `make install` | `$(DOCKER) npm install` | Install dependencies |
| `make dev` | see below | Start Vite dev server (interactive, port-forwarded) |
| `make build` | `$(DOCKER) npm run build` | Production bundle via `vite build` |
| `make compile` | `$(DOCKER) npm run compile` | Type-check only; no output files |
| `make clean` | *(runs on host)* `rm -rf node_modules dist` | Remove build artifacts |

### `make dev` — Docker invocation

`make dev` requires interactive TTY (`-it`) and port forwarding. It cannot use the shared `$(DOCKER)` variable and must be a separate `docker run` line:

```makefile
dev: image
	docker run --rm -it -p 5173:5173 -v "$$(pwd)":/workspace -w /workspace $(IMAGE) npm run dev
```

Port 5173 is the Vite default. If the project overrides the port in `vite.config.ts`, update the `-p` flag to match.

**There is no `make watch` target.** Vite's HMR (hot module replacement), active while `make dev` is running, fills the continuous-rebuild role that `make watch` fills in the VS Code extension profile.

## Dockerfile.dev

```dockerfile
FROM node:lts-alpine
WORKDIR /workspace
```

Minimal — no global tools required. All tooling is installed via `npm install` from `package.json`.

## `vite.config.ts` Requirements

Two settings are required for the dev server to work correctly inside Docker:

- `server.host: '0.0.0.0'` — allows connections from the Docker host. Without this, the dev server binds to `localhost` inside the container and is unreachable from the host browser.
- `server.watch.usePolling: true` — enables file-change detection across Docker volume mounts. Without this, file changes may not trigger HMR.

## TypeScript Configuration

- `tsconfig.json`: set `"noEmit": true` — TypeScript is used for type-checking only. Vite handles bundling and output.
- Target `ES2022` or later (Vite transpiles for the target browser; the TypeScript target need only be modern).
- Run `make compile` after every set of changes. It runs `tsc --noEmit` and catches type errors without producing output files.

## Compile vs. Build

| Command | What it does | When to use |
|---|---|---|
| `make compile` | `tsc --noEmit` — type errors only, no output | After every set of code changes |
| `make build` | `vite build` — production bundle to `dist/` | To verify the final artifact |

These are distinct operations. There is no `make package` target — the `dist/` output of `make build` is the deployable artifact.

## Logging

`console.log`, `console.warn`, and `console.error` are acceptable in SPA and game code. The `LogOutputChannel` restriction in the VS Code extension profile does not apply here.

## Testing

Vitest is the recommended test framework for Vite projects — it shares `vite.config.ts` and requires minimal additional setup. All test runs must be wrapped in a `make test` target, consistent with the hub guideline.

## Phaser 3 Angle API (mixed units — verify before use)

Phaser's angle utilities do not follow a consistent naming convention for radians vs degrees. Before using any `Phaser.Math.Angle.*` function, check its parameter docs.

**Radians** (degrees will silently produce wrong results):
- `Phaser.Math.Angle.Between(x1, y1, x2, y2)` — returns radians in [-π, π]
- `Phaser.Math.Angle.RotateTo(current, target, lerp)` — all values in radians
- `Phaser.Math.Angle.GetShortestDistance(a1, a2)` — radians
- `Phaser.Math.Angle.Wrap(angle)` — radians, wraps to [-π, π]

**Degrees** (radians will silently produce wrong results):
- `Phaser.Math.Angle.ShortestBetween(a1, a2)` — degrees in [-180, 180]; use this for sprite rotation
- `Phaser.Math.Angle.WrapDegrees(angle)` — wraps to [-180, 180]
- `sprite.setAngle(degrees)` / `sprite.angle` — always degrees
- `scene.physics.velocityFromAngle(degrees, speed, vec)` — degrees, 0 = east

**Recommended pattern for Phaser sprite steering** (stay in degrees throughout):
1. `Phaser.Math.Angle.Between(...)` → convert with `Phaser.Math.RadToDeg(...)` → `targetDeg`
2. `diff = Phaser.Math.Angle.ShortestBetween(currentDeg, targetDeg)` → clamp → add to heading
3. `Phaser.Math.Angle.WrapDegrees(heading)` → keep in [-180, 180]
4. `sprite.setAngle(heading)` + `velocityFromAngle(heading, speed, body.velocity)`

## Usage
Reference this profile in feature plans for SPA, browser game, and Vite-based web projects alongside `skills/typescript.md`.
