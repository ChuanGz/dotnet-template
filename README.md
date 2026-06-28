# .NET Service Template

An option-driven template specification for teams building .NET APIs, backend services, integrations, and background workers with consistent engineering defaults.

> **Status:** Foundation stage. This repository defines the intended template scope, options, and compatibility rules; it does not yet contain an installable `dotnet new` template.

## Purpose

The project aims to reduce repeated setup decisions while keeping generated services proportional to their needs. Consumers select capabilities explicitly, and compatibility rules prevent invalid or misleading combinations.

The current document is a reference for the proposed template contract. Commands shown below are illustrative and will not work until the template is implemented and installed.

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

`dotnet-service` is the proposed short name for future `dotnet new` usage. It identifies the platform and workload without coupling generated projects to a business domain or API-only architecture.

The maintained [template option reference](docs/reference/template-options.md) defines proposed values, defaults, compatibility rules, and validation status. Options are not stable until M3 acceptance criteria pass.

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
