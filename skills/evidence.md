---
name: evidence
description: Evidence assessment and confidence labeling framework for any empirical claim
---
# Evidence Assessment

Rules for evaluating the reliability and decisiveness of evidence before making a claim. The core
principles below apply to **any empirical claim** — a runtime investigation, a spike measurement, a
test result, a review finding, a survey statement in a plan. The framework was first written for
observability data (logs, metrics, traces) and those specializations still live here in the
**Observability-specific** section and its sub-files, but the general principles are not restricted to
telemetry: a generated artifact, a benchmark, a wall-clock, and a document are all evidence, and all of
them can be reported with more confidence than they earn.

## Core Principles (general)

### Uncertainty Must Be Visible
Confidence labels reflect the strength of the **evidence**, not the appeal of the narrative.

| Label | Meaning |
|---|---|
| **Confirmed** | Directly verified (inspected the artifact) OR corroborated by multiple independent signals |
| **Supported** | Consistent with the hypothesis and from a reliable source, but not independently confirmed |
| **Hypothesis** | Plausible explanation that has not been tested or directly verified |
| **Inconclusive** | Evidence examined but does not clearly support or refute the hypothesis |

State the label with the claim. A confident sentence with no evidence behind it is a hypothesis
wearing a conclusion's clothes.

### Verify the Artifact, Not Only Its Summary
Summary statistics cannot reveal patterns, inflection points, or whether a thing is actually right.
An interpretation drawn from summary numbers remains a **hypothesis until the artifact itself is
examined**.

- For a metric-based claim about a pattern or trend: confirm it against the time-series, not the
  min/max/avg. (See Observability-specific.)
- For a **produced artifact**: inspect it directly. A generated video with the exact requested frame
  count, codec, and duration can be visually broken; a timeline with well-formed spans can be
  mis-aligned to the audio; a document that passes a link check can still say the wrong thing. Green
  automated metrics are necessary, not sufficient — **look at the thing** before trusting the numbers.
- If you cannot examine the artifact, flag the finding as **unverified** rather than stating it as
  fact.

### A Claim Carries the Task It Was Measured On
A quantitative result is evidence *for the task it was measured on*, and does not automatically
transfer to a different task that merely resembles it. Before reusing a number — your own or one from a
document, paper, or vendor — check that the original task matches the task at hand.

- A word-error-rate measured for **transcription** does not bound the accuracy of **forced alignment
  of known text**, where a mis-heard word costs one token rather than a wrong output.
- A benchmark on one model tier, hardware, resolution, or input distribution is not a measurement of
  another.

A precise number applied to the wrong task is more dangerous than vagueness: it looks authoritative and
propagates silently. When a claim is inherited across a task boundary, label it **Hypothesis** until
re-measured on the actual task.

### Do Not Diagnose From an In-Progress Symptom
While a process is still running, its intermediate state is an **observation, not a conclusion**. A
quiet log, low GPU or CPU utilisation, a stalled progress bar, a not-yet-written output file — none of
these is a diagnosis. Wait for the run's own terminal report (exit status, final log line, completed
artifact) before naming a cause or asking anyone to act on it.

Reporting a diagnosis from a mid-run symptom produces retractions: "it failed to load" when it was
still loading, "the queue is wedged, restart it" when the interrupt was merely slow to take effect.
The correct move while a run is live is to keep observing and to say explicitly that the run is still
in progress — never to convert a symptom into a settled cause.

### "Nothing Found" Is a Valid Output
Resist the temptation to produce a "root cause" or a positive result without evidence. Documenting what
was checked and found to be normal — or that an approach did **not** work, and why — is a real result.
A negative finding retires uncertainty exactly as a positive one does.

### Guard Against Confirmation Bias
1. Ask: "What would this look like if my hypothesis were wrong?"
2. Actively seek contradictory evidence — a control that *should* fail, an independent signal that must
   corroborate, a repeated structure that should self-agree.
3. Check at least two independent signals before labeling a finding **Confirmed**.
4. Separate data collection from interpretation — gather first, conclude second.
5. If the first signal you checked seemed to confirm the hypothesis, that is when to look hardest for
   the disconfirming one.

## Observability-specific

These rules specialize the general principles for telemetry (logs, metrics, traces). They do not apply
outside that domain — a documentation task or a generated-asset spike has no "historical baseline" to
compare against, and telling it to find one is noise.

### Baseline Before Judgment
Before claiming a metric or pattern is abnormal, compare it to its own historical baseline. Absolute
values without context are meaningless.
- Investigate the metric's state *before* the event.
- If baseline data is unavailable, state this as a limitation.

### Time Window Considerations
- **Baseline inclusion**: the window must start before the event.
- **Clock skew**: account for seconds/minutes of disagreement in distributed systems.
- **Periodicity**: observation must span 2–3 full cycles of a suspected periodic phenomenon.

### Specific Evidence Guidelines
For detailed rules on specific telemetry types:
- [Logs Evidence](evidence/Logs.md)
- [Metrics Evidence](evidence/Metrics.md)
- [Groundcover & Traces](evidence/Groundcover.md)

## Usage

Reference this document wherever a claim must be defended by evidence:
- **Investigate** and **Discover** — findings about systems and domains.
- **Spike** — the falsifiable check, the confidence labels, and "verify the artifact" and "a claim
  carries its task".
- **WebResearch** — the evidence standard for harvested replies.
- **Plan** — survey claims about existing code/data carry a confidence label; a claim inherited across
  a task boundary is a Hypothesis until re-measured.
- **Code**, **Test**, **CodeReview** — a result that passes automated metrics is not verified until the
  artifact behind it is examined; report outcomes at the confidence the evidence supports.
