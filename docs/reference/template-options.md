# Template Option Reference

## Status and ownership

This document owns the proposed `dotnet-service` option contract. Values and defaults remain provisional until M3 validates deterministic output and compatibility behavior. Changes require an option-model review and a changelog entry.

## Options

| Group | Option | Values | Default | Generated effect |
|---|---|---|---|---|
| Runtime | `--dotnet-version` | `net8.0`, `net10.0` | `net8.0` | Select target framework |
| Structure | `--project-structure` | `simple`, `layered`, `modular` | `layered` | Select project boundaries |
| API | `--api-style` | `controllers`, `minimal`, `none` | `controllers` | Select HTTP entry point |
| API | `--api-versioning` | `true`, `false` | `true` | Include API versioning |
| API | `--openapi` | `true`, `false` | `true` | Include OpenAPI generation |
| Data | `--data-provider` | `none`, `efcore`, `dapper` | `efcore` | Select data access |
| Data | `--database-provider` | `none`, `postgresql`, `sqlserver`, `sqlite` | `postgresql` | Select database integration |
| Integration | `--integration` | `none`, `http`, `messaging`, `hybrid` | `none` | Select external integration style |
| Messaging | `--message-broker` | `none`, `rabbitmq`, `azure-service-bus`, `kafka` | `none` | Select message broker |
| Messaging | `--message-pattern` | `none`, `outbox`, `inbox-outbox` | `none` | Select delivery reliability support |
| Jobs | `--job-processing` | `none`, `hosted-service`, `hangfire` | `none` | Select background processing |
| Security | `--authentication` | `none`, `jwt`, `oidc` | `jwt` | Select authentication setup |
| Security | `--authorization` | `none`, `basic`, `policy` | `policy` | Select authorization setup |
| Cache | `--cache-provider` | `none`, `memory`, `redis` | `none` | Select caching support |
| Observability | `--observability` | `none`, `standard`, `opentelemetry` | `opentelemetry` | Select telemetry setup |
| Deployment | `--container` | `true`, `false` | `true` | Include container packaging |
| Testing | `--test-level` | `unit`, `integration`, `architecture`, `full` | `integration` | Select generated test projects |
| Sample | `--sample` | `none`, `basic`, `module` | `module` | Include example behavior |
| CI | `--ci-provider` | `none`, `github-actions`, `azure-devops` | `github-actions` | Select generated CI workflow |

## Compatibility rules

The generator must reject incompatible combinations or normalize them as stated. Recommendations produce warnings rather than block generation.

| Rule | Required behavior |
|---|---|
| `data-provider = none` | Set `database-provider = none` |
| `database-provider = none` | Set `data-provider = none` |
| `integration = none or http` | Set `message-broker = none` |
| `integration = messaging or hybrid` | Require `message-broker != none` |
| `message-pattern != none` | Require messaging integration and persistent data |
| `authentication = none` | Set `authorization = none` |
| `authorization != none` | Require authentication |
| `api-style = none` | Disable API versioning and OpenAPI |
| `job-processing = hangfire` | Require a database provider |
| `database-provider = sqlite` | Warn for enterprise production use |
| `cache-provider = redis` | Recommend container support for local infrastructure |
| `test-level = architecture` | Recommend layered or modular structure |
| `test-level = full` | Include unit, integration, and architecture tests |

## M3 acceptance evidence

- [ ] Every option maps to deterministic generated output.
- [ ] Defaults generate the smallest supported production service.
- [ ] Invalid combinations fail with actionable messages.
- [ ] Normalized values are visible to the user.
- [ ] Representative combinations build and test in CI.
- [ ] Breaking option changes include migration guidance.
