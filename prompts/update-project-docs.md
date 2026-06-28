# Update Project Documentation

## Purpose

Keep project documentation aligned with changed behavior.

## Required input

- Behavior or contract change: `[change]`
- Selected template options and generated project type: `[options]`
- Affected documentation: `[files]`
- Verified commands, examples, and outputs: `[evidence]`
- Intended reader: `[audience]`

## Prompt

Update only documentation owned by the generated project and affected by the change. Describe verified behavior, selected-option implications, prerequisites, usage, failure handling, and compatibility impact needed by the intended reader.

## Output expectation

A focused documentation patch with working links and verified examples.

## Constraints

Do not copy technology-neutral guidance into the project, restate the template option reference, or add generic advice, placeholders, unsupported claims, speculative features, or duplicated sections.

## Review checklist

- Documentation matches implemented behavior.
- Commands and links are valid.
- Assumptions and limitations are visible.
- Obsolete guidance is removed.
- No unrelated content is changed.
