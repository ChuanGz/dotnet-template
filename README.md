# .NET Service Template

An option-driven template specification for teams building .NET APIs, backend services, integrations, and background workers with consistent engineering defaults.

> **Status:** M1–M8 implementation and local validation complete. External-link and platform-specific checks remain continuously enforced in CI.

## Purpose

The project aims to reduce repeated setup decisions while keeping generated services proportional to their needs. Consumers select capabilities explicitly, and compatibility rules prevent invalid or misleading combinations.

### Repository responsibility

This repository owns the concrete .NET template contract: supported options, generated structure, framework choices, compatibility rules, tests, packaging, and upgrade behavior. It must turn engineering standards into executable defaults and verifiable generated output.

It does not own general software-engineering principles, pattern catalogs, or technology-neutral guidance. A rule belongs here only when it changes the generated .NET project or its automated validation.

## Supported use cases

The planned template covers:

- ASP.NET Core REST APIs using Controllers or Minimal APIs
- Internal and database-backed services
- Simple, layered, and modular-monolith structures
- HTTP and messaging integrations
- Background processing and container packaging

It does not target desktop or client UI frameworks, Razor Pages, MVC UI, games, Azure Functions, Kubernetes platform provisioning, or legacy .NET Framework applications.

## Template contract

`dotnet-service` is the template short name. It identifies the platform and workload without coupling generated projects to a business domain or API-only architecture.

The maintained [template option reference](docs/reference/template-options.md) defines values, defaults, compatibility rules, and validation status.

## Usage

Install the local template, then generate only the capabilities the service needs:

```bash
dotnet new install ./template/content
dotnet new dotnet-service -n OrderService --api-style controllers --data-provider efcore --database-provider postgresql
```

```bash
dotnet new dotnet-service -n LookupService --api-style minimal --data-provider none --database-provider none
```

Database-enabled projects require `ConnectionStrings__ServiceDatabase`. See [Data and Migrations](docs/guides/data-and-migrations.md) before creating a migration or changing transaction behavior.

## Documentation index

- [Adopt and operate the template](docs/guides/adoption.md)
- [Template options](docs/reference/template-options.md)
- [Data and migrations](docs/guides/data-and-migrations.md)
- [Enterprise capabilities](docs/guides/enterprise-capabilities.md)
- [Migration strategy](docs/governance/migration-strategy.md)
- [Deprecation policy](docs/governance/deprecation-policy.md)

## Implementation acceptance criteria

The foundation stage is complete when:

- the template can be installed and discovered through `dotnet new list`;
- every documented option maps to deterministic generated output;
- invalid combinations fail with actionable messages;
- supported combinations build and test successfully;
- generated projects contain only the capabilities selected by the consumer; and
- example commands are verified in automated tests.

## Validation follow-up

The following validation work is intentionally deferred:

- M6: add real integration tests for RabbitMQ, Azure Service Bus, Kafka, outbox delivery, and Hangfire.
- M7: execute Docker builds, security scans, and OpenTelemetry runtime verification in the repository gate.
- M8: smoke-test the generated service, health endpoints, and runnable container.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
