# Roadmap

## Vision

`dotnet-template` will provide a production-ready, enterprise-ready .NET starter template with OSS-quality governance and documentation. It will be reusable, option-driven, easy to understand, and straightforward to extend without weakening its defaults.

The template is intended to remain stable across thousands of generated projects over many years. That requires explicit contracts, isolated optional capabilities, predictable upgrades, and compatibility decisions made before implementation.

## Design Principles

- Standardize contracts and expected behavior before implementing features.
- Build commonly used capabilities before optional enterprise integrations.
- Keep defaults simple, useful, and safe.
- Isolate optional features so they do not complicate the default path.
- Make every milestone independently reviewable and valuable to adoption or maintenance.
- Add abstractions only when they solve a demonstrated template problem.
- Minimize breaking changes to options and generated output.
- Favor long-term maintainability over short-term implementation convenience.

## Evolution Diagram

```text
Repository Foundation
        │
        ▼
.NET Standards Adoption
        │
        ▼
Template Option Model
        │
        ▼
API Foundation
        │
        ▼
Data Foundation
        │
        ▼
Enterprise Capabilities
        │
        ▼
Production Readiness
        │
        ▼
Documentation & Adoption
```

## Milestone Summary

| Milestone | Name | Goal | Deliverable |
|---|---|---|---|
| M1 | Repository Foundation | Establish a professional, reviewable repository | OSS-like repository foundation |
| M2 | .NET Standards Adoption | Convert principles into enforceable .NET decisions | Approved standards-adoption matrix |
| M3 | Template Option Model | Stabilize configuration and compatibility contracts | Scalable option model |
| M4 | API Template Core | Implement the common service path | Production-ready API foundation |
| M5 | Data Template Core | Add reliable relational data support | Production-ready data foundation |
| M6 | Enterprise Capabilities | Add isolated integration and processing options | Optional enterprise modules |
| M7 | Production Readiness | Automate quality, security, telemetry, and delivery checks | Production engineering baseline |
| M8 | Documentation & Adoption | Make the template easy to evaluate, use, and extend | Documented first stable release |

## Detailed Milestones

### M1 — Repository Foundation

**Goal:** Establish the repository controls required for transparent contribution and maintenance.

**Scope:**

- README and MIT License
- GitHub issue and pull request templates
- CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, ROADMAP, and CHANGELOG
- Markdown linting and link validation

**Exit checklist:**

- [x] README defines the repository purpose, status, supported use cases, options, and compatibility rules.
- [x] MIT License and OSS governance files are present.
- [x] Issue forms, pull request template, and CODEOWNERS establish contribution entry points.
- [x] CONTRIBUTING defines accepted work, engineering evidence, and rejection criteria.
- [x] SECURITY and SUPPORT define reporting boundaries.
- [x] ROADMAP and CHANGELOG record planned and notable repository evolution.
- [x] CI validates Markdown formatting and links on pushes and pull requests.
- [x] Documentation quality workflow passes on the default branch after the M1 changes merge.
- [x] An evidence-based M1 audit records scope, gaps, and completion status.

**Review gate:** M1 is complete only when every checklist item has repository or CI evidence. File presence alone is insufficient. See the [M1 foundation audit](docs/milestones/m1-repository-foundation.md).

**Deliverable:** A professional OSS-like repository foundation.

### M2 — .NET Standards Adoption

**Goal:** Convert accepted engineering principles into explicit .NET decisions and enforceable generated-project controls before implementation makes them expensive to change.

**Scope:**

- Mapping from engineering principle to .NET decision, generated artifact, and automated evidence
- Coding, project structure, API, validation, logging, testing, and documentation decisions
- CI/CD controls and security baseline for generated projects
- Template philosophy, boundaries, defaults, and non-goals

**Exit checklist:**

- [x] The standards-adoption matrix covers code, structure, API, configuration, validation, errors, logging, testing, documentation, CI, dependencies, and security.
- [x] Every adopted decision names its generated artifact and automated evidence.
- [x] Applicability, trade-offs, exceptions, and M3 implementation handoffs are explicit.
- [x] Technology-neutral guidance and speculative patterns are excluded.
- [x] Baseline C# formatting and language rules are represented in `.editorconfig`.
- [x] An evidence-based M2 audit records the review result and remaining implementation work.

**Review gate:** Every adopted rule changes generated output or automated validation, states its .NET-specific trade-off, and has an observable pass condition. See the [M2 audit](docs/milestones/m2-dotnet-standards-adoption.md).

