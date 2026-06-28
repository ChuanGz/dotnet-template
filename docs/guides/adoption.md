# Adopt and operate the template

This how-to is for .NET developers evaluating, generating, verifying, and extending a service without repository-author assistance.

## Install and generate

Prerequisites are .NET 8 or 10 SDK and Docker when container output is selected.

```bash
dotnet new install ./template/content
dotnet new dotnet-service -n SampleService --dotnet-version net10.0
cd SampleService
dotnet restore
dotnet build -c Release
dotnet run
```

Verify `/health/live`; database-enabled output also exposes dependency readiness at `/health/ready`. Configuration secrets use environment variables such as `ConnectionStrings__ServiceDatabase`; do not commit them.

## Select and understand capabilities

Use the [option reference](../reference/template-options.md) before combining API, data, integration, job, cache, observability, container, and CI options. Generated folders are extension boundaries: add HTTP clients under `Integrations`, broker adapters under `Messaging`, persistence mappings under `Persistence`, and telemetry enrichment under `Observability`. Unselected folders must remain absent.

## Verify delivery

Run `dotnet format --verify-no-changes`, `dotnet build -c Release`, dependency vulnerability inspection, then `docker build`. Generated CI performs the same controls. A failing scan blocks release; review the direct or transitive package, upgrade deliberately, and record any time-bounded exception rather than suppressing the job.

For containers, run as the configured non-root user and supply configuration at runtime. OpenTelemetry exports through OTLP; set `OTEL_EXPORTER_OTLP_ENDPOINT` and a stable `OTEL_SERVICE_NAME`. Missing collectors must not break request processing.

## Upgrade

Template upgrades do not overwrite generated projects. Compare the old and new generated output for the same option set, read `CHANGELOG.md`, apply contract migrations from the [migration strategy](../governance/migration-strategy.md), and run all delivery controls before merging. Pin the template/package version for reproducible generation.

## Extend safely

Start from one selected capability and preserve its boundary. Add contract tests for public behavior and a generation case proving unrelated variants stay unchanged. If a new option changes defaults or removes output, follow the deprecation policy before release.
