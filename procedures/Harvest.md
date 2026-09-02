# Harvest

## Intent

Distil existing research sources — archived WebResearch replies, Discover documents, spikes,
findings records, work-item notes — into published codex claims in the lore vault, and cut an
edition. A harvest is a **content** work item: its plan is a source inventory plus a claim
manifest, its implementation is authoring anchors and claims, and its test is a fixed gate
checklist. Run through the generic pipeline, such a work item produces a `plan.md` whose real
content is a manifest and a `code.md` that logs a checklist; Harvest collapses those into their
true shape while keeping the two review gates, which are the steps that catch misread sources,
mislabelled confidence, and missing dates.

Harvest sits between a SideQuest and the full pipeline, as `Spike.md` does: three documents, two
reviews, one checklist. The normative rules for the vault stay where they live — the archivist
procedure (`docs/projects/loradel/archivist.md` in the tickets repo) and the vault's
`CONVENTIONS.md` §10. This procedure says when to open them and which sections apply; it never
restates them.

## When to Harvest

- A work item names one or more existing research artifacts and one or more target codex topics.
- The ledger or a Reflect says a research pass "should reach the codex".
- A consult found "codex: no prior coverage" on a subject the estate has already researched.

Do NOT use Harvest for:
- New research (`Discover.md`, `WebResearch.md`) — harvest what they archive, afterwards.
- Re-verifying published claims when a horizon expires (`Reverify.md`).
- Fiction tenants of the vault (universe-gen imports and hand-authored lore follow `CONVENTIONS.md`
  §§1–9 directly).

## Document Storage & Naming

In the work item folder under `docs/pending/`:

- `workitem.md` — the sources, the target topics, and any stated constraints (prerequisite).
- `harvest.md` — the distillation plan (source inventory, claim manifest), the authoring log, the
  gate results, and the edition entry. Replaces `plan.md`, `code.md`, and `test.md`.
- `harvestreview.md` — two review passes: §A the distillation review (before authoring) and §B
  the fidelity review (after). Replaces `planreview.md` and `codereview.md`.
- `reflect.md` — per `Reflect.md`, unchanged.

Vault content lands in the lore repo (`universes/codex/`); the tickets work item folder holds the
paper trail.

## Procedure

### 1. Prerequisite: Work Item

A harvest begins with a `workitem.md` naming its sources and target topics. If it names neither,
it is not ready: send it back through `Triage.md` or the codex ledger.

### 2. Read

Read in full before planning: archivist §1 (harvest intake) and §2 (promotion); `CONVENTIONS.md`
§10 including its Claim lifecycle subsection; every source artifact the work item names; the
existing index of every target topic that already exists; and the vault's `check` rule list in
the lore `README.md`. Run a codex search for each target subject and record the result in the manifest preamble
(step 3) — an existing topic means claims extend it, and existing claims are cross-link
targets, not candidates for re-authoring.

### 3. Distillation plan (`harvest.md`)

Write the two tables that are the plan:

**Source inventory** — one row per source artifact: path; the document's own date (or the rule
archivist §1 step 5 gives for undated sources); transport or producing procedure (the
`generator` value); anchor slug, marked **new** or **reused from WI n**; and whether a re-verify
round is needed. Digests are not planned — they are computed at authoring per `CONVENTIONS.md`
§4 with the vault's digest tooling, never by hand.
A source shared with an earlier harvest is a reuse row; a source whose evidence has moved since
it was written gets a **re-verify** mark, and the round runs through `WebResearch.md` before
authoring, its archived reply becoming one more source row.

**Claim manifest** — one table per target topic: slug; one-line statement; confidence (translated
per archivist §1 step 2); scope (or "stable"); verified date (per archivist §1 step 3 — every
claim carries one); sources; harvest anchor; and horizon or leaf mark where the topic's index
does not already carry one. Below the table: errata seeds from the sources' stated gaps, the
cross-link targets in other topics (linked by slug, never duplicated), and any topic that another
queued harvest will create — named in prose only (archivist §1 step 5).

Size: a manifest over about twenty claims for one topic is split — sibling topics, or a second
work item — before review, because a fidelity sample cannot cover more.

### 4. Distillation review (`harvestreview.md` §A)

The review gate before authoring. External if a reviewer is available; otherwise **self-applied**
in the same session under the `PlanReview.md` provision, with its three countermeasures: record
the mode, record the sample, and never resolve an uncertain finding in the plan's favour.

Dimensions, each producing Blocking or Non-blocking findings:

- **Fidelity** — open the cited source for a sample of manifest rows (at least six, including the
  rows with numbers, version pins, and quotations) and confirm the statement says what the source
  says. A precise but false row is Blocking.
- **Labels** — vendor claims, single sources, and inferences are not `confirmed`; conflicting
  sources are `contested`; examined-but-unresolved is `inconclusive`.
