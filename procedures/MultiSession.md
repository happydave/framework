# Multi-Session

## Intent

Run a multi-session arc — one owner objective executed by several cooperating sessions, often while the owner is away — on named roles and artifact-borne authorization instead of improvised protocol and relayed approvals. Authorization that travels session-to-session degrades into unverifiable hearsay with each hop, and a fleet's natural failure mode is well-meaning proxying that manufactures authority no one granted (`../internal/DESIGN.md`, Artifact-Borne Authorization). This procedure makes authorization something any session can verify by reading the repo, and makes the wiring between sessions explicit enough that hand-offs cannot silently drop.

## Roles

Roles are named per arc, even when one session wears several hats — they are obligations, not headcount. An arc that is genuinely one session does not need this procedure.

- **Coordinator** — owns arc content: sequencing, dispatch briefs (`Dispatch.md`), gated follow-ons. Stays out of the executor's working tree.
- **Developer (executor)** — brief-driven: works from the dispatch brief, runs to a natural gate or pings the shepherd at each stop, and reports completion to the party the brief names.
- **Shepherd** — owns liveness and legitimacy: subscribes to executor idle notices, keeps a fallback heartbeat, nudges stalls, routes safeguards-flagged work per the brief, brokers consults, and keeps the decision log and morning brief where the owner will read them. The shepherd is explicitly NOT an authorizer: a shepherd go-ahead is never the owner's answer.
- **Tester** — a fresh-context session running `Test.md` against the artifacts. Invoke for significant verification only (multi-host runbooks, load tests, checkpoint gates). The value is independence from the diagnosis: a session with no investment in a finding is the natural catcher of a harness measuring the wrong thing — the 2026-09-05 arc's measurement error was made and caught by the same session.

A role stays defined here until it accrues standalone playbooks; only then does it split into an `agents/` persona (the `../agents/ops.md` precedent). A shepherd persona was considered and declined on this condition — re-raise when the condition triggers.

## Artifact-Borne Authorization

Authorization derives from committed artifacts and the owner's own messages, never from peer attestation. Peers carry pointers to authorization (cite the committed artifact); they do not re-grant it. Two layers, both committed to git:

**Standing (per project)** — a standing-authorization section in the project's `project.md`, stating that work items under the project may be taken through the full pipeline without further owner authorization, subject to the standing constraints it lists (e.g. never push, ops authorization tiers, `[human]` gates hold rather than block, owner questions stay open but do not stop work). The section is owner-edited only: git history makes a session-edited authorization detectable, and a session-edited section is void. A session that finds the section missing or ambiguous defaults to per-arc authorization — never to inference.

**Per arc (per brief)** — a "Decision authority" section in every dispatch brief (template requirements in `Dispatch.md`) classifying the arc's foreseeable choices as **pre-authorized** (proceed and log), **consult** (run the protocol below), or **hold** (owner only). It also states the guardrail-routing rule — which executor safeguards-flagged work reroutes to — so the executor can verify the routing is owner-directed rather than peer-improvised.

## Consult Protocol

A consult resolves a decision the brief marks consult, or any situation the brief did not list. Requirements:

- At least one peer independently verifies the load-bearing claims (not just concurs). Concurrence is agreement with a conclusion; verification is opening the artifacts the conclusion rests on.
- The decision, its rationale, and any riders attached to it are logged where the owner will read them (the shepherd's decision log and morning brief).
- The owner question is recorded as OPEN. A consult never closes an owner question by proxy — it decides only that work continues on its merits.
- The record names who wore which hat at decision time, so a coordinator-as-shepherd brokering a consult on its own dispatch is visible as self-review.

The consult-vs-owner test is bounded cost of being wrong — reversibility plus verifiability — not importance. Values questions (what the product promises) stay with the owner unless a committed project stance settles them.

*Illustration (2026-09-05):* a proceed-overnight decision on a re-scoped defect ran this protocol — a second session independently verified the code claims behind the re-scope; riders were attached (the correction leads the morning brief, negative control before the fix, overlap check with sibling work items); the decision and hats were logged; the executor's question to the owner stayed open.

## Defaults: the Unlisted and the Void

- **Unlisted case** — a situation outside the brief's pre-authorized/consult/hold taxonomy escalates to the consult protocol, which may conclude hold. It is never treated as pre-authorized — the unlisted case is exactly where hedging returns. Blanket hold is not the default either; that recreates the overnight stall.
- **Void premise** — when the dispatched objective's premise fails (the defect as dispatched does not exist, the artifact to change is gone), the dispatch is void at that boundary. Re-scoping is a consult, never pre-authorized, and the record is corrected visibly: withdrawn claims stay in the record marked withdrawn, because every earlier reader believed them.

*Illustration (2026-09-05):* the executor found the dispatched defect was a measurement error, stopped at that boundary rather than continuing on the stale brief, corrected the records visibly, and put the re-scope through a consult.

## Two-Hats Rule

Shepherd obligations never lapse while the same session is coordinating. Liveness obligations are kept or explicitly handed off — "you have the watch", acknowledged — never silently dropped. The asymmetry is deliberate: shepherd failures are silent (an unnoticed stall), coordinator failures are eventually noisy.

*Illustration (2026-09-05):* the arc's clean hand-offs were explicit ("the arc is complete and you have the watch"); its one dropped hand-off happened where hats blurred — the executor reported checkpoint close to the shepherd while the coordinator sat on a stale hold. The brief's mandatory "report completion to" line (`Dispatch.md`) plus shepherd verification of the hand-off is the fix.

## Arc Lifecycle

1. **Authorize** — the coordinator locates the standing-authorization section in the project's `project.md`, or obtains per-arc authorization from the owner. No inference.
2. **Brief** — the coordinator writes the dispatch brief per `Dispatch.md`, including "Decision authority" and "report completion to", and subscribes to the executor's idle notices.
3. **Arm the watch** — the shepherd (whichever session holds the hat) subscribes to executor idle notices and starts a fallback heartbeat.
4. **Execute** — the executor runs the brief to a natural gate, escalating per the taxonomy above; stalls draw a shepherd nudge.
5. **Hand off** — the executor reports completion to the named party; the shepherd verifies the hand-off happened.
6. **Report** — the shepherd's decision log and morning brief go where the owner will read them: proxy decisions, riders, open owner questions, corrections — the correction leads.
