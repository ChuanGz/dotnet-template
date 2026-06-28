# Production Readiness Decisions

## Current decision

The template is production-capable for API, EF Core persistence, health, OpenTelemetry, and container options. It is not production-ready for message-broker, outbox, inbox-outbox, or Hangfire options: those outputs currently provide contracts or placeholders rather than durable provider implementations.

This distinction is a release gate. Generation and compilation are not substitutes for integration tests.

## Architecture decisions

- Keep the public option contract stable; complete existing options rather than rename or remove them.
- Keep optional infrastructure absent from default output and condition packages and files on the selected capability.
- Centralize package versions in generated `Directory.Packages.props`; projects own package selection, while the props file owns versions.
- Generate Swagger when selected, but expose it only in Development unless `OpenApi__Enabled=true` is explicitly configured.
- Match Docker build and runtime images to the selected target framework and run as the platform non-root user.
- Require runtime evidence for infrastructure claims. Broker, outbox, Hangfire, telemetry, and containers need behavioral tests, not source-presence assertions.
- Gate pull requests with build, formatting, dependency review, CodeQL, filesystem vulnerability scanning, and generated-container smoke tests.

## Prioritized implementation plan

1. Implement RabbitMQ, Azure Service Bus, and Kafka publishers behind `IMessagePublisher`, with provider-specific health checks and Testcontainers or emulator-backed tests where available.
2. Implement transactional outbox persistence, leasing, retry, idempotency, and a dispatch worker; verify commit, delivery, duplicate handling, and recovery behavior.
3. Implement Hangfire server and storage wiring per supported database provider; verify enqueue, execution, retry, and restart persistence.
4. Add an OTLP test collector assertion so CI verifies exported spans and metrics, not only instrumented-service startup.
5. Exercise every option value and representative compatibility combination, then publish a stable release only after all gates pass.

## Definition of Done

- Every documented option is accepted by the template engine, produces deterministic isolated output, and has behavioral evidence appropriate to the capability.
- RabbitMQ, Azure Service Bus, Kafka, outbox, inbox-outbox, and Hangfire tests exercise real infrastructure or an officially supported emulator.
- .NET 8 and .NET 10 generated projects restore, format, build, test, and run in their matching containers.
- CI fails on vulnerable dependencies, high or critical filesystem findings, CodeQL findings, container startup failure, health failure, or telemetry export failure.
- Swagger is closed in Production by default and can be enabled explicitly.
- Documentation, option metadata, generated README content, and implementation describe the same architecture.
- No deferred validation item remains in the stable-release gate.
