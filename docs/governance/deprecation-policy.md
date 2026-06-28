# Deprecation Policy

## Purpose

Retire options and generated contracts predictably without silently breaking consuming projects.

## Lifecycle

An option, value, default, generated contract, or supported runtime moves through:

```text
Supported → Deprecated → Removed
```

Deprecation requires a supported replacement or an explicit explanation that the capability will not be replaced.

## Required notice

For stable releases, removal requires both:

- at least two published minor releases carrying the deprecation notice; and
- at least 180 days after a supported replacement becomes available.

Removal occurs only in a major release. Before `1.0.0`, the repository may use a shorter window, but it must publish the impact and migration path before removal.

## Deprecation evidence

Every deprecation must record:

- affected option, value, contract, or runtime;
- reason and decision owner;
- first deprecated release and earliest removal release/date;
- supported replacement;
- migration and validation instructions;
- behavior of new and existing generated projects.

The option reference, machine-readable model, generated warnings, release notes, and changelog must agree. Deprecated values remain valid during the notice window and produce an actionable warning.

## Exceptions

An unsupported runtime, critical vulnerability, legal restriction, or unavailable dependency may require accelerated removal. The decision must identify the risk, rejected compatibility alternatives, affected consumers, migration path, and approval evidence. Convenience is not an exception.

## Removal gate

- The notice window is satisfied or an exception is approved.
- A replacement and migration guide are available when applicable.
- Compatibility tests cover deprecated and replacement paths before removal.
- Contract versioning reflects the breaking change.
- Release notes and changelog identify the final supported version.
