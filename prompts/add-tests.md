# Add Tests

## Purpose

Add meaningful coverage for existing behavior or a scoped change.

## Required input

- Behavior and acceptance criteria: `[requirements]`
- Selected test level and relevant template options: `[options]`
- Code under test: `[files]`
- Existing test conventions: `[examples]`
- Known risks or regressions: `[risks]`

## Prompt

Add the smallest useful set of tests allowed by the selected test level. Verify observable behavior, generated boundaries, failures, and relevant edge cases using the project's existing unit, integration, architecture, database, or container test infrastructure.

## Output expectation

Deterministic tests with clear arrange, act, and assert behavior, plus commands to run them.

## Constraints

Do not generate a test type excluded by the selected options, test implementation details, duplicate coverage, weaken assertions, or replace required real-boundary tests with mocks.

## Review checklist

- Each test protects a stated behavior or risk.
- Success, failure, and boundary cases are considered.
- Tests are isolated and repeatable.
- Assertions prove outcomes rather than execution alone.