**Deliverable:** A reviewable .NET standards-adoption matrix established before implementation.

### M3 — Template Option Model

**Goal:** Define a stable configuration contract that can grow without creating invalid project combinations.

**Scope:**

- Option matrix and compatibility rules
- Default configuration
- Mandatory and optional capability boundaries
- Supported .NET LTS versions
- Minimal API versus Controllers guidance
- Simple, layered, and modular structure guidance

**Exit checklist:**

- [x] One versioned machine-readable file owns option names, values, and defaults.
- [x] Normalization and compatibility rules are executable rather than prose-only.
- [x] Defaults, valid combinations, invalid combinations, and normalization have automated cases.
- [x] CI validates the model without external package dependencies.
- [x] Contract evolution rules cover defaults, additions, renames, removals, and migration.
- [x] Migration and deprecation policies define consumer impact, notice, evidence, and removal gates.
- [x] M4 and later generated-output responsibilities are explicit.
- [x] An evidence-based M3 audit records completion and handoff.

**Review gate:** M3 is complete only when the model validator and compatibility suite pass. See the [M3 audit](docs/milestones/m3-template-option-model.md).

**Deliverable:** A stable, scalable configuration model.

### M4 — API Template Core

**Goal:** Implement the most common generated-service path before adding optional infrastructure.

**Scope:**

- ASP.NET Core Web API foundation
- Controllers with an optional Minimal API path
- Dependency injection and configuration
- Validation and consistent error handling
- Response conventions and OpenAPI
- Health checks
- Authentication and authorization

**Review gate:** Supported API variants generate independently, build without manual changes, expose documented health and OpenAPI behavior, enforce the selected security configuration, and pass API tests.

**Deliverable:** A reusable production-ready API foundation.

### M5 — Data Template Core

**Goal:** Provide reliable relational persistence without coupling API-only projects to data infrastructure.

**Scope:**

- EF Core
- PostgreSQL, SQL Server, and SQLite providers
- Migration workflow
- Transaction guidance
- Integration test infrastructure
- Testcontainers guidance

**Review gate:** Each provider can be selected independently, migrations and transaction behavior are documented, generated projects build, and database integration tests pass against real provider instances where supported.

**Deliverable:** A reusable production-ready data foundation.

### M6 — Enterprise Capabilities

**Goal:** Add integration and processing capabilities as isolated, composable options.

**Scope:**

- HTTP integrations
- Messaging with RabbitMQ, Azure Service Bus, or Kafka
- Outbox and inbox-outbox reliability options
- Background jobs
- Redis caching
- Cross-option compatibility validation

**Review gate:** Each capability is opt-in, absent from default output, covered by compatibility tests, and documented with operational requirements and failure behavior.

**Deliverable:** Optional enterprise capabilities that do not affect the default template.

### M7 — Production Readiness

**Goal:** Make generated projects verifiable and operable through automated engineering controls.

**Scope:**

- GitHub Actions and release checks
- Docker packaging
- Formatting, linting, and static analysis
- Dependency and security scanning
- OpenTelemetry and structured logging
- Release readiness validation

**Review gate:** The default and representative option combinations pass build, test, analysis, scanning, container, and telemetry checks in CI with documented failure handling.

**Deliverable:** A production-quality engineering baseline.

### M8 — Documentation & Adoption

**Goal:** Enable developers to evaluate, generate, operate, and extend projects without relying on repository authors.

**Scope:**

- Getting started and template usage
- Option and architecture guides
- API and testing guides
- CI/CD and Docker guides
- Sample module
- Release and upgrade documentation
- First stable release

**Review gate:** A new user can install the template, generate the default and documented variants, run tests, build a container, understand selected options, and extend the sample using verified instructions.

**Deliverable:** A template developers can understand, adopt, and extend with confidence.

## Success Criteria

The roadmap is complete when:

- the default template produces a production-ready service without unnecessary optional infrastructure;
- supported enterprise capabilities are selectable, isolated, tested, and documented;
- generated projects are reusable and maintainable across teams;
- repository governance, documentation, and releases meet OSS-quality expectations;
- junior developers can follow verified workflows without hidden project knowledge;
- senior engineers can evaluate architecture decisions, trade-offs, and extension points;
- option contracts and generated output are stable enough to support thousands of projects;
- compatibility and upgrade guidance minimize breaking changes over time; and
- every supported configuration is validated through automated build, test, and CI checks.
