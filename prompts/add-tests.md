# Add Tests

## Purpose

Add meaningful coverage for existing behavior or a scoped change.

## Required input

- Behavior and acceptance criteria: `[requirements]`
- Code under test: `[files]`
- Existing test conventions: `[examples]`
- Known risks or regressions: `[risks]`

## Prompt

Add the smallest useful set of tests that verifies observable behavior, boundaries, failures, and relevant edge cases. Follow the existing unit or integration test setup and naming conventions.

## Output expectation

Deterministic tests with clear arrange, act, and assert behavior, plus commands to run them.

## Constraints

Do not test implementation details, duplicate coverage, weaken assertions, or replace integration tests with mocks when real boundaries are required.

## Review checklist

- Each test protects a stated behavior or risk.
- Success, failure, and boundary cases are considered.
- Tests are isolated and repeatable.
- Assertions prove outcomes rather than execution alone.
