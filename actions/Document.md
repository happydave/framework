# Document

## Intent

After implementation, verify that the project's documentation — README, code comments, inline help text, and any other human-facing descriptions — is accurate, complete, and consistent with the current state of the code.

Implementation changes code. Documentation does not always keep pace. This action closes that gap explicitly rather than hoping it happens incidentally.

## When to Document

- After completing an implementation (before or after the Reflect action)
- After any change that alters user-facing behavior, configuration, setup instructions, or public APIs
- When a reflection or review identifies documentation drift

This action can apply to a single ticket's scope or to the project as a whole. Use judgment — a small bugfix may need no documentation pass, while a feature that changes setup steps or adds new capabilities almost certainly does.

## Procedure

### 1. Identify What May Have Changed

Review the implementation and determine which documentation surfaces could be affected:

- **README** — project description, setup instructions, usage examples, feature list
- **Code comments** — function and module-level documentation, especially on public APIs
- **Inline help text** — CLI help strings, UI labels, tooltip text, error messages
- **Configuration documentation** — environment variables, config files, options
- **Contribution or development guides** — build steps, test instructions, architecture notes

### 2. Check Each Surface for Accuracy

For each relevant documentation surface:

- Does it describe the current behavior, not a previous version?
- Are setup or installation steps still correct?
- Are examples still valid and runnable?
- Are referenced files, commands, or paths still correct?
- Are new features, options, or behaviors documented?
- Have removed features or deprecated behaviors been cleaned up?

### 3. Check for Consistency

Look for contradictions across documentation surfaces:

- Does the README match the actual CLI flags or API?
- Do code comments agree with the behavior they describe?
- Are the same concepts described the same way in different places?

### 4. Update

Make the necessary corrections. Keep the existing style and tone of each document — this action updates content, not voice.

## Guidance

- This is a verification and correction pass, not a rewrite. Touch only what is inaccurate, incomplete, or inconsistent.
- Do not add documentation for internal implementation details unless the project's conventions call for it. Focus on surfaces that users, contributors, or future AI sessions will read.
- If a documentation gap is large enough to warrant its own work item (e.g., a missing architecture guide), create a ticket rather than writing it inline during this action.
- When in doubt about whether something needs updating, check the code. The code is the source of truth; documentation must agree with it.
