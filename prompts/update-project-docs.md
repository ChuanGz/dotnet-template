# Update Project Documentation

## Purpose

Keep project documentation aligned with changed behavior.

## Required input

- Behavior or contract change: `[change]`
- Affected documentation: `[files]`
- Verified commands, examples, and outputs: `[evidence]`
- Intended reader: `[audience]`

## Prompt

Update only the documentation affected by the change. Describe the verified behavior, prerequisites, usage, failure handling, and compatibility impact needed by the intended reader.

## Output expectation

A focused documentation patch with working links and verified examples.

## Constraints

Do not add generic guidance, placeholder content, unsupported claims, speculative features, or duplicated sections.

## Review checklist

- Documentation matches implemented behavior.
- Commands and links are valid.
- Assumptions and limitations are visible.
- Obsolete guidance is removed.
- No unrelated content is changed.
