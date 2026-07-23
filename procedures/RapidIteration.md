# Rapid Iteration

## Intent

Support work that is *discovered through running the software* rather than
specified up front: exploring an unfamiliar problem, or hardening a tangled
subsystem under repeated testing. The standard pipeline (Plan → Code → Test → …)
assumes the spec precedes the code; rapid iteration is a **loop** for when it does
not.

This procedure names the loop so it is used deliberately, instead of improvising
around the linear pipeline.

## When to Use

- Exploring territory you do not have a strong vision for, or a stack you are not
  fluent in.
- Stabilizing a subsystem where bugs surface only at runtime and interact.
- Any "test it, see what breaks, fix a batch, repeat" cadence.

For well-specified, mechanical work, use the standard pipeline — it is the better
autopilot when requirements are known.

## The Loop

```
test → triage → fix in groups → reflect → document (at group/phase close)
```

Each pass is a **batch, not a pipeline run**. You are not carrying one item end to
end; you are cycling the whole set.

Entry condition: something runnable must already exist. The loop **sustains**
iteration; it does not initiate a project (build a prototype or run `Spike.md` first).

### Steps

1. **Test** — run the software (or have the requester play/use it) and collect
   observations.
2. **Triage** — turn the observations into prioritized, grouped work items with
   root-cause hypotheses and flagged decision points (see `Triage.md`).
3. **Fix in groups** — implement a themed batch. Plan and code together; per-item
   ceremony scales with complexity and risk (a one-line fix needs no `plan.md`).
4. **Reflect** (lightweight, per group) — note what converged, what didn't.
5. **Document at close** — refresh the design/architecture docs at group or phase
   close, not only when drift bites.

## Two Intents (one loop)

The loop skeleton is the same; the intent sets the dials:

- **Exploratory** — discovering *what it should do*. Triage emits design/feature
  items. **Capture decisions at fork points** and write them back to the **design
  doc** (not just commit messages / `code.md`), or the design silently goes stale.
  Ceremony stays light; commit granularity can be per-group.
- **Hardening** — making *what exists* robust. Triage emits defect items. Favor
  **commit per revert-unit** (usually per-WI) so a regression can be bisected and
  backed out cleanly.

## Practices

- **Front-load observability for tangled subsystems.** Trip-condition: *if you
  cannot root-cause from reading the code, or a round does not converge, stop
  fixing and add instruments first* (debug overlays, state readouts, invariant
  assertions). Visualizing state collapses rounds of guessing into one look.
- **Nesting.** A big or tangled work item gets its **own** rapid-iteration loop
  (an umbrella WI planned and hardened as a mini-project), rather than being
  forced into a batch.
- **Scope guard.** The loop is productive and unbounded — it will polish forever.
  Periodically check against the project goal (`ProjectAssessment.md`) so it
  terminates deliberately, not by exhaustion.
- **Capture deferrals.** Out-of-scope and newly discovered issues become work
  items immediately; never lose them to chat.

## Guidance

- Match ceremony to risk, not to habit; over-ceremony on trivial items is its own
  friction.
- The loop is a good scaffold for *capturing* discovery, but it is not a method
  for *doing* discovery — that comes from triage, decision-capture, and
  observability.
- Reflect/Document have two cadences: a quick per-group note, and a fuller
  `Reflect.md` + `Document.md` pass at phase close.