- **Dates** — every row has a `verified` date that follows the source's date rule; scoped rows
  name the scope in the statement as well as the field.
- **Scope** — the manifest covers what the work item names and nothing it does not; deliberate
  omissions are listed with a reason.
- **Links** — no forward wiki-links to topics that do not exist yet; shared anchors are reuse
  rows; cross-links to other topics resolve to real slugs.
- **Size** — the cap in step 3 was applied.

Record the status (Complete / Significant Findings), the sample, and the uncertain findings with
their dispositions. Revise `harvest.md` until no Blocking finding remains.

### 5. Author

In the lore repo, in this order: anchors (`type: document`, `provenance: generated`, the full
`source` group per archivist §1 steps 1 and 5); claims, one file per manifest row with the
frontmatter `CONVENTIONS.md` §10 requires and the quoting rule from archivist §1 step 2; the
topic index and errata note; the tenant's notes index; then blessing, top-down per archivist §2.
Log deviations from the manifest — a row merged, a label raised on new evidence, a claim dropped
— in the **Authoring log** section of `harvest.md` as they happen, not afterwards.

### 6. Fidelity review (`harvestreview.md` §B)

The review gate after authoring, self-applicable as in step 4. Re-sample the authored claims
against their opened sources: at least six claims, chosen from the categories most easily
garbled (API facts, counts, licence clauses, quotations), plus every row whose label the
authoring log raised. Check for hedges lost in authoring (a `confirmed` claim resting on a
vendor page), forward links, and — where the topic borrows from a licence or legal topic — run a
text search for a distinctive clause from the source topic and require zero hits. Tiers per
`CodeReview.md`: Escalations (a claim no opened source supports — the harvest **holds** and
nothing is blessed or tagged), Resolved, Observations; then the disposition.

### 7. Gate checklist

Run every item; record the results in the **Gates** section of `harvest.md`:

1. `lore check` on the codex tenant: 0 violations, and no new warnings the manifest did not
   predict; then on every other tenant: unchanged. The `missing-verified` violation and the
   `unknown-generator` warning are what make the manifest's dates and generators
   machine-checked here.
2. `lore digest check` over the topic's anchors: every one `ok`.
3. `resolve --canon canon <topic>` lists exactly the manifest's blessed claims; errata absent.
4. `go test ./...` in the lore repo passes.
5. Dupcheck on the topic index and the tenant root (`skills/markdown.md`).
6. The cross-link text search from step 6 where it applies.
7. Link validation on every tickets document touched.

A failure is fixed and the checklist re-run from item 1. A digest mismatch is fixed by
recomputing, never by editing the recorded value.

### 8. Edition

Cut the edition per archivist §4 — the annotated tag and the root entry — and record the tag in
`harvest.md`. One edition per coherent blessing batch; a held fidelity review means no edition.

### 9. Reflect, commit, complete

`Reflect.md` as usual. Commit the lore repo (content plus tag) and the tickets repo per
`GitCommit.md`; never push. Then `Complete.md`.

## The `harvest.md` Template

```markdown
# Harvest: <Work Item Title>

## Source inventory
| Source | Date | Generator | Anchor | New/reused | Re-verify? |

## Claim manifest — <topic slug> (horizon: <days or stable>)
| Slug | Statement | Confidence | Scope | Verified | Sources | Anchor |

Errata seeds: … Cross-links: … Named in prose only: …

## Authoring log
<!-- deviations from the manifest, as they happen -->

## Gates
<!-- the seven checklist results -->

## Edition
<!-- tag, date, root entry -->
```

## The `harvestreview.md` Template

```markdown
# Harvest Review: <Work Item Title>

## A. Distillation review
Status: … Mode: external | self-applied
Sample: <rows checked → sources opened>
Findings by dimension (Fidelity, Labels, Dates, Scope, Links, Size): Blocking / Non-blocking
Uncertain findings and dispositions: …

## B. Fidelity review
Mode: … Sample: <claims re-read → sources>
Escalations / Resolved / Observations
Disposition: proceed to gates | held
```

## Guidance

- **The manifest is the plan.** If a design question arises that the manifest cannot express —
  a topic split, a horizon choice with consequences for consumers — write it under the manifest
  as a decision with its reason; do not grow a separate plan.
- **Verify against opened sources, never memory.** Both reviews are factual checks; a reviewer
  who has not opened the source has not reviewed the row.
- **Blessing means vetted, not true.** A contested claim is blessed with its contested-ness as
  content; hedging it into `supported` to make it publishable is a fidelity failure.
- **Tooling.** When the lore binary provides anchor, claim, and digest verbs, use them; until
  then the vault's digest helper stands in. The procedure does not change either way.
- Source: loradel WIs 1229–1233 (codex-ed3 through ed6) and their reflects.
