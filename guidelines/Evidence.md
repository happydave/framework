# Evidence Assessment

Rules for evaluating the reliability and decisiveness of evidence during investigation. These apply to any observability data — logs, metrics, traces, or other telemetry — regardless of the specific tooling.

## Core Principles

### Baseline Before Judgment

Before claiming a metric or pattern is abnormal, compare it to its own historical baseline. Absolute values without context are meaningless. A 40-second checkpoint that has been 40 seconds for months is not a finding. A checkpoint that jumped from 5 seconds to 40 seconds at a specific point in time is.

For any metric claimed to be abnormal, the investigation must show what the metric looked like *before* the event or change under investigation. If baseline data is unavailable, state this as a limitation — do not paper over it.

### Visual Verification

Summary statistics (min, max, first, last, avg) cannot reveal patterns, trends, periodicity, spikes, or inflection points. When an investigation tool returns summary data rather than a full time series, treat interpretations as hypotheses until confirmed visually.

For any finding that claims a pattern, trend, or anomaly in metric data: generate a visual (chart link, dashboard screenshot, or equivalent) **before writing the finding**. Include the visual reference in the document. If you cannot produce a visual, flag the finding explicitly as "unverified — based on summary statistics only."

### Uncertainty Must Be Visible

Confidence labels reflect the strength of the **evidence**, not the strength of the **argument**. A well-structured narrative built on unverified data is not a high-confidence finding.

Definitions:

| Label | Meaning |
|---|---|
| **Confirmed** | Visually verified via time-series chart with clear before/after contrast, OR corroborated by multiple independent signals |
| **Supported** | Consistent with hypothesis and backed by data, but not independently confirmed via visual or second signal |
| **Hypothesis** | Plausible explanation that has not been tested against alternatives or visually verified |
| **Inconclusive** | Evidence examined but does not clearly support or refute the hypothesis |

The rougher the data, the rougher the report should read. Uncertainty should be visible in the document's tone and structure, not hidden behind formatting and polish. Fluency is not accuracy — a polished table of numbers with confident labels is persuasive precisely because it *looks* like evidence. That makes unverified polish actively harmful.

### "Nothing Found" Is a Valid Output

An investigation that checks all available signals and finds nothing abnormal is genuinely useful — it prevents someone else from repeating the same work. But it is only useful if it is honest about what was checked, what was found, and what remains unknown. Resist the temptation to produce a "root cause" when you don't have one.

## Evidence Types and Reliability

### Logs

**A single decisive log can be sufficient evidence.** If a log message explicitly records the event under investigation (e.g., an error message with a stack trace, a state transition log, a rejection reason), that log entry alone may answer the question. Not everything requires corroboration — sometimes one log says exactly what happened.

**Log absence is never definitive.** Logs get lost. They are dropped by buffering, sampling, rate limiting, and ingestion failures. The absence of an expected log entry is worth noting but never proves the event didn't happen. Frame it as: "No log found for X in the examined window" — not "X did not occur."

**Reduced log volume requires comparative analysis.** If an investigation observes fewer logs than expected, this could mean the events genuinely decreased OR that logs are being lost. To distinguish:
- Compare against a known-good baseline period
- Check for evidence of log dropping (ingestion errors, pipeline metrics, gaps in otherwise continuous streams)
- If log dropping cannot be ruled out, state the ambiguity explicitly

### Metrics

**Metric absence is never definitive.** Like logs, metrics can be lost — scrape failures, exporter crashes, network partitions, retention expiry. The absence of a metric or a gap in a time series is worth noting but does not prove the underlying system stopped doing the thing the metric measures. Check exporter health (`up` metric, scrape targets) before drawing conclusions from metric absence.

**Stuck metrics may indicate reporting failure.** A metric that shows absolutely no change over a period where change is expected (e.g., a counter that should increment, a gauge that normally oscillates) may indicate the exporter or reporter has stalled rather than that the measured quantity is truly static. This is especially suspect for metrics known to vary continuously. Investigate the reporter's health before trusting a flatlined metric.

**Non-zero values can be decisive when zero is expected.** Some metrics are expected to be zero under normal operation (rejected connections, assertion counts, error counters for specific categories). A non-zero value in these metrics is immediate, high-confidence evidence that the condition occurred. These are among the most reliable signals available.

### Traces

**Traces are sampled.** Most distributed tracing systems sample rather than capture every request. The absence of error traces does not mean errors didn't occur. The presence of error traces is reliable evidence that errors did occur. Quantitative conclusions from trace counts should account for the sampling rate.

## Time Window Considerations

**Every piece of evidence has a time dimension.** When assessing any evidence:

- **Confirm the evidence falls within the relevant time window.** A log from Tuesday doesn't explain a Wednesday incident.
- **Confirm the time window is wide enough.** A 5-minute window may miss a 30-minute periodic pattern.
- **Confirm the time window includes baseline.** A window that starts after the event began cannot establish what "normal" looked like.
- **Account for clock skew.** Distributed systems may have clocks that disagree by seconds or minutes. Don't assume timestamps from different sources are perfectly synchronized.
- **Be explicit about the window examined.** Every finding should state the time range it covers so a reader can judge whether it's sufficient.

For periodic phenomena, the observation window must span at least 2–3 full cycles of the suspected period. For change-related investigation (upgrade, deployment, config change), the window must include meaningful time before and after the change.

## Confirmation Bias

The most common failure mode in investigation is finding what you're looking for and stopping. When you arrive with a hypothesis and find the first piece of evidence that fits, the temptation to declare the hypothesis confirmed is strong.

Defenses:

1. **Before interpreting a metric as abnormal, ask: "What did this look like before the event?"** This is mandatory, not optional.
2. **Actively look for evidence that contradicts the hypothesis**, not just evidence that supports it.
3. **If the first metric you check seems to confirm the hypothesis, check at least two more independent signals** before writing a confirmed finding.
4. **Separate data collection from interpretation.** Gather the data first, then assess what it shows — don't interleave "querying" and "concluding."

## Verification Checkpoints

Build explicit verification into the investigation process rather than producing conclusions and only checking them when challenged:

1. **After initial metric collection**: Generate visual links for key metrics. Review them (or have the human review them) before proceeding to interpretation.
2. **Before writing findings**: For each finding that will be labeled above "Hypothesis", confirm it meets the evidence threshold for that label.
3. **Before finalizing the document**: Ask "If someone showed me this evidence cold, without the narrative, would I reach the same conclusion?" If the answer is "maybe not", the narrative is doing too much work and the evidence too little.