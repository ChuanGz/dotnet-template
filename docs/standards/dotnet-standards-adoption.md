# .NET Standards Adoption

## Decision and scope

This document defines the .NET-specific decisions that generated `dotnet-service` projects must implement or verify. It owns concrete defaults and evidence targets, not general engineering guidance.

M2 standardizes the contract before template code exists. M3 must map each applicable row to deterministic generation and compatibility tests; later milestones implement the generated artifacts.

## Adoption matrix

| Area | Adopted .NET decision | Generated artifact | Automated evidence | Applicability and trade-off |
|---|---|---|---|---|
| SDK | Pin one supported LTS SDK for generation and CI; choose the exact default during M3 release validation | `global.json`, target frameworks | Restore and build matrix | Pinning improves repeatability but requires planned updates |
| Compiler | Enable nullable reference types, implicit usings, deterministic builds, and warnings as errors in CI | shared build properties | `dotnet build` | Strict compilation increases upgrade work but prevents warning drift |
| Formatting | Use repository `.editorconfig`; CI runs format verification without rewriting files | `.editorconfig` | `dotnet format --verify-no-changes` | Generated code and contributions use one reviewable baseline |
| Dependencies | Centralize package versions and commit dependency lock files | package props and lock files | locked restore | Repeatability adds deliberate dependency-update work |
| Structure | Generate only the selected `simple`, `layered`, or `modular` structure; do not add unused layers | solution and project references | build plus dependency tests where boundaries exist | More structure is justified only by selected boundaries |
| API | Generate only the selected Controllers or Minimal API path; use stable HTTP semantics and Problem Details errors | endpoints and API configuration | API integration tests and OpenAPI validation | API-specific controls do not apply when `api-style = none` |
| Configuration | Bind typed options and validate required configuration at startup; keep secrets out of source | options classes and configuration | startup failure tests and secret scan | Early failure is preferred to latent invalid configuration |
| Validation | Validate external input at the entry boundary and preserve business-rule ownership inside the capability | endpoint validation and domain behavior | boundary and behavior tests | Duplicate validation is rejected unless boundaries have different contracts |
| Errors | Map known failures once at the accountable boundary; never expose stack traces or provider details | exception handling and public error contracts | API and logging tests | Stable public errors increase compatibility responsibility |
| Logging | Use structured `ILogger` messages, correlation context, and explicit sensitive-data exclusions | logging configuration and call sites | analyzer rules and integration tests | Additional fields must support an operational decision |
| Observability | Generate health and telemetry only at the selected level; preserve cancellation and trace context | health checks and telemetry configuration | startup and telemetry smoke tests | Disabled observability options must not leave unused packages or setup |
| Testing | Generate only selected test levels; integration tests use real boundaries where mocks cannot prove behavior | test projects and fixtures | `dotnet test` by configuration | Test volume follows failure risk, not a fixed pyramid |
| Documentation | Record generation options, prerequisites, commands, configuration, and enabled capabilities | generated `README.md` | Markdown lint, link check, and command smoke tests | Generated docs must omit capabilities not selected |
| CI | Restore, format-check, build, test, and scan the exact generated configuration | provider-specific workflow | representative option matrix | Expensive optional integration checks run only when selected |
| Security | Deny access according to the selected auth model, avoid committed secrets, and require senior review for security-default changes | auth configuration and security workflow | authorization tests, dependency review, secret scan | Security controls are explicit; `none` never implies hidden protection |

## Mandatory generation rules

- Do not generate packages, projects, configuration, tests, or documentation for an unselected capability.
- Do not introduce CQRS, MediatR, Repository Pattern, or other architecture patterns without a selected option and concrete generated-project requirement.
- Keep option normalization visible; never silently produce output different from the recorded configuration.
- Treat generated build, test, formatting, documentation, and security checks as part of the template contract.
- Keep public contracts additive where possible and document migration for breaking option or output changes.

## Exception process

An exception must identify the affected option set, problem, rejected default, alternative, trade-off, owner, validation, and removal or review trigger. Convenience or personal preference is not sufficient. A default change requires compatibility impact and migration review.

## M3 handoff

M3 must assign every matrix row one of three states: generated, not applicable for the selected options, or deferred to a named milestone. M3 is not complete while a mandatory row lacks deterministic output or a validation plan.
