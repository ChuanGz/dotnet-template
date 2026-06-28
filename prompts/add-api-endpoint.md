# Add an API Endpoint

## Purpose

Add one endpoint consistent with the project's selected API style.

## Required input

- HTTP method, route, and behavior: `[contract]`
- Selected API style, versioning, OpenAPI, and security options: `[options]`
- Request, response, and error examples: `[models]`
- Authentication and authorization requirements: `[security]`
- Existing endpoint example and test setup: `[context]`

## Prompt

Add the endpoint using the selected Controllers or Minimal API path and the generated project's existing conventions. Implement only the validation, versioning, OpenAPI, authentication, authorization, error contract, and tests enabled by the supplied options and requirements.

## Output expectation

Endpoint code, models, validation, focused tests, and API documentation changes.

## Constraints

Do not enable a disabled API capability or change API style, security policy, versioning strategy, or shared response contracts. Escalate authentication or authorization ambiguity for senior review.

## Review checklist

- Route and HTTP semantics match the contract.
- Validation and error responses are deterministic.
- Authorization is explicit and reviewed.
- Success and failure paths are tested.
- OpenAPI output remains accurate.
