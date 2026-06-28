# Data and Migrations

## Why the default is simple

The template uses `DbContext` directly as the default persistence boundary. It does not add a generic repository, unit-of-work wrapper, CQRS, or another data-access pattern by default.

Do not select patterns to prove engineering maturity. Select a pattern only when it solves a concrete problem, reduces a demonstrated risk, or improves long-term maintainability. Record that problem and the trade-off before adding the pattern.

Add an abstraction when the project has evidence that the default boundary is insufficient—for example, repeated domain-specific query behavior, a required persistence boundary across modules, or a test seam that cannot be provided at a higher level. Do not add one for hypothetical provider replacement or architectural symmetry.

This keeps generated projects understandable and avoids forcing thousands of services to maintain abstractions they do not use. Teams remain free to introduce a justified pattern without changing the template default.

## Select persistence

Use `--data-provider efcore` with exactly one `--database-provider`: `postgresql`, `sqlserver`, or `sqlite`. Use `--data-provider none --database-provider none` for services without persistence.

Configure `ConnectionStrings__ServiceDatabase` outside source control. Built-in connection strings are local-development fallbacks only.

## Create and apply migrations

Install a `dotnet-ef` tool version matching the generated target framework, then run:

```bash
dotnet ef migrations add <MigrationName>
dotnet ef migrations script --idempotent --output artifacts/migration.sql
```

Review the SQL and rollback impact. Apply migrations as a deployment step before starting the new service version. The template deliberately does not call `Database.Migrate()` at startup because concurrent instances and partial rollout failures make startup migration unsafe.

## Transaction boundary

`ServiceDbContext.SaveChangesAsync` is atomic for one unit of work. Use an explicit EF Core transaction only when multiple saves must commit together. Keep external HTTP calls and message publication outside database transactions; reliable cross-system delivery belongs to the later outbox capability.

## Integration tests

Use SQLite only for fast tests that do not depend on provider-specific SQL behavior. Use Testcontainers with the selected production provider for migrations, constraints, transactions, concurrency, and query behavior. Pin container image versions, create a fresh database per test collection, and capture container logs on failure.
