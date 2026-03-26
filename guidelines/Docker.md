# Docker Build Environment Guidelines

## Purpose
These guidelines establish a container-first build philosophy. All project build tooling runs inside Docker containers so that contributors need only Docker (and `make`) on their workstation — no language runtimes, package managers, or build tools installed locally.

This reduces onboarding friction, eliminates "works on my machine" problems, and keeps the host environment clean.

## Exemptions
The following tools are assumed to be available on the host and do not need to run in Docker:
- **Git** — standard version control; expected on every developer workstation.
- **Go toolchain** — all expected users of this framework have Go installed locally. Go projects may build natively or in Docker at the project's discretion.
- **Docker** — obviously required on the host.
- **Make** — used to wrap Docker commands. Expected on macOS/Linux; Windows users may use WSL.

All other language runtimes and build tools (Node.js, npm, Rust, Python, etc.) SHALL run inside Docker containers unless a feature plan explicitly opts out with justification.

## Core Principles
- The host machine is not a build environment. Docker is the build environment.
- A `Dockerfile.dev` in the project root defines the build image.
- A `Makefile` in the project root wraps all Docker commands behind simple targets.
- Build output is written to the host filesystem via volume mounts so that editors, debuggers, and other host tools can access it.
- Contributors should never need to run `npm install`, `cargo build`, `pip install`, or equivalent directly on their host.

## Dockerfile.dev
- Use an official base image with a pinned major version (e.g. `node:lts-alpine`, `rust:1-alpine`).
- Install only what the build requires — keep the image small.
- Set `WORKDIR /workspace` as the standard mount point.
- Do not copy source code into the image. The project directory is mounted at runtime.

Example:
```dockerfile
FROM node:lts-alpine
RUN npm install -g @vscode/vsce
WORKDIR /workspace
```

## Makefile
- Define an `image` target that builds the Docker image. All other targets depend on it.
- Use a consistent `DOCKER` variable for the `docker run` invocation.
- Mount the project directory as a volume at `/workspace`.
- For interactive/long-running commands (e.g. watch mode), use `docker run --rm -it`.
- The `clean` target runs on the host (just `rm -rf`) since it only deletes files.

Standard targets (adapt names to the project):

| Target | Description |
|---|---|
| `image` | Build the Docker image from `Dockerfile.dev` |
| `install` | Install dependencies (writes to host via volume mount) |
| `compile` | One-shot build |
| `watch` | Continuous rebuild (interactive, foreground) |
| `package` | Produce distributable artifact |
| `clean` | Remove build artifacts and dependencies (runs on host) |

Example:
```makefile
IMAGE = my-project-dev
DOCKER = docker run --rm -v "$$(pwd)":/workspace -w /workspace $(IMAGE)

.PHONY: image install compile watch package clean

image:
	docker build -t $(IMAGE) -f Dockerfile.dev .

install: image
	$(DOCKER) npm install

compile: image
	$(DOCKER) npm run compile

watch: image
	docker run --rm -it -v "$$(pwd)":/workspace -w /workspace $(IMAGE) npm run watch

package: image
	$(DOCKER) npm run package

clean:
	rm -rf node_modules dist out *.vsix
```

## Volume Mount Conventions
- The project root is always mounted at `/workspace`.
- Build output (compiled files, bundled artifacts) lands in the project directory on the host.
- Dependency directories (e.g. `node_modules/`) are also written to the host via the mount so they persist across container runs and are visible to editor tooling (language servers, IntelliSense).

## When NOT to Use Docker
- **Git operations** — always run on the host.
- **Go builds** — exempted per the Go toolchain exemption above.
- **Editor/IDE operations** — VS Code, debugging (F5), Extension Development Host, etc. run natively.
- **Simple file operations** — `rm`, `mkdir`, `cp`, etc. run on the host.
- **Running the built artifact** — if it requires a host-native environment (e.g. a VS Code extension runs inside VS Code, not in a container).

## Explicit AI Freedom
The AI has full discretion over:
- Exact Docker image choice and tag (as long as it uses an official image)
- Additional tools installed in the image beyond the minimum
- Makefile syntax details and variable naming
- Whether to use `alpine` or full images
- Shell used inside containers

## Usage
Reference this file in feature plans when the project uses Docker-based builds.
Follow these rules automatically unless a feature plan explicitly overrides them.
