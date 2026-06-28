# Review Generated Code

## Purpose

Review AI-generated changes before commit.

## Required input

- Requirements and acceptance criteria: `[requirements]`
- Generated diff: `[diff]`
- Original template options, generated README, and affected paths: `[context]`
- Test and CI results: `[results]`

## Prompt

Review the diff against the selected `dotnet-service` options and generated-project conventions. Check correctness, scope, option compatibility, security, maintainability, tests, observability, and documentation. For each actionable finding, cite the affected location, failure scenario, impact, violated generated contract, and minimum correction.

## Output expectation

Prioritized findings followed by residual risks and missing verification. State clearly when no actionable finding exists.

## Constraints

Do not propose changing template options, enabling unrelated capabilities, stylistic rewrites, generic best practices, or pattern adoption without project evidence.

## Review checklist

- Behavior matches the requirements.
- Template options and conventions are preserved.
- Security-sensitive changes receive senior review.
- Relevant tests and CI checks pass.
- No placeholders or unrelated changes remain.
