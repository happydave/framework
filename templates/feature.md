# Feature Plan Instructions

## Purpose of a Feature Plan

Each feature plan document (templates/feature.md or similar) must contain enough precise, unambiguous description so an AI can produce complete, correct, production-ready code for that feature on the first attempt.

The document exists to communicate desired **outcomes**, **non-negotiable rules**, and **verifiable success criteria** — not to dictate internal implementation choices unless those choices are essential to the outcome.

## Core Principles

- Write only what must be true about the finished feature.
- State outcomes and constraints clearly; avoid prescribing how unless the how is itself a constraint.
- Explicitly identify areas where the AI has freedom to choose the best approach.
- Use plain, objective language. No code, no pseudo-code, no file structures unless they are a hard requirement.

## Required Content & Guidance

Every feature plan must include the sections below. Complete only what is genuinely necessary for unambiguous implementation; omit or mark optional sections that do not apply.

**Objective**  
One clear sentence that captures the single desired purpose of the feature.  
Example: Enable users to securely register, verify their email, and log in so they can access protected resources.

**Invariants & Hard Constraints**  
Bullet list of non-negotiable truths that must always hold. Keep this list short and provable. Include only items that, if violated, break correctness, security, or compliance.  
Examples:  
- Passwords are never stored in plain text or reversible form.  
- All authentication tokens expire and cannot be used after revocation.  
- Personally identifiable data is encrypted at rest using AES-256 or stronger.  
(For project-wide security rules — e.g., OWASP Top 10 mitigation, no plain-text secrets in logs — reference a central security.md or include critical ones here.)

**Required Behaviors & Verifications**  
Concise descriptions of required behavior and verifiable success criteria. Organize by major concern (user-visible actions, data flows, security/privacy, etc.).  
Use SHALL statements for must-have outcomes and include focused scenarios (Gherkin-style or numbered steps) that define “done.”  
Cover at least: one happy path, one key failure mode, one security-relevant case.  
Example:  
- SHALL allow new users to register with a valid email and strong password, then send a time-limited verification link.  
- SHALL reject registration attempts with duplicate emails (return 409 Conflict).  
Given valid email and strong password  
When user submits registration  
Then verification email is sent and account is created in unverified state  
AI has freedom over: route patterns, validation libraries, exact HTTP status wording (unless security-critical), internal error handling structure, and non-functional optimizations unless listed below.

**Edge Cases & Required Error Responses**  
Bullet list of significant exceptions and exactly how the system must respond (status code, user message intent, retryability, etc.).

**Non-Functional Constraints** (only when critical to the project)  
List only project-wide or feature-specific requirements that affect correctness or viability.

**Data & State Changes** (when the feature affects persistent state)  
Simple description of new/updated entities and allowed transitions — no schema syntax or implementation detail.

**Explicit AI Freedom**  
Mandatory closing section that lists what is intentionally **not** constrained. Tailor this list to reflect the actual project tech stack (e.g., specify allowed frameworks).  
Example:  
The AI has full discretion over:  
- Choice of libraries and patterns within the approved tech stack  
- File and directory organization  
- Naming conventions (except where names are user-visible or constrained)  
- Internal code structure and optimizations  
- Exact phrasing of non-security-critical user messages

## Dependencies & Context

Reference related documents or prior features only when order or shared invariants matter.

## Final Checks Before Marking Ready

- Do the invariants and SHALLs eliminate realistic sources of wrong implementation?  
- Are the verifications sufficient for a human to confirm the feature works as intended?  
- Have all critical decisions been stated while leaving non-critical ones open?

Once these checks pass, mark the document Ready for Implementation.
