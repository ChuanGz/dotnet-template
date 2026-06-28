# .NET Service Template

An option-driven template specification for teams building .NET APIs, backend services, integrations, and background workers with consistent engineering defaults.

> **Status:** Foundation stage. This repository defines the intended template scope, options, and compatibility rules; it does not yet contain an installable `dotnet new` template.

## Purpose

The project aims to reduce repeated setup decisions while keeping generated services proportional to their needs. Consumers select capabilities explicitly, and compatibility rules prevent invalid or misleading combinations.

The current document is a reference for the proposed template contract. Commands shown below are illustrative and will not work until the template is implemented and installed.

## Supported use cases

The planned template covers:

- ASP.NET Core REST APIs using Controllers or Minimal APIs
- Internal and database-backed services
- Simple, layered, and modular-monolith structures
- HTTP and messaging integrations
- Background processing and container packaging

It does not target desktop or client UI frameworks, Razor Pages, MVC UI, games, Azure Functions, Kubernetes platform provisioning, or legacy .NET Framework applications.

## Template options

`dotnet-service` is the proposed short name for future `dotnet new` usage. It identifies the platform and workload without coupling generated projects to a business domain or API-only architecture. Names, defaults, and generated behavior remain subject to implementation validation.

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

The generator must reject incompatible combinations or normalize them as described below. Recommendations should produce a warning rather than block generation.

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
| `cache-provider = redis` -> `container = true` (recommended) | Provide local Redis infrastructure |
| `test-level = architecture` -> layered or modular (recommended) | Architecture tests need explicit boundaries |
| `test-level = full` | Includes unit, integration, and architecture tests |

## Proposed usage

These examples document the intended interface; they are not executable in the repository's current foundation stage.

```bash
dotnet new dotnet-service -n OrderService --api-style controllers
```

```bash
dotnet new dotnet-service -n LookupService --api-style minimal
```

## Implementation acceptance criteria

The foundation stage is complete when:

- the template can be installed and discovered through `dotnet new list`;
- every documented option maps to deterministic generated output;
- invalid combinations fail with actionable messages;
- supported combinations build and test successfully;
- generated projects contain only the capabilities selected by the consumer; and
- example commands are verified in automated tests.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
