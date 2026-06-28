# Review Generated Code

## Purpose

Review AI-generated changes before commit.

## Required input

- Requirements and acceptance criteria: `[requirements]`
- Generated diff: `[diff]`
- Project standards and selected options: `[context]`
- Test and CI results: `[results]`

## Prompt

Review the diff for correctness, scope, security, compatibility, maintainability, test coverage, and documentation accuracy. Report only actionable findings. For each finding, cite the affected location, failure scenario, impact, and minimum correction.

## Output expectation

Prioritized findings followed by residual risks and missing verification. State clearly when no actionable finding exists.

## Constraints

Do not propose stylistic rewrites, unrelated refactoring, generic best practices, or pattern adoption without evidence.

## Review checklist

- Behavior matches the requirements.
- Template options and conventions are preserved.
- Security-sensitive changes receive senior review.
- Relevant tests and CI checks pass.
- No placeholders or unrelated changes remain.
