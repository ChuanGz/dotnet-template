# AI Usage for Template Users

AI can accelerate routine development, but it does not replace project context or engineering judgment. You remain responsible for selecting suitable template options, reviewing generated code, and verifying every change through tests and CI.

## Before prompting AI

1. Read the generated project's `README.md` and relevant documentation.
2. Identify the selected template options, including structure, API style, data access, authentication, integrations, observability, and test level.
3. Locate an existing implementation similar to the requested change.
4. Give AI the relevant project structure, standards, and constraints. Do not provide secrets or production data.

## Working method

- State the problem, expected behavior, affected project area, and acceptance criteria.
- Require existing naming, layering, error handling, security, testing, and dependency conventions.
- Request a small, reviewable change. Split large features into independently verifiable steps.
- Ask AI to identify assumptions, edge cases, and files it intends to change.
- Review the code before committing. Reject unrelated rewrites and unjustified abstractions.
- Run formatting, build, tests, and repository CI checks.
- Update README, API, operational, or architectural documentation when behavior changes.

## Good uses

- Create focused API endpoints and request or response models.
- Generate validation rules from explicit requirements.
- Add unit and integration tests.
- Update OpenAPI-related and project documentation.
- Explain the existing project structure.
- Identify missing edge cases.
- Review code against the generated project's standards.

## Uses requiring rejection or escalation

- Do not let AI choose architecture or template options without project requirements.
- Do not add CQRS, MediatR, Repository Pattern, or other patterns without a concrete problem and justified trade-off.
- Require senior review for authentication, authorization, secrets, encryption, or other security changes.
- Reject project-structure rewrites and attempts to bypass template compatibility rules.
- Do not generate a large feature in one prompt.
- Do not accept code without relevant tests or code that violates existing standards.
- Reject generic documentation, placeholder sections, and unsupported claims.

## Completion check

Before committing, confirm that the change is scoped, follows existing conventions, handles relevant failure cases, passes tests and CI checks, and includes required documentation updates.

Reusable task prompts are available in [`prompts/`](../prompts/README.md).
