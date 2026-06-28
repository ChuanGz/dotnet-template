# dotnet-template

Production-ready, option-driven .NET template for teams building APIs, backend services, integrations, and background processing with consistent architecture, security, testing, observability, and delivery standards.

> Status: repository foundation. Template implementation is not available yet.

## Supported use cases

Supports ASP.NET Core REST APIs with Controllers or Minimal APIs, internal services, modular monoliths, database-backed services, HTTP and messaging integrations, background processing, and containers.

Does not target WPF, WinForms, WinUI, MAUI, Blazor UI, Razor Pages, MVC UI, games, Azure Functions, Kubernetes platforms, or legacy .NET Framework.

## Template options

`production-api` is the proposed template short name used with `dotnet new`.

| Group | Option | Values | Default | Purpose |
|---|---|---|---|---|
| Runtime | `--dotnet-version` | `net8.0`, `net10.0` | `net8.0` | Select LTS target |
| Structure | `--project-structure` | `simple`, `layered`, `modular` | `layered` | Choose organization level |
| API | `--api-style` | `controllers`, `minimal`, `none` | `controllers` | Choose API style |
| API | `--api-versioning` | `true`, `false` | `true` | Enable API versioning |
| API | `--openapi` | `true`, `false` | `true` | Enable OpenAPI |
| Data | `--data-provider` | `none`, `efcore`, `dapper` | `efcore` | Choose data access |
| Data | `--database-provider` | `none`, `postgresql`, `sqlserver`, `sqlite` | `postgresql` | Choose database |
| Integration | `--integration` | `none`, `http`, `messaging`, `hybrid` | `none` | Choose integration style |
| Messaging | `--message-broker` | `none`, `rabbitmq`, `azure-service-bus`, `kafka` | `none` | Choose broker |
| Messaging | `--message-pattern` | `none`, `outbox`, `inbox-outbox` | `none` | Choose reliability pattern |
| Jobs | `--job-processing` | `none`, `hosted-service`, `hangfire` | `none` | Choose job strategy |
| Security | `--authentication` | `none`, `jwt`, `oidc` | `jwt` | Choose authentication |
| Security | `--authorization` | `none`, `basic`, `policy` | `policy` | Choose authorization |
| Cache | `--cache-provider` | `none`, `memory`, `redis` | `none` | Choose cache |
| Observability | `--observability` | `none`, `standard`, `opentelemetry` | `opentelemetry` | Choose telemetry level |
| Deployment | `--container` | `true`, `false` | `true` | Enable containers |
| Testing | `--test-level` | `unit`, `integration`, `architecture`, `full` | `integration` | Choose test level |
| Sample | `--sample` | `none`, `basic`, `module` | `module` | Include sample |
| CI | `--ci-provider` | `none`, `github-actions`, `azure-devops` | `github-actions` | Choose CI |

## Compatibility rules

| Rule | Meaning |
|---|---|
| `data-provider = none` -> `database-provider = none` | No data access means no database configuration |
| `database-provider = none` -> `data-provider = none` | No database means no EF Core or Dapper |
| `integration = none or http` -> `message-broker = none` | No messaging means no broker |
| `integration = messaging or hybrid` -> `message-broker != none` | Messaging requires a broker |
| `message-pattern != none` -> `integration = messaging or hybrid` | Inbox/outbox requires messaging |
| `message-pattern != none` -> data and database providers are not `none` | Reliable messaging requires persistence |
| `authentication = none` -> `authorization = none` | Authorization requires identity |
| `authorization != none` -> `authentication != none` | Anonymous users cannot be authorized |
| `api-style = none` -> API versioning and OpenAPI are `false` | No API means no API metadata |
| `job-processing = hangfire` -> `database-provider != none` | Hangfire requires persistence |
| `database-provider = sqlite` | Warn for enterprise production use |
| `cache-provider = redis` -> `container = true` recommended | Provide local Redis infrastructure |
| `test-level = architecture` -> layered or modular recommended | Architecture tests need boundaries |
| `test-level = full` | Includes unit, integration, and architecture tests |

## Example commands

```bash
dotnet new production-api -n OrderService --api-style controllers
```

```bash
dotnet new production-api -n LookupService --api-style minimal
```

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
