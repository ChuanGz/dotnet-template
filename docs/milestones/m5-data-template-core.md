# M5 Data Template Core Audit

## Outcome

M5 adds isolated EF Core persistence for PostgreSQL, SQL Server, and SQLite without coupling data-free projects to database packages or source files.

## Evidence

| Criterion | Status | Evidence |
|---|---|---|
| Provider selection | PASS | Canonical option model and template symbols |
| Provider isolation | PASS | Source modifiers, conditional packages, and `tests/m5/run.sh` |
| Generated projects build | PASS | Independent provider generation gate |
| Real provider smoke test | PASS | SQLite readiness check against a real database file |
| Migration safety | PASS | Deployment-owned migration workflow; no startup migration |
| Transaction guidance | PASS | Explicit unit-of-work and cross-system boundaries |
| Production-provider testing | DOCUMENTED | PostgreSQL and SQL Server Testcontainers guidance; CI execution remains environment-dependent |

## Audit result

**PASS** — M5 provides the production data foundation. Messaging reliability, outbox behavior, and distributed transactions remain M6 responsibilities.

## Reopen triggers

Reopen M5 when a provider stops generating independently, data-free output contains persistence artifacts, migration ownership changes, or provider-specific behavior is accepted without a real-provider test.
