---
name: versioning
description: Version increment policy: one ticket, one patch
---
# Versioning Guidelines

## Purpose
These guidelines define the versioning policy for projects managed under this framework. Consistent versioning ensures that progress is trackable and that releases (even minor internal ones) are clearly identified.

## Core Policy: One Ticket, One Patch
For most projects (see Exemptions below), every completed work item SHALL result in exactly one patch version increment.

- **Trigger**: Successful completion of all implementation and verification steps for a work item.
- **Increment**: Increment the patch version (e.g., `1.2.3` -> `1.2.4`).
- **Timing**: The version bump should be the final change made during the **Code** phase, just before closing the work item.

## Project-Specific Implementation
The exact mechanism for versioning depends on the project's language and tooling:

- **TypeScript / Node.js**: Increment the `version` field in `package.json`.

## Regenerate the Lock File
When the manifest version is bumped, **regenerate the project's lock file and include it in
the same commit.** Bumping the manifest alone leaves the lock file's own version field
stale, so the manifest and lock drift apart over successive work items.

- **TypeScript / Node.js**: after editing `package.json`, run the lock-regeneration target
  (e.g. `make install`, which wraps `npm install`) so `package-lock.json` picks up the new
  version, and stage the lock alongside the manifest. Verify the resulting lock diff is
  version-field-only (no unexpected dependency churn) before committing.
- Projects that version via tooling which already rewrites the lock (e.g. Cargo, where
  `Cargo.lock` regenerates on the next build) still SHALL commit the regenerated lock with
  the version bump — do not defer it to a later commit.

## Exemptions

### Go Projects
Go projects are **exempt** from this specific file-based versioning policy.
- **Reason**: Go versioning is idiomatic via git tags (`v1.2.3`).
- **Policy**: Unless the plan specifies otherwise, skip tagging for Go Projects.
