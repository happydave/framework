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

- `docs/pending/12-diagnose-panelid-zero-calls/investigate.md`
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

### 3. Assess Findings

For each significant finding, evaluate:

- What does the evidence show? State facts before interpretations.
- How confident is the conclusion? Distinguish confirmed from inferred.
- What is the scope and impact? Quantify where possible (error counts, affected callers, time windows).
- What remains unknown or uncertain?

### 4. Write the Investigation Document

Produce `investigate.md` with the findings. Structure the document around what was discovered and what it means — not around the chronological steps of discovering it.

## Required Content

Every investigation document must include:

- **Question** — what was investigated, stated as a clear question or problem statement
- **Summary** — a concise answer to the question (a few sentences that convey the essential finding for someone who reads nothing else)
- **Methodology** — how the investigation was conducted: what data sources were used, what time window was examined, what approach was taken to identify the findings. Enough detail that someone could reproduce or extend the investigation.
- **Findings** — detailed, evidence-backed account of what was discovered. Organize by significance or topic, not by the order things were found. Include specifics: service names, error counts, trace IDs, duration patterns, log messages — whatever supports the conclusions.

## Optional Content

Include when relevant, omit when not:

- **Recommendations** — suggested next steps based on the findings. These may be fixes, further investigation, tickets to create, or a decision that no action is needed.
- **Open Questions** — specific unknowns that the investigation could not resolve and may warrant follow-up
- **Scope & Limitations** — constraints that affected the investigation (limited time window, missing telemetry, services not instrumented, etc.) if they materially affect confidence in the findings

## Guidance

- State the answer early. The Summary section should give the reader the essential finding without requiring them to read the full document. Details follow for those who need them.
- Be specific. "Several services are making bad calls" is less useful than "portal-nebo accounts for ~75% of panelId=0 traffic (1,075 error traces in 6 hours), followed by messagechannels (178) and notificationhandler (75)."
- Separate evidence from interpretation. State what the data shows, then state what you conclude from it — clearly distinguished.
- Quantify where possible. Counts, rates, percentages, and time windows make findings concrete and actionable. Relative comparisons ("most of the errors" vs "75% of the errors") lose information.
- Record methodology so the investigation is reproducible. Another person (or AI) should be able to re-run the same queries to verify findings or check whether the situation has changed.
- Investigation may answer the original question and raise new ones. Note new questions explicitly rather than leaving them implicit in the findings.
- Not every investigation leads to action. Sometimes the answer is "this is expected behavior" or "the impact is negligible." That is a valid and useful finding.
