# .NET Service Template

An option-driven template specification for teams building .NET APIs, backend services, integrations, and background workers with consistent engineering defaults.

> **Status:** The template contract and its supported generation paths are implemented and validated. Production broker adapters, durable outbox dispatch, and Hangfire storage are optional reference extensions, not template release blockers.

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

## How it works

1. Install the template package with `dotnet new install`.
2. Run `dotnet new dotnet-service` with the capabilities required by the service.
3. The template validates option compatibility, evaluates computed conditions, and includes only the matching source files and configuration.
4. The generated project is restored, built, tested, and maintained like a normal .NET application.

The template makes creation-time decisions. It is not a framework, runtime, deployment platform, or application host.

## What is the output?

The output is a standalone .NET application source tree. Depending on the selected options, it can contain API endpoints, persistence, authentication, integrations, messaging contracts, background jobs, caching, observability, container files, and CI configuration.

Capabilities that are not selected are excluded rather than left as disabled scaffolding. The generated project does not reference this repository and does not require the template to build or run.

## Flow new features to the template

Changes intended for future applications should be implemented in `template/content` and delivered through the template contract:

1. Add or update the implementation in the generated source tree.
2. For optional behavior, define the option and compatibility rules, then conditionally include its files and package references.
3. Add generation, build, and behavior tests for enabled and disabled cases.
4. Update the option reference and generated-project documentation in the same change.

Existing generated applications do not receive the change automatically. Teams adopt applicable improvements through their normal application change and review process.

## Can capabilities be installed later?

Yes, but installation after generation is an application change, not a template operation. A team can add the required packages, source files, configuration, and tests manually, or generate a temporary project with the desired options and selectively merge the relevant changes.

Regenerating over an existing application is not an upgrade mechanism because it can overwrite application-owned decisions. Use the [migration strategy](docs/governance/migration-strategy.md) when adopting newer template capabilities.

## How does the template coexist with the generated application?

The template repository is the upstream blueprint; the generated application is an independently owned snapshot. After generation:

- application teams own business code, configuration, migrations, deployment, and dependency updates;
- template changes affect newly generated applications only; and
- reusable improvements can flow back into the template when they are broadly applicable and preserve its option contract.

This boundary lets generated services evolve independently without coupling their build or release lifecycle to the template repository.

## Documentation index

- [Adopt and operate the template](docs/guides/adoption.md)
- [Template options](docs/reference/template-options.md)
- [Production readiness decisions](docs/architecture/production-readiness.md)
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

The template release is validated independently from optional end-to-end infrastructure reference implementations:

- M6: representative messaging, reliability, jobs, and cache combinations are generation- and build-tested. Real RabbitMQ, Azure Service Bus, Kafka, outbox-delivery, and Hangfire infrastructure samples are optional extensions.
- M7: CI now builds and runs .NET 8 and .NET 10 containers, probes liveness with OpenTelemetry enabled, verifies Swagger is closed in Production, and gates CodeQL and Trivy findings.
- M8: generated-service and container smoke tests are automated; external link checks remain CI-owned.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
