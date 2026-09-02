# WebResearch

## Intent

Package a **single-shot research brief** for a web-enabled AI research session, and harvest its
reply back into the workflow. The researcher session has web access but **no filesystem access and
no conversational follow-up** — everything it needs must be inlined in one prompt, and everything it
returns must arrive in one reply.

WebResearch is the external-landscape counterpart to `Dispatch.md`: Dispatch hands a workflow
procedure to an agent that can read the repo; WebResearch hands *questions* to a researcher that
can read the web. Two transports execute a round; both consume the same brief and produce the same
verbatim-archived reply:

- **The `researcher` subagent** (`agents/researcher.md`, linked at `~/.claude/agents/`) — the
  default. Tool-restricted to WebSearch/WebFetch only, so injected web content cannot reach files
  or shell and raw pages never enter the orchestrating session's context; its prompt bakes in this
  procedure's evidence labels. The orchestrating session passes the brief as the task prompt and
  archives the reply itself.
- **An external web-enabled AI session** via human copy-paste — exactly two operations per round
  (brief into the session, reply into a file). Use when a round warrants a heavier researcher than
  the subagent, or when no subagent runtime is available.

Either way the researcher has no filesystem access and no conversational follow-up — everything it
needs must be inlined in one prompt, and everything it returns must arrive in one reply, so the
procedure minimizes mid-round back-and-forth by design.

## When to use WebResearch

- External landscape work inside a `Discover` (or `Design`): vendor/pricing/ToS surveys, licensing
  reads, prior-art scans, library liveness checks.
- Questions where currency matters (licenses, pricing, maintenance status shift under you) and the
  answer must carry citations.

Do NOT use WebResearch for:
- Anything answerable from local repos or docs (read them directly).
- Feasibility questions better settled by a local spike (run `Spike.md` instead).
- Multi-turn exploratory chat with a researcher — the single-reply contract is the point.

## Briefing & Result Storage

- **Brief**: `docs/pending/<id>-<desc>/briefs/web-research-<topic>-brief.md` — the audit trail of
  what was asked.
- **Reply**: archived **verbatim** at `docs/projects/<project>/research/web-research-<topic>.md`,
  with a provenance header prepended after pasting.
- Multi-round series keep running lessons in `briefs/process-notes.md`.
- **An archive produced without a brief** — an external session's reply pasted directly, or a
  research record written before this procedure existed — still gets the provenance blockquote
  (§6) naming its transport and date; where neither is recorded, say so in the blockquote (the
  codex anchors such an archive as `webresearch-unrecorded-transport`). A dated, attributed
  archive is what lets a later harvest stamp `verified` honestly.

## Procedure

### 1. Frame

**Consult the codex first.** Before commissioning new research, search the codex tenant of the
lore vault (`~/Documents/projects/lore/universes/codex/` — `lore search`/`resolve` from that
repo, e.g. `go run ./cmd/lore search --vault universes --universe codex <term>`; registering
`lore mcp` to make this one call is an **owner step**, not one a session performs) for existing
claims on the subject. A hit enters the brief's context capsule as a **prior finding, with its
confidence, scope, and edition** ("codex, ed. N") — it eliminates or sharpens questions; it does
not replace re-verification of volatile claims at adoption. A hit that is verify-overdue or
scope-displaced is a question generator: fold its re-verification into this round. No coverage?
Say "codex: no prior coverage on <subject>" in the brief — negative consults are recorded so the
archivist sees demand. A brief whose purpose is to re-verify *published* claims follows
`Reverify.md`'s brief shape (per-hypothesis dated verdicts) on top of this procedure.

Identify the **decisions** the research informs, then write the questions. Every question carries a
**working hypothesis** to confirm or refute (and, where useful, what would change your mind).
Hypotheses are what license the researcher to editorialize usefully — to argue rather than survey —
and to volunteer the adjacent thing you didn't ask about.

Split the work into **rounds**: one brief per topic cluster with a distinct evidence temperament
(e.g. adversarial ToS-reading vs. architecture survey vs. dependency health). One round goes deep;
a mega-brief flattens all clusters into generic instructions. Rounds in a series run sequentially so
each capsule can carry the prior rounds' findings forward — this buys free cross-validation when a
later round re-touches an earlier claim.

### 2. Compose the brief

Structure, in order (see the storage section above for worked examples):

1. **Header** (above a horizontal rule; ours, not part of the prompt): round number, transport
   (researcher subagent or external session), generated date, and the exact paste-destination path
   for the reply. Then the rule — everything below it is the prompt, one select-to-end copy.
