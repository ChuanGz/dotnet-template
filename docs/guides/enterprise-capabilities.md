# Enterprise capabilities

M6 capabilities are opt-in and absent from default output.

## HTTP integrations

Use `--integration http` or `hybrid`. Configure `Integrations:Service:BaseUrl`. The generated typed client uses the standard resilience handler; pass cancellation tokens and define operation-specific timeouts.

## Messaging and reliability

Use `--integration messaging|hybrid` with `--message-broker rabbitmq|azure-service-bus|kafka`. Configure `Messaging:ConnectionString` through secrets, never committed settings. `outbox` and `inbox-outbox` require EF Core. Write the business change and outbox record in one database transaction; publish asynchronously; mark successful delivery; consumers deduplicate by message ID. Cross-system atomic transactions are not supported.

## Jobs

`hosted-service` generates a cancellation-aware worker. `hangfire` is reserved by the option contract and requires a database; production scheduling and storage configuration must be supplied by the generated service owner.

## Cache

`memory` is process-local. `redis` uses `ConnectionStrings:Redis`; define TTLs at call sites and never treat cache data as authoritative.
