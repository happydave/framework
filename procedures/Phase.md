# Phase

## Intent

Record a named group of work items, owned by one project, that must be completed together — so a comprehensive chunk of work does not leave related work items behind. A phase is the middle layer between a project (an initiative, never really finished) and a work item (one atomized unit). Project documents have long carried this concept in prose as "milestones", "checkpoints", or "M1a" title prefixes; those remain names for a phase, not a different thing. The record and the frontmatter key are `phase`.

A phase is not a plan and not a design. It carries a purpose, owner-stated exit criteria, and a way to answer "does this still owe anything?" without reading a paragraph.

## When to Create a Phase

- A project design has checkpoints or milestones whose work items must close together (see `Project.md`, Decomposition).
- A chunk of work spans several projects and needs one place where its completeness is answered. The phase is owned by one of those projects; a cross-cutting effort with no natural owner is a project in its own right, not a phase.
- A phase may be created before any of its members exist, as a planning device. Its planned-member list carries no authority (see Membership).

Phases are opt-in. Existing prose milestones are not retrofitted; a project adopts phases when it next decomposes.

## Document Storage & Naming

A phase is one flat file in its owning project's folder:

- `docs/projects/<owner>/phases/<slug>.md`

Slugs are unique within the owning project, not globally; from outside the owner a phase is referred to as `<owner>/<slug>`. Files under `phases/` that carry no frontmatter are not phase records and are ignored by tooling. Phase-level artifacts, if any arise, sit beside the record as `phases/<slug>-<artifact>.md`. A phase has no archive step: the record lives and goes with its project.

## Document Format

Phase records MUST use YAML frontmatter with exactly these three fields, followed by the body:

```
---
title: <title>
status: <pending | active | complete>
project: <owner-slug>
---

# <title>

## Purpose

...

## Exit criteria

...
```

`project` repeats the owner that the path already encodes, so a reader of the file alone knows the owner. Where the two disagree, the path is authoritative.

`workflow-phase-create` writes this format when the tooling is available. Manual creation must follow this spec.

## Required Content

- **Title** — a concise name for the phase.
- **Status** — `pending`, `active`, or `complete`. Starts as `pending`.
- **Project** — the owning project's slug.
- **Purpose** — why these work items belong together and what is true when the phase is done.
- **Exit criteria** — stated by the owner. They may be exactly "all members complete"; they may add a condition beyond membership (a suite passes, a measurement lands inside an envelope). **Do not invent exit criteria the owner did not state or directly imply** — the rule in `WorkItem.md` against invented acceptance criteria applies here unchanged.

## Optional Content

- **Planned members** — the work items intended for this phase, by ID where they exist and by title where they do not. This list is a planning device and carries **no authority** over membership; the close step reads it back as a checklist.
- **Members** — a table the tooling can regenerate from declarations. If present it is derived content and is subject to the same drift reconciliation as a project's backlog table.
- **Decisions** — dated, append-only entries following the Decision Records convention in `Design.md`.

## Membership

**A work item's own frontmatter is the only authoritative statement of phase membership.** Every member list, count, and table anywhere else is derived from the work item folders on disk.

A work item declares membership with the optional `phase` field defined in `WorkItem.md`:

- a bare slug, resolved against the work item's own `project`; or
- `<owner>/<slug>`, for a work item joining a phase owned by another project.

A work item with `project: none` must use the qualified form. A work item declares at most one phase; one that plausibly serves two joins the earlier one. SideQuest and Discover primary documents may carry the field the same way. A hand-written declaration must name a record that exists; `workflow-work-item-create` validates the value against an existing record when `phase` is supplied.

Tooling keys members by folder name, never by bare ID, because IDs in the tree are not unique.

## Procedure

1. **Create** — confirm the owning project exists and the slug is free within it. Write the record with `status: pending`, the Purpose, and the Exit criteria; add Planned members if known. Prefer `workflow-phase-create`; otherwise write the file to the format above. Note the phase in the owning project's document (Optional Content, `Project.md`).
2. **Declare** — each member work item sets its `phase` field. Work items created later join by declaring; nothing is edited in the phase record.
3. **Activate** — set `status: active` by hand when work on a member begins. The tooling's derived state (open and terminal counts, mid-flight members) shows whether that is true; a declared status that disagrees with the derived state is reported, not hidden.
4. **Close** — the gate, in order:
   1. Compute the members from declarations across `docs/pending/`, `docs/hold/`, and `docs/archive/`.
   2. **Refuse while any member is open**, naming the open members. A member is open unless its status is one the tooling treats as terminal — `complete`, `completed`, `superseded`, `reverted`. A missing status, `pending`, `deferred`, and any unrecognised value are open. A member in `docs/hold/` with an open status is open: held work is owed work. An archived member is terminal by construction (`Archive.md` requires `complete` first).
   3. Read back the Planned members list and report, as **warnings, never refusals**, any entry that resolves to no work item ("planned, never created") or to a work item that does not declare this phase. The owner may well have dropped the entry deliberately; the warning exists because a work item intended for a phase and never written is exactly the "left behind" case.
   4. Confirm any exit criteria beyond membership are met, and record the evidence as a dated entry in the record.
   5. Set `status: complete`. Prefer `workflow-phase-complete`, which applies steps 1–3 and refuses on 2; by hand, apply the same gate and say so in the dated entry.
   6. Update the owning project's document, as `Complete.md` has work items do. If this closes a design line, offload its completed rows to the project's history in the same edit.

Phases **never auto-complete** when their last member closes, because exit criteria may exceed membership, and a phase **never blocks** a member's own completion or archival. The close gate is the only enforcement point.

## Status Tracking

- **pending** — created; may have no members yet.
- **active** — work is under way. Set by hand.
- **complete** — the gate passed. Written by `workflow-phase-complete`, or by hand at the owner's risk.

There is no override flag. The owner can always edit the file by hand and the tooling never prevents that; the tooling itself only ever writes `complete` onto a phase that owes nothing. A later extension of the work item status taxonomy may grow the terminal set; the gate follows the tooling's classification, which is defined once, so a hand-applied gate and the tool never disagree.

## Guidance

- Sequencing between phases ("decompose checkpoint 3 when 2 is reached") is prose in the project document. It is a judgement made at a review, not a dependency edge, and is not modelled.
- Keep the record short. Purpose and exit criteria are a paragraph each; a phase that takes longer to write than a work item is trying to be a design.
- A phase spanning projects is still owned by one project and appears on that project's surfaces; the members' own backlogs are unchanged. A cross-cutting effort nobody owns is a project.
- When a work item completes and it was the last open member of its phase, say so in the completion report and point here (`Complete.md`, step 3). Do not close the phase from a work item's pipeline.