2. **Opener** — a polite, complete request ("Please provide a thorough, current (<month year>)
   research pass on **<subject>** …"), never a bare imperative, plus an instruction to research
   fresh rather than rely on trained knowledge.
3. **Context capsule** — self-contained prose; the researcher has no access to files, so *inline*
   who we are, what exists, constraints (budget, stack, license bar), and **relevant prior
   findings** (from earlier rounds or earlier discoveries) so the researcher builds on them instead
   of rediscovering them. Curation is the skill: too little yields generic answers, too much buries
   the questions.
4. **The decisions this research informs** — one line each.
5. **Questions** — each with its working hypothesis.
6. **Out of scope** — including what is deliberately left to local spikes (`Spike.md`) or other rounds.
7. **Evidence standard** (below).
8. **Output shape** (below).

### 3. Evidence standard (include in every brief)

- **Primary sources** for anything license/pricing/ToS/status; quote **short operative fragments**
  with links to the full text (not long verbatim passages); if a page is inaccessible, say so
  rather than silently substituting a secondary source.
- **Link every load-bearing claim.**
- **Labels are two-dimensional** — confidence × recency, inline:
  - Confidence: `[CONFIRMED]` (primary source), `[VENDOR-CLAIM]` (vendor marketing — a ceiling),
    `[SECONDARY]` (press/blog), `[SINGLE-SOURCE]`, `[INFERENCE]` (reasoning from evidence).
  - Recency: fresh-verified is the default; `[STABLE-KNOWLEDGE]` for slow-moving material not
    re-checked (may be applied to a whole section collectively, with volatile bits flagged
    individually); `[UNVERIFIED]` / `[UNVERIFIED-this-pass]` for what couldn't be checked.
- **Date volatile claims** ("as of <YYYY-MM>"). For any proposed dependency, require
  **liveness** (last release/commit recency).
- Gaps stated plainly beat smoothed-over ones; findings and opinion stay separate.

### 4. Output shape (include in every brief)

Tell the researcher the reply is archived verbatim and read later by another AI, so:

- **One complete reply**: no clarifying questions (state assumptions and proceed), no offers to
  continue, no references to the conversation.
- **Plain Markdown only**: headings, tables, prose, blockquotes — no ASCII-art diagrams,
  box-drawing, flowcharts, emoji, or images.
- **Single-line table cells**; anything longer goes in prose below the table, referenced by row.
- Structure: `## Bottom line` first, per-question sections, then `## Recommendation (opinion)` and
  `## Gaps and unverified items` last.
- **Tailor table columns to the survey type** (vendor surveys want pricing/API/license columns;
  open-source surveys want `License` + `Liveness (as of <date>)`); name the columns in the brief.

### 5. Execute

Persist the brief, then execute by transport:

- **Researcher subagent (default):** pass everything below the rule as the agent's task prompt,
  then write its reply verbatim to the stated destination file.
- **External session:** the user copies everything below the rule into the researcher session as
  one message, and pastes the reply verbatim into the stated destination file.

### 6. Harvest

- Prepend a **provenance blockquote** to the archived reply: work item, round, link to the brief,
  execution date — and the reply's own self-stated "as of" date when it differs (a researcher
  running past midnight UTC will date its findings tomorrow; the codex stamps claims with the
  "as of" date and the blockquote is where the two are reconciled) — "archived verbatim below."
- **Digest into the requesting document** (e.g. `discover.md` Findings): the archived reply is a
  *source*; the digest carries the load-bearing findings with labels and links back. When the
  requesting document uses `skills/evidence.md` vocabulary, translate: `CONFIRMED` → Confirmed;
  `SECONDARY`/`VENDOR-CLAIM`/`SINGLE-SOURCE` → Supported or Hypothesis per corroboration;
  `INFERENCE` → Hypothesis; conflicting sources → Inconclusive.
- **Cite the codex where it was consulted**: the digesting document records "codex, ed. N" (plus
  the claim's scope/pin where load-bearing) for any codex claims it leaned on — citations are what
  make the archivist's supersession impact sweep able to find consumers. Where a codex topic owns
  the reply's domain, the archived reply is harvest material: a `Harvest.md` work item takes it
  onward through the archivist intake path (`docs/projects/loradel/archivist.md` §1).
- **Grade the brief**, not just the research: did the one-reply discipline hold, were labels/URLs
  used, were hypotheses engaged? Researcher-invented improvements get adopted into the next round's
  brief; slips become tightened instructions. Record lessons in `process-notes.md` for series work.

## Required Content in the Brief Artifact

- **Header**: round/series position, transport, generated date, paste-destination path.
- **The prompt**: everything below the rule, self-contained per steps 2–4.

## Guidance

- The researcher will improve on the spec — good ones push back on instructions and invent label
  refinements. Harvest those improvements into the procedure rather than treating them as
  deviations.
- Prefer thoroughness over brevity in the reply; it is a reference artifact, not a chat answer.
  Say so in the brief.
- A negative result ("nothing combines X and Y") is valuable but is an `[INFERENCE]` from absence —
  expect the researcher to say one pass cannot prove a negative, and treat it accordingly.
- Volatile domains decay: stamp everything, and re-verify at the moment of adoption/integration,
  not just at research time.
