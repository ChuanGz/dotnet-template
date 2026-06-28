# Add a Feature

## Purpose

Implement one bounded feature using the generated project's conventions.

## Required input

- Feature behavior and acceptance criteria: `[requirements]`
- Selected template options and generated capability set: `[options]`
- Relevant files or similar feature: `[context]`
- Generated project conventions and validation commands: `[constraints and commands]`
- Allowed change scope: `[files or modules]`

## Prompt

Implement the smallest change that satisfies the acceptance criteria inside the generated project's existing capability set. Follow its structure, API style, data access, validation, error-handling, security, observability, and test options. State assumptions and justify any new dependency or abstraction against an observed problem.

## Output expectation

Focused production code, relevant tests, documentation updates, and validation commands.

## Constraints

Do not change selected options, rewrite generated structure, enable an optional capability implicitly, bypass compatibility rules, add CQRS/MediatR/Repository Pattern without evidence, or expand scope without approval.

## Review checklist

- Acceptance criteria are covered.
- Changes stay within scope.
- Failure and edge cases are handled.
- Tests verify behavior.
- Documentation reflects changed behavior.
