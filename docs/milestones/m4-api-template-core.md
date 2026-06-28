# M4 API Template Core Audit

## Outcome

M4 provides an installable `dotnet-service` template for controller, minimal, and non-HTTP business-service foundations without adding data or enterprise integrations.

## Evidence

| Criterion | Status | Evidence |
|---|---|---|
| Standard template installation | PASS | `template/content/.template.config/template.json` |
| API styles isolated | PASS | Template source modifiers and `tests/m4/run.sh` |
| Option contract aligned | PASS | M4 tests compare implemented options with `config/template-options.json` |
| Error and validation behavior | PASS | Problem Details, controller validation, minimal endpoint filter |
| API contracts aligned | PASS | Controllers and Minimal API use the same request and response contracts |
| Health behavior | PASS | Live and ready health endpoints |
| Security configuration | PASS | JWT bearer configuration and fallback authorization policy |
| OpenAPI optionality | PASS | Conditional package and middleware |
| API versioning | PASS | Version sets, version metadata, and version-aware routes |
| Generated projects build | PASS | API template CI workflow and local generation gate |

## Audit result

**PASS** — M4 implements the API foundation and automated generation checks. EF Core, databases, messaging, jobs, caching, containers, and telemetry remain owned by later milestones.

## Reopen triggers

Reopen M4 when an API mode stops generating independently, an unselected capability leaks into output, generated projects fail to build, or public error and security behavior diverges across API styles.
