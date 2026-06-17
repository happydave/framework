# Triage

## Intent

Convert an unstructured dump — playtest findings, a bug report batch, a feature
wishlist, a block of user feedback — into discrete, prioritized work items, each
with a root-cause hypothesis (for defects) or a clear intent (for features), and
with any human-decision points flagged explicitly.

Triage is the connective tissue of the rapid-iteration loop (see
`RapidIteration.md`). The quality of everything downstream — planning, fixing,
sequencing — is inherited from the quality of triage. It is the highest-leverage
step when work arrives as a pile rather than a spec.

## When to Use

- After a test/playtest produces a list of observations.
- When the requester hands over a batch of mixed feedback ("a few things…").
- Whenever incoming work is larger than one obvious change and not already broken
  into work items.

Do NOT use Triage for a single, already-scoped request — just do the work.

## Procedure

### 1. Itemize

Split the dump into atomic items. One symptom or one desired behavior per item.
Resist bundling unrelated things "because they were reported together."

### 2. Classify each item

- **Defect** (something is wrong) → hardening intent.
- **Design/feature** (something should exist or behave differently) → exploratory
  intent.
- **Confirmation / non-issue** → record and drop (no work item).

### 3. Hypothesize and locate

For each defect, write a one-line **root-cause hypothesis** grounded in the code
(read enough to ground it; do not guess blindly). For each feature, write a
one-line **intent**. If a defect cannot be root-caused from reading, mark it
"needs repro/investigation" rather than inventing a fix.

### 4. Flag decision points

Mark every item that hides a choice only the requester can make (a behavior
trade-off, a mechanism with options, a scope call). These become explicit
questions, not silent assumptions. Decision points are surfaced before fixing,
not discovered mid-implementation.

### 5. Prioritize and group

- Severity first: asset loss / data loss / blocking bugs lead; cosmetic last.
- Group related items by **theme** (shared subsystem or shared root cause).
- Note complexity/scope. A big or tangled item gets its **own loop** rather than
  being squeezed into the batch (see nesting in `RapidIteration.md`).

### 6. Emit work items

Create a work item per item (or per tightly-coupled cluster), carrying the
hypothesis/intent, severity, and any flagged decisions. Record items deliberately
deferred or out of scope as work items too — do not lose them.

## Output

A prioritized, grouped set of work items with:
- root-cause hypothesis (defect) or intent (feature),
- severity/priority,
- flagged human-decision points,
- intent tag (hardening vs exploratory) to drive ceremony in the loop.

## Guidance

- Ground hypotheses in the code; an unrooted "fix" wastes a round.
- Separate "destroys/loses something" from "looks wrong" — they have different
  urgency and different fixes.
- Confirmations are signal too: record what is verified working so the loop can
  converge.
- Surface decision points up front; mid-fix discovery causes rework.
