# Investigate

## Intent

Answer a specific question about a running system's behavior by examining observability data — traces, logs, metrics, or any other available telemetry. The output is a structured record of the question, methodology, findings, and recommendations. Investigation exists to turn vague symptoms into concrete, actionable understanding.

Investigation is diagnostic. It starts with a question or observation ("what is calling service X with bad input?", "why are error rates elevated?", "where is this latency coming from?") and ends with evidence-backed findings. It is not planning, implementation, or discovery of external products — it is examination of systems the team already operates.

## When to Investigate

- A system is exhibiting unexpected behavior and the cause is unknown
- A specific question about runtime behavior needs an evidence-based answer
- Error rates, latency, or resource consumption have changed and the source needs identification
- A caller, dependency, or data flow needs to be traced through a distributed system
- Any time the question is "what is actually happening?" rather than "what should we build?"

Investigation may be prompted by an alert, a support request, a hunch, or idle curiosity about system behavior. The trigger does not matter — the process is the same.

## Document Storage & Naming

Investigation documents live inside a ticket folder when one exists, or standalone when investigation is ad hoc:

- `docs/pending/12-diagnose-high-error-rate/investigate.md`
- `docs/pending/PROJ-456-elevated-error-rate/investigate.md`

The presence of `investigate.md` in a folder indicates that investigation has been conducted. A folder may contain `investigate.md` alongside `ticket.md` when investigation was prompted by a ticket, or `investigate.md` alone when the investigation preceded or replaced a ticket.

## Procedure

### 1. Establish the Question

State clearly what is being investigated and why. A good investigation question is specific enough to guide the search but open enough to follow unexpected leads.

If the question is vague, refine it with the human before investing significant effort. "The system is slow" is a starting point, not an investigation question. "Which upstream callers are contributing to elevated p99 latency on service X?" is.

### 2. Investigate

Use available observability tools and data sources to answer the question. This may include:

- Distributed traces — following requests across service boundaries
- Logs — searching for error messages, patterns, or correlating events
- Metrics — identifying rate changes, anomalies, or resource pressure
- Service topology — understanding caller/callee relationships
- Any other available telemetry or tooling

Follow the evidence. Investigation is not a checklist — pursue what the data reveals, adjust the approach as findings emerge, and go deeper where the signal is strong. Spend more time on promising leads, less on dead ends.

Document the methodology as you go — what was queried, what filters were applied, what time windows were examined. This makes findings reproducible and allows others to verify or extend the investigation.

### 3. Verify Evidence

Before writing findings, verify the evidence meets the threshold for the claims you intend to make. Follow the rules in `guidelines/Evidence.md`. The key checks:

- **Baseline comparison**: For any metric claimed to be abnormal, confirm what the metric looked like *before* the event under investigation. If the before and after values are similar, the metric is not evidence — regardless of how large the absolute values look.
- **Visual verification**: For any metric-based finding that claims a pattern, trend, or anomaly, generate a visual (chart link, dashboard view) and verify it before writing the finding. Include the visual reference in the document. If you cannot produce a visual, flag the finding explicitly as unverified.
- **Evidence reliability**: Apply the evidence-type rules from `guidelines/Evidence.md` — understand what each type of evidence can and cannot prove (e.g., log absence ≠ event absence; metric absence ≠ normal operation; a single decisive log may be sufficient).
- **Time window adequacy**: Confirm the observation window covers the relevant period, includes baseline, and spans enough cycles for periodic phenomena.
- **Confirmation bias check**: Before concluding a hypothesis is confirmed, actively look for evidence that contradicts it. If the first signal you checked seemed to confirm the hypothesis, check at least two more independent signals.

This step is not optional. Findings that skip verification must be labeled "Hypothesis" or "Unverified."

### 4. Assess Findings

For each significant finding, evaluate:

- What does the evidence show? State facts before interpretations.
- How confident is the conclusion? Use the confidence labels from `guidelines/Evidence.md`:
  - **Confirmed** = visually verified + before/after comparison, or corroborated by multiple independent signals
  - **Supported** = consistent with hypothesis, backed by data, not independently confirmed
  - **Hypothesis** = plausible, not tested against alternatives or visually verified
  - **Inconclusive** = evidence examined, does not clearly support or refute
- What is the scope and impact? Quantify where possible (error counts, affected callers, time windows).
- What remains unknown or uncertain?

### 5. Write the Investigation Document

Produce `investigate.md` with the findings. Structure the document around what was discovered and what it means — not around the chronological steps of discovering it.

If the investigation found nothing abnormal, say so honestly. Document what was checked and what was found normal. This is a valid and useful output — it prevents someone else from repeating the same work. But it is only useful if it is honest about what was checked, what was found, and what remains unknown. Resist the temptation to produce a "root cause" when you don't have one.

## Required Content

Every investigation document must include:

- **Question** — what was investigated, stated as a clear question or problem statement
- **Summary** — a concise answer to the question (a few sentences that convey the essential finding for someone who reads nothing else)
- **Methodology** — how the investigation was conducted: what data sources were used, what time window was examined, what approach was taken to identify the findings. Enough detail that someone could reproduce or extend the investigation.
- **Findings** — detailed, evidence-backed account of what was discovered. Organize by significance or topic, not by the order things were found. Include specifics: service names, error counts, trace IDs, duration patterns, log messages — whatever supports the conclusions. Every finding must carry a confidence label.

## Optional Content

Include when relevant, omit when not:

- **Recommendations** — suggested next steps based on the findings. These may be fixes, further investigation, tickets to create, or a decision that no action is needed.
- **Open Questions** — specific unknowns that the investigation could not resolve and may warrant follow-up
- **Scope & Limitations** — constraints that affected the investigation (limited time window, missing telemetry, services not instrumented, tool limitations such as summary-only statistics) if they materially affect confidence in the findings
- **What Was Checked and Found Normal** — for inconclusive investigations, a structured record of metrics/logs/traces examined and their observed state, so future investigators don't repeat the same checks

## Guidance

- **State the answer early.** The Summary section should give the reader the essential finding without requiring them to read the full document. Details follow for those who need them.
- **Never fabricate context not present in the source data.** If a detail — a channel name, a username, a timestamp, a service name — was not returned by an observability tool or explicitly stated by the human, do not invent it. If the detail matters for the document (e.g. "reported via Slack"), record only what is known and leave the rest blank or marked as unknown. A plausible-sounding fabrication is worse than an explicit gap.
- **Be specific.** "Several services are making bad calls" is less useful than "service-x accounts for ~75% of requests with parameter-id=0 traffic (1,075 error traces in 6 hours), followed by service-y (178) and service-z (75)."
- **Separate evidence from interpretation.** State what the data shows, then state what you conclude from it — clearly distinguished.
- **Quantify where possible.** Counts, rates, percentages, and time windows make findings concrete and actionable. Relative comparisons ("most of the errors" vs "75% of the errors") lose information.
- **Record methodology so the investigation is reproducible.** Another person (or AI) should be able to re-run the same queries to verify findings or check whether the situation has changed.
- **Investigation may answer the original question and raise new ones.** Note new questions explicitly rather than leaving them implicit in the findings.
- **Not every investigation leads to action.** Sometimes the answer is "this is expected behavior" or "the impact is negligible." That is a valid and useful finding.
- **Follow `guidelines/Evidence.md`.** The evidence assessment rules apply to all investigations. They are not suggestions — they are the standard for what counts as verified evidence versus hypothesis.