# Reverify

## Intent

Re-verify published codex claims when their volatility horizon expires, and dispose of each
answer honestly: refresh what holds, correct what was wrong, supersede what the world has moved
past, and sweep for everything built on the displaced claim. A horizon on a topic is a
commitment to run this loop on that cadence; without it the library accumulates overdue
warnings and the claims quietly decay into fiction.

Reverify is the second codex loop. `Harvest.md` is triggered by a research pass and produces
claims; Reverify is triggered by a **date** (or a challenge) and re-examines claims that already
exist. The vault rules it applies stay where they live — the archivist procedure
(`docs/projects/loradel/archivist.md` in the tickets repo) §3 for the fork between errata and
supersession, §6 for the impact sweep, and the vault's `CONVENTIONS.md` §10 Claim lifecycle.
This procedure says when to open them and in what order; it never restates their mechanics.

## When to Reverify

- A topic's or claim's horizon has been reached: `lore check` reports `verify-overdue`, or the
  due date recorded in a work item (or, later, by the scheduler) arrives.
- An impact sweep or a consult found a published claim whose scope the world has displaced.
- The owner challenges a claim.

Do NOT use Reverify for:
- Claims still in draft — a harvest that needs fresh evidence runs its re-verify row inside
  `Harvest.md`.
- Routine early refreshes. A fresh `verified` stamp without new evidence resets the horizon and
  hides decay; run on or after the date, or on a challenge, never "while we are here".

## Document Storage & Naming

In the work item folder under `docs/pending/`:

- `workitem.md` — the topics and the due dates (prerequisite; a standing cycle can hold several).
- `reverify.md` — the scan table, the hypothesis table with dispositions, sweep results, gate
  results, and the edition entry. Replaces `plan.md`, `code.md`, and `test.md`.
- `briefs/web-research-<topic>-reverify-brief.md` — the brief, per `WebResearch.md`; the reply
  is archived verbatim under the owning project's `research/` with its provenance blockquote.
- `reflect.md` — per `Reflect.md`, unchanged.

## Procedure

### 1. Trigger and scope

Record in `reverify.md` what triggered the run (rule output, due date, sweep hit, or owner
challenge) and which topics it names. Run `lore check` on the codex tenant and list every
`verify-overdue` finding: overdue claims in topics the trigger did not name join the round, or
are recorded as deferred with their date. Nothing runs early (see When not).

### 2. Scan

For each topic in scope, list its living claims (`resolve --canon canon <topic>` gives the
blessed set) in the **scan table**: slug, one-line statement, `scope`, `verified`, sources, and
the edition it was last blessed in. Group the claims into **hypotheses** — one per fact the
world could have moved — quoting each claim's scope as the hypothesis's own scope. Several
claims can share a hypothesis; a claim can carry several.

### 3. Brief and round

Write one brief per topic cluster following `WebResearch.md` §2 and the brief-shape section
below, then execute and archive per its §§5–6. The codex consult in the brief's context capsule
is the round's own prior finding: every hypothesis cites "codex, ed. N, `<slug>`, verified
YYYY-MM-DD" so the researcher argues against the published state, not a paraphrase. Record both
the execution date and the reply's self-stated "as of" date in the provenance blockquote when
they differ; the "as of" date is the candidate `verified` stamp.

### 4. The date test

Before disposing of any hypothesis the reply marks **changed** or **refuted**, compare the date
of the new state (a merge, a release, a policy change — the reply must supply it) with the
claim's `verified` date:

- New state **after** `verified` → the claim was true of its interval; the world moved.
- New state **before** `verified` → the claim was wrong when stamped; we misread or missed it.
- New state **undatable** → treat as wrong-when-stamped unless the reply gives positive evidence
  the old state existed; record the uncertainty in the claim's note. A pivot without a date is
  not a supersession, because a supersession asserts an interval.

The verdict word is the researcher's; the path is decided here.

### 5. Dispose

Per hypothesis, in `reverify.md`'s **hypothesis table** (verdict, date test, path, claims
touched):

- **Holds** — refresh `verified` on each claim to the "as of" date; re-bless (archivist §2).
- **Wrong when stamped** — the errata path (archivist §3, "we were wrong"): correct, re-verify,
  re-bless; the errata note records what was misread.
- **World moved** — the supersession path (archivist §3, "the world moved"), all five steps,
  with the reply's pivot as the sibling's content.
- **Unverifiable this pass** — no stamp change, no horizon reset; an errata line records what
  could not be checked and why. An overdue claim that stays overdue is honest.

No published claim is edited before its row in the table is filled.

### 6. Sweep

For every supersession, run the impact sweep (archivist §6) and record each hit in
`reverify.md`; capture each to the owning project's intake. Reverify never reworks consumers.

### 7. Gates and edition

Run the gate checklist and cut the edition exactly as `Harvest.md` steps 7–8, recording results
in `reverify.md`; the edition entry names the horizon served and the topics touched. A held
disposition (a hypothesis whose date test the reply cannot support and the owner has not ruled
on) means no edition.

### 8. Reflect, commit, complete

Grade the brief per `WebResearch.md` §6 (did every hypothesis get a verdict line and a date?),
then `Reflect.md`, `GitCommit.md` for both repos, never push, then `Complete.md`.

## The brief shape

In addition to `WebResearch.md`'s required content, a re-verify brief SHALL:

- State the round's purpose as re-verification of published claims and ask the researcher to
  research fresh rather than recall.
- Present each hypothesis with its codex citation (edition, slug, `verified`) and its scope
  quoted from the claim.
- Require, per hypothesis, an opening verdict line — **holds / changed / refuted** — followed by
  the new state and **the date the state changed** where one exists, or "undatable" with what
  was found.
- Require the reply's own "as of" date in its Bottom line.
- Carry the WebResearch evidence standard and output shape by reference to that procedure.

## The `reverify.md` Template

```markdown
# Reverify: <Work Item Title>

## Trigger and scope
<!-- rule output / due date / sweep hit / challenge; topics; overdue claims deferred, with dates -->

## Scan
| Slug | Statement | Scope | Verified | Sources | Edition |

## Hypotheses
| Hypothesis | Claims | Verdict | New state (date) | Date test | Path |

## Sweep
<!-- per supersession: consumer hits and the intake captures made -->

## Gates
<!-- Harvest.md step 7 results -->

## Edition
<!-- tag, date, horizon served -->
```

## Cadence

Until WI 1128's scheduler exists, the trigger is manual: a work item records each due date
(the first cycle is WI 1246 — rocm-amd-stack 2026-09-26, genai-hosted-providers 2026-10-10, the
bevy-vrm leaf 2026-10-12), and `lore check`'s `verify-overdue` line is the safety net. When a
scheduler exists it SHALL emit, per due claim or topic: topic, slug or index, horizon, due date,
and the edition last blessed in — enough to open a work item without a scan.

## Guidance

- **Horizons are commitments.** A topic marked 90 days is a promise to run this loop quarterly;
  mark honestly at harvest time (archivist §1 step 3) rather than plan to skip it.
- **The verdict word is not the path.** "Changed" from a researcher can mean we were wrong; the
  date test decides, and the errata note or the pivot text says which.
- **The sweep is what makes supersession actionable.** A superseded claim with no sweep is an
  archive entry; with one, it is a list of things to fix.
- Source: loradel WI 1229's re-verify round (2026-09-01) read against archivist §3.
