---
name: debug
description: AI-specific debugging methodology: scientific loop, bias mitigation, verification gates
---
# AI Adaptations for Debugging

This document adapts traditional debugging methodologies for use by AI agents, specifically focusing on systematic diagnosis and overcoming cognitive biases. It complements `Investigate.md` (data collection procedures) with reasoning principles for how to interpret that data.

**When to apply:** During the **Code** phase when bugs surface, or during an **Investigate** action when runtime behavior needs deeper analysis.

## Cross-Reference with Other Guidelines

| Document | Role |
|---|---|
| `Discover.md` | Pre-planning investigation of products or technologies |
| `Investigate.md` | Step-by-step procedures for collecting observability data |
| `skills/evidence.md` | Rules for assessing the quality and reliability of evidence |
| **`Debug.md`** (this file) | AI-specific reasoning methods for interpreting evidence and generating hypotheses |

## 1. The Scientific Debugging Loop (Zeller)

AI agents should not just "try a fix." They must formalize their reasoning using a systematic search rather than a random walk.

-   **Requirement**: Before any code change, state the hypothesis in the terminal, the implementation log, or a `debug.md` file.
-   **Methodology**:
    1.  **Observe**: Capture the failure (logs, test output, screen capture).
    2.  **Hypothesize**: Propose a cause for the failure.
    3.  **Predict**: If the hypothesis is true, what *else* should be true?
    4.  **Experiment**: Modify the code or environment to test the prediction.
    5.  **Verify**: Did the experiment confirm the prediction?
-   **Template**:
    -   **Observed**: "Test `api_timeout` failed with 500 Error."
    -   **Hypothesis**: "The timeout middleware is triggered before the database connection is established."
    -   **Testable Prediction**: "Increasing the timeout to 5000ms will result in a 200 OK."
    -   **Action**: "Update `config.ts` timeout value."

## 2. Chain of Thought (CoT) as a "Mental Trace"

Use the agent's internal reasoning as a rubber-ducking tool.

-   **Technique**: When a bug is complex, the agent should perform a "dry run" of the code in text, line by line, explaining what each variable should hold.
-   **Isolation**: If the dry run behavior differs from the actual logs, the "delta" between the agent's mental model and reality is the location of the bug.

## 3. Overcoming Confirmation Bias

Per `skills/evidence.md`, agents are prone to finding what they expect.

-   **Human-in-the-loop Point**: Human judgment is REQUIRED when:
    -   The agent claims a root cause based on "lack of logs" (Log absence is not definitive).
    -   The agent proposes a fix that "should work" but hasn't been verified with a passing test.
    -   The agent is stuck in a loop of 3+ unsuccessful attempts at the same bug.
-   **Verification Gate**: For any finding labeled **Confirmed**, the agent must provide a "Before" and "After" log snippet or screenshot link showing the transition from failure to success.
-   **Recall is not evidence**: A claim about an artifact's contents — what a function returns, what a config file sets, what a document says — is verified by opening the artifact, not by recollection. A remembered fact is a hypothesis; an opened file is a finding. This bias is strongest where the agent is *most* fluent, because a familiar pattern supplies a plausible answer without the artifact ever being read. `Plan.md` states this as the **Open-and-verify** rule for planning; it applies equally to any claim an agent makes about code it has not just read.
-   **The measuring instrument is a hypothesis too**: When a test or harness reports a defect, the correctness of the test itself is one of the hypotheses — ranked by how recently the instrument was written, not left until last. A freshly written check that reports a product defect is, on priors, about as likely to be reporting its own.
-   **Read the library before writing a rule about it**: When a fix or invariant depends on a third-party library's semantics (what a field means, when a callback fires), read the library's code for that path before committing to the rule. The relevant function is often a dozen lines; two plausible-sounding rules built on a misremembered field have each cost a debugging round.

## 4. Self-Refinement Loop (Self-Refine)

Before finalizing a fix, the agent should "critique" its own solution.

-   **Procedure**:
    1.  Propose the fix.
    2.  Ask: "What side effects could this change have on the rest of the system?"
    3.  Ask: "Is this the simplest way to fix the root cause, or am I just masking a symptom?"
    4.  Adjust the fix based on this internal critique.

## 6. Minimal Reproduction (Delta Debugging)

Reduce the noise to isolate the signal.

1.  **Simplify Input**: Find the smallest input that still causes the failure (e.g., the smallest JSON blob, the shortest string).
2.  **Bisection**: Use `git bisect` or manual binary search to find the exact commit or line change that introduced the failure.
3.  **Isolate Environment**: Remove external dependencies or layers one by one until the failure disappears (or is isolated).

## 7. SRE Troubleshooting (Google)

Focused on stability and root cause analysis in complex systems.

1.  **Stop the Bleeding**: Identify if an immediate mitigation is needed (e.g., revert, disable feature flag) before deep diagnosis.
2.  **Reproduce**: Create a reliable, automated test case that fails every time.
3.  **Examine & Diagnose**: Use logs and metrics to trace the failure from the edge to the source.
4.  **Negative Results**: Explicitly document what was checked and found *normal* to prevent redundant work.

## 8. Observability-Driven Debugging (ODD)

Using internal telemetry to understand behavior.

1.  **Instrumentation First**: Add spans, logs, or attributes *before* trying to fix the bug if current data is insufficient.
2.  **High Cardinality Search**: Filter by specific IDs (request ID, user ID) to see the exact path of a failing transaction.
3.  **Compare Traces**: Look at a "good" trace vs. a "bad" trace to identify the divergence point.
4.  **Price the probe before taking it**: Deep inspection of a process under load perturbs what it measures. Before a goroutine/thread dump of a process at scale, estimate the stop-the-world cost (population × per-frame cost) and decide whether the dump is worth contaminating the run; prefer a dump from a control run, or after the measurement window closes, when the number under measurement is a timing. (Go: a full-stack dump of hundreds of thousands of goroutines stops the world for over a minute, and `pprof` truncates `debug=2` output at 64 MiB.)

## 5. Surprise Analysis & Assumption Proofing

When a prediction fails or a result contradicts the current mental model, the agent must pause to re-baseline. The level of rigor applied should be proportional to the severity of the failure.

- **Protocol**:
    1. **Gap Analysis**: Explicitly document the `Expected Result` vs. `Observed Result`.
    2. **Assumption Inventory**: Enumerate and document all assumptions that supported the failed expectation (e.g., "Assumed the environment variable was set," "Assumed the function returned a Promise").
    3. **Direct Proofs**: Systematically verify each assumption with a targeted test, code inspection, log statement, or debugger inspection.
    4. **Log Results**: Document the outcome of these proofs before formulating the next hypothesis.
- **Persistence**: For significant failures or persistent issues, record this analysis in a `debug.md` file within the current work item or investigation folder to preserve the reasoning trail without cluttering the primary log (`code.md` or `investigate.md`).
