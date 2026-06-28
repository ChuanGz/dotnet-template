# M3 Template Option Model Audit

## Outcome

M3 establishes one executable, versioned contract for template options and compatibility. It does not claim that M4–M7 generated artifacts exist.

## Evidence

| Criterion | Status | Evidence |
|---|---|---|
| Machine-readable source of truth | PASS | `config/template-options.json` |
| Model integrity validation | PASS | `src/DotNetTemplate.OptionModel` |
| Defaults and normalization tests | PASS | `tests/options/cases.json` |
| Invalid combinations rejected | PASS | Compatibility test cases |
| CI enforcement | PASS | `.github/workflows/option-model.yml` |
| Human reference synchronized | PASS | `docs/reference/template-options.md` |
| Evolution and handoff bounded | PASS | Contract evolution rules and ROADMAP |
| Consumer migrations are governed | PASS | `docs/governance/migration-strategy.md` |
| Deprecation and removal are governed | PASS | `docs/governance/deprecation-policy.md` |

## Audit result

**PASS** — The option model is executable and independently reviewable. M4 and later milestones remain responsible for proving deterministic generated output for each applicable option.

## Process record

| Date | Change | Result |
|---|---|---|
| 2026-06-28 | Replaced prose-only ownership with a versioned JSON contract | One source of truth established |
| 2026-06-28 | Added a dependency-free validator and compatibility suite | Defaults, normalization, and rejection behavior executable |
| 2026-06-28 | Added CI and contract-evolution rules | M3 closed with explicit M4 handoff |
| 2026-06-28 | Added migration and deprecation policies | Long-term consumer compatibility governed |

## Reopen triggers

Reopen M3 when an option changes without a contract-version decision, generated output cannot represent a model value, normalization becomes ambiguous, or a valid combination lacks a deterministic implementation path.
