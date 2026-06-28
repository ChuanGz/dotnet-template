# Add an API Endpoint

## Purpose

Add one endpoint consistent with the project's selected API style.

## Required input

- HTTP method, route, and behavior: `[contract]`
- Request, response, and error examples: `[models]`
- Authentication and authorization requirements: `[security]`
- Existing endpoint example and test setup: `[context]`

## Prompt

Add the endpoint using the existing Controllers or Minimal API convention. Implement input validation, status codes, error handling, authorization, OpenAPI metadata, and tests required by the supplied contract.

## Output expectation

Endpoint code, models, validation, focused tests, and API documentation changes.

## Constraints

Do not change API style, security policy, versioning strategy, or shared response contracts. Escalate security ambiguity for senior review.

## Review checklist

- Route and HTTP semantics match the contract.
- Validation and error responses are deterministic.
- Authorization is explicit and reviewed.
- Success and failure paths are tested.
- OpenAPI output remains accurate.
