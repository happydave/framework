# AI Adaptations for Debugging

This document adapts traditional debugging methodologies for use by AI agents, specifically focusing on systematic diagnosis and overcoming cognitive biases. It complements `Investigate.md` (data collection procedures) with reasoning principles for how to interpret that data.

**When to apply:** During the **Implement** phase when bugs surface, or during an **Investigate** action when runtime behavior needs deeper analysis.

## Cross-Reference with Other Guidelines

| Document | Role |
|---|---|
| `Discover.md` | Pre-planning investigation of products or technologies |
| `Investigate.md` | Step-by-step procedures for collecting observability data |
| `Evidence.md` | Rules for assessing the quality and reliability of evidence |
| **`Debug.md`** (this file) | AI-specific reasoning methods for interpreting evidence and generating hypotheses |

## 1. Structured Hypothesis Generation

AI agents should not just "try a fix." They must formalize their reasoning before editing code.

-   **Requirement**: Before any code change, state the hypothesis in the terminal, the implementation log, or a `debug.md` file.
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

Per `guidelines/Evidence.md`, agents are prone to finding what they expect.

-   **Human-in-the-loop Point**: Human judgment is REQUIRED when:
    -   The agent claims a root cause based on "lack of logs" (Log absence is not definitive).
    -   The agent proposes a fix that "should work" but hasn't been verified with a passing test.
    -   The agent is stuck in a loop of 3+ unsuccessful attempts at the same bug.
-   **Verification Gate**: For any finding labeled **Confirmed**, the agent must provide a "Before" and "After" log snippet or screenshot link showing the transition from failure to success.

## 4. Self-Refinement Loop (Self-Refine)

Before finalizing a fix, the agent should "critique" its own solution.

-   **Procedure**:
    1.  Propose the fix.
    2.  Ask: "What side effects could this change have on the rest of the system?"
    3.  Ask: "Is this the simplest way to fix the root cause, or am I just masking a symptom?"
    4.  Adjust the fix based on this internal critique.

## 5. Surprise Analysis & Assumption Proofing

When a prediction fails or a result contradicts the current mental model, the agent must pause to re-baseline. The level of rigor applied should be proportional to the severity of the failure.

- **Protocol**:
    1. **Gap Analysis**: Explicitly document the `Expected Result` vs. `Observed Result`.
    2. **Assumption Inventory**: Enumerate all assumptions that supported the failed expectation (e.g., "Assumed the environment variable was set," "Assumed the function returned a Promise").
    3. **Direct Proofs**: Systematically verify each assumption with a targeted test, code inspection, log statement, or debugger inspection.
    4. **Log Results**: Document the outcome of these proofs before formulating the next hypothesis.
- **Persistence**: For significant failures or persistent issues, record this analysis in a `debug.md` file within the current work item or investigation folder to preserve the reasoning trail without cluttering the primary log (`implementation.md` or `investigate.md`).
