# Spike

## Intent

Answer one feasibility, cost, or design question by building the smallest throwaway thing that
produces a decisive result. A spike exists to **retire a risk or settle a decision** before committing
to a plan — not to deliver production work. Its output is a verdict backed by evidence, captured in a
`spike.md`.

A spike is deliberately sized between a SideQuest and the full Work Item pipeline:

- A **SideQuest** is a chore with negligible risk and no design question — it needs no plan and reaches
  for a result directly. A spike has a real question whose *framing* matters: a poorly-designed spike
  measures the wrong thing convincingly, which is worse than measuring nothing.
- The **full pipeline** (Plan → PlanReview → Code → CodeReview → Test → Document → Reflect) delivers
  production work through independent quality gates. A spike answers a question and is then thrown away
  or promoted; running eight artifacts to produce one number is friction without payoff.

Spike sits between them: a short **Design** written before building, a single execution-and-findings
artifact, and a Reflect. Two documents, not eight.

## When to Spike

- A feasibility question that a local experiment can settle ("does X run on this hardware?", "can we
  read Y out of Z?", "is A accurate enough to drive B?").
- A cost or performance measurement needed before planning ("how long does one of these take?").
- A choice between approaches where a small experiment beats argument.
- De-risking the critical path of a larger project before decomposing it.

A spike often **follows a Discover** and precedes a Plan: Discover builds understanding from existing
sources (docs, source, prior art); a spike produces a *measured verdict* from a throwaway build. The
two compose — a Discover may end by naming the spikes that would settle its open questions. Do not
force a bright line between them; if you are reading source to understand it, that is Discover, and if
you are running something to measure it, that is Spike, and one activity may do both.

Do NOT use Spike for:
- Production work intended to ship (use `Plan` → `Code`).
- A trivial chore with no question to answer (use `SideQuest`).
- Diagnosing a running production system (use `Investigate`).
- Understanding a product or domain from existing sources with no build (use `Discover`).

## Document Storage & Naming

A spike lives in a work item folder under `docs/pending/`:

- `docs/pending/<id>-<name>/workitem.md` — the question and its context (prerequisite).
- `docs/pending/<id>-<name>/spike.md` — the Design, the execution, the findings, the verdict, and a
  brief Reflect. This single artifact replaces the pipeline's `plan.md` / `code.md` / `codereview.md`
  / `test.md` / `document.md` / `reflect.md`.

A spike that produces reusable artifacts (a prototype, a findings entry in a research repo) stores
those where that repo's conventions put them; `spike.md` links to them.

## Procedure

### 1. Prerequisite: Work Item

A spike begins with a `workitem.md` capturing the question and any stated constraints.

### 2. Design (write this before building)

Write the **Design** section of `spike.md` first. It is short — a few lines each — but every field is
load-bearing, and skipping it is how a spike ends up measuring the wrong thing:

- **Decision** — the specific choice or risk this spike unblocks. Not "explore X" but "decide whether
  to build the pipeline on X or Y", "confirm X is fast enough to use per-shot". If you cannot name the
  decision, you are not ready to spike.
- **Stopping rule** — what result ends the spike. A spike's job is a *decision*, not a precise
  measurement: **stop when the decision is determined, not when the number is polished.** Once the
  evidence flips (or confirms) the decision, further precision is waste. *(This rule is gated — see the
  ordering note in step 3.)*
- **Baseline** — if a prior approach or a prior spike already produced a result, name it. Where a
  baseline exists, this spike is a **challenger**: it is worth adopting only if it beats the baseline
  on an axis that matters, and "more principled" is not such an axis. State the axis.
- **Falsifiable check** — name, in advance, at least one observation that would show the result is
  *wrong*. A spike that can only confirm its own hypothesis has not been designed. (A repeated
  structure that should self-agree; a control run that *should* fail; an independent signal that must
  corroborate.) Deciding this before you see the result is what keeps it honest.
- **Premises to verify** — any concrete claim about existing code, data, or tooling that the spike
  will build on must be confirmed against the actual artifact *before* building, not from memory or
  documentation. (A shipped workflow may be wrapped and hide steps; an installed tool may be a
  version behind; a model list is not a model graph.) This is the one rule imported wholesale from
  `Plan.md`'s open-and-verify discipline, because it is the cheapest defect to prevent and the most
  expensive to discover mid-run.

For a high-stakes or expensive spike, review the Design before executing. This can be inline — a short
adversarial pass over your own Design in the same session, asking what it would measure that is *not*
the decision, which premise is assumed rather than verified, and what result the falsifiable check
could not catch. The intent and focus of writing the Design down is itself a filter: several defects
in this framework's own spikes were caught at Design, not execution.

### 3. Execute

Build the smallest thing that produces the result, and gather evidence. Apply `skills/evidence.md` —
its confidence labels (Confirmed / Supported / Hypothesis / Inconclusive), its rule that uncertainty
must stay visible, and specifically:

- **Run the falsifiable check from the Design, and inspect the artifact directly — not only its
  metrics.** A result can pass every automated measure and still be wrong: a generated video with the
  exact requested frame count and codec can be visually broken; a timeline with well-formed spans can
  be mis-aligned. **Look at the thing** (`[agent]`-level verification, per `Plan.md`) before trusting
  the numbers.
- **Ordering (this guards the stopping rule).** The stopping rule in the Design lets you stop
  *refining a measurement* once the decision is settled. It does **not** license stopping before the
  falsifiable check has run and the artifact has been inspected. Verify first; stop refining second. An
  agent that invokes "the decision is determined" to skip inspection has misused the rule.
- **Do not diagnose from an in-progress symptom.** While a run is live, a quiet log or low resource
  use is an *observation*, not a conclusion; wait for the run's own terminal report before naming a
  cause. (See `skills/evidence.md`.)

Record what was done and what was observed in `spike.md` as you go.

### 4. Verdict

State the answer to the Decision plainly, at the confidence the evidence supports. **A negative or
null result is a successful spike** — "X does not work on this hardware, because <root cause>" or "the
new approach does not beat the baseline" retires the risk exactly as a positive result does, and is
recorded as success, not failure. If the spike revealed the decision was mis-framed, say so and name
the better question.

### 5. Reflect

Close `spike.md` with a brief Reflect (a section, not a separate file). Follow `Reflect.md`'s intent:
what the spike got right, what it got wrong, and any concrete recommendation it feeds back — to a
downstream work item, to the framework, or to a follow-up spike. A spike frequently surfaces a finding
larger than its own question (a shared-infrastructure problem, a wrong assumption in a prior document);
capture it here and route it, do not bury it.

### 6. Completion

When the verdict and Reflect are written, set the work item's `status` to `complete`. A spike is done
when the decision is answered — not when the thing it built is production-ready, which it never is.

## The `spike.md` Template

```markdown
# Spike: <Work Item Title>

## Design
- **Decision:** <the choice/risk this unblocks>
- **Stopping rule:** <what result ends the spike>
- **Baseline:** <prior result to beat, or "none">
- **Falsifiable check:** <an observation that would show the result is wrong>
- **Premises to verify:** <claims about existing artifacts, confirmed before building>

## Execution
<!-- What was built and run, what was observed, with confidence labels. Include the
     falsifiable check and the direct artifact inspection, not only metrics. -->

## Verdict
<!-- The answer to the Decision, at the confidence the evidence supports. A negative
     result is a success. Name a better question if the decision was mis-framed. -->

## Reflect
<!-- Brief: what went right/wrong, and any recommendation routed onward. -->
```

## Guidance

- **The verdict is the deliverable, not the artifact.** The prototype is scaffolding; throw it away or
  promote it deliberately through a real Plan. Do not let a spike's throwaway code accrete into
  production by default.
- **Design before build is the highest-leverage step.** It is short, and it is where the wrong-thing-
  measured-convincingly failure is caught.
- **Match effort to the decision, not to the curiosity.** Stop when the decision is determined.
- **Promotion path.** If a spike says "yes, build it", the follow-up is a normal `Plan` (informed by
  the spike), not an extension of the spike.
