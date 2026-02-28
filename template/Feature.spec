## [Feature Name] - Specification

### Objective
One clear sentence describing the goal and what problem this feature solves. Avoid implementation language; describe user/system outcome only.

---

### Invariants (non-negotiable truths about system behavior or constraints)
- Each invariant must be: provably true from fundamental constraints, contain no unstated assumptions, not implicitly contradict other invariants
- For each invariant below, you may optionally add a brief rationale explaining why it's an invariant rather than an assumption

**Core Invariants (must always hold):**
1. [Invariant statement] — *Rationale: [optional explanation]*

2. [Invariant statement] — *Rationale: [optional explanation]*

**Domain/Context Invariants (true within defined scope):**
1. [Invariant statement] — *Scope limitation: [when this applies or does not apply]*

---

### Functional Requirements (behavioral SHALL statements)
Each requirement must specify: trigger condition, expected behavior, outcome. Use SHALL for mandatory behaviors.

**User-Visible Behaviors:**
1. The system SHALL [exact behavior] when [precise trigger condition], resulting in [observable outcome].

2. The system SHALL [exact behavior] when [precise trigger condition], resulting in [observable outcome].

**Data Requirements:**
1. The system SHALL persist/transform/access data with these properties: [describe what, not how].

2. The system SHALL ensure data consistency by: [describe the guarantee].

**Security & Privacy (if applicable):**
1. The system SHALL restrict access to [resource] to users with [specific authorization level or condition].

2. The system SHALL protect [sensitive data type] through: [mechanism description without implementation details].

---

### Acceptance Scenarios (what constitutes sufficient completeness for human approval)
**Scenario:** [Short title describing the situation]
**Given** [precise initial state/context with all relevant conditions specified]
**When** [exact action or trigger, described descriptively not procedurally]
**Then** [observable outcome that confirms correct behavior]
**And** [optional additional verification point]

*Note: Each scenario should test one coherent aspect of the feature. Focus on what makes this "done" rather than exhaustive testing.*

---

### Edge Cases & Error Handling (required, not optional)
Document expected behavior for all significant exception conditions:

- **[Case name]** — [Precise response without implementation details] — *Impact: [What user sees or what system state results]*
  - ⚠️ **Critical**: [If particularly important for correctness, explain why]

---

### Non-Functional Requirements (performance, scalability, constraints)
Document requirements that constrain how the feature behaves but don't describe specific behaviors:

**Performance:**
- [Requirement description] — *Rationale: [User need or technical constraint]*

**Scalability:**
- [How behavior changes at scale or growth assumptions] — *Constraint source: [Assumption or limit]*

**Reliability:**
- [Availability, durability guarantees] — *Requirement source: [Business or technical requirement]*

**Compatibility:**
- [Supported environments/platforms] — *Deployment constraint: [Why this matters]*

---

### Data Model & State Changes (describe what data exists/changes without implementation details)

**Data Entities Affected:**
- [Entity name]: [description of what it represents, key properties, relationships to other entities]

**State Transitions:**
1. Initial state: [what exists before feature activation]
2. Transition: [what changes during operation]
3. Final state: [state after completion]

**Data Persistence Guarantees:**
- What data is persisted and for how long
- Data retention/deletion policies if relevant

---

### Known Constraints & Assumptions (explicitly document any limiting conditions)

**Hard Constraints** (cannot be changed):
1. [Constraint description with source: user requirement, technical limitation, regulatory]

**Assumptions Made** (statements treated as true for this spec's validity; should be verified):
1. [Assumption] — *Verification method: [how to confirm or falsify]*

**Exclusions & Out-of-Scope:**
- What is deliberately not covered by this feature (prevents scope creep and clarifies boundaries)

---

### Validation Approach (descriptive, no code)

How correctness will be verified:
1. [Descriptive test case or verification method] — *Expected result: [what confirms success]*
2. [Descriptive test case or verification method] — *Expected result: [what confirms success]*

Failure modes to detect:
- [Mode]: [how it manifests, how to identify]

---

### Completion Checklist
Mark as Complete only when all of the following are satisfied:

- [ ] Each invariant is provably true with no unstated assumptions
- [ ] No implicit contradictions between requirements or invariants
- [ ] All acceptance scenarios describe verifiable outcomes
- [ ] Edge cases cover significant exception conditions (not exhaustive but comprehensive)
- [ ] Dependencies and ordering constraints are explicit
- [ ] Known constraints and assumptions are documented
- [ ] Validation approach can confirm correctness without implementation details

**Status**: Pending / Complete

---

*Note to spec author: This template is designed to eliminate ambiguity for AI implementation. If you find yourself writing "the system should handle this gracefully" or similar vague language, expand the description until the expected behavior is unambiguous.*
