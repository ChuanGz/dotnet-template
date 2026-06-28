# Add a Feature

## Purpose

Implement one bounded feature using the generated project's conventions.

## Required input

- Feature behavior and acceptance criteria: `[requirements]`
- Relevant files or similar feature: `[context]`
- Selected template options and standards: `[constraints]`
- Allowed change scope: `[files or modules]`

## Prompt

Implement the smallest change that satisfies the acceptance criteria. Follow existing boundaries, naming, dependency, validation, error-handling, security, and testing conventions. State assumptions and explain any new dependency or abstraction.

## Output expectation

Focused production code, relevant tests, documentation updates, and validation commands.

## Constraints

Do not rewrite project structure, bypass compatibility rules, add unrelated patterns, or expand scope without approval.

## Review checklist

- Acceptance criteria are covered.
- Changes stay within scope.
- Failure and edge cases are handled.
- Tests verify behavior.
- Documentation reflects changed behavior.
