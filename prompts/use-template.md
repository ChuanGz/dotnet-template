# Use the Template

## Purpose

Establish project context before requesting implementation work.

## Required input

- Original generation command or recorded template options: `[options]`
- Relevant README and documentation excerpts: `[context]`
- Generated project structure and project files: `[tree or relevant paths]`
- Available build, test, format, and CI commands: `[commands]`
- Task and acceptance criteria: `[requirements]`

## Prompt

Explain how the selected `dotnet-service` options shape this project and where the requested change belongs. Identify generated boundaries, included and excluded capabilities, compatibility constraints, and validation commands. List assumptions or missing evidence before proposing changes.

## Output expectation

A concise implementation boundary, affected areas, risks, and validation plan.

## Constraints

Do not reinterpret template options, enable an unselected capability, invent paths or commands, add patterns, or write code until the generated-project evidence is sufficient.

## Review checklist

- Selected options are interpreted correctly.
- Recommendations match the supplied project structure.
- Unknowns are explicit.
- No unnecessary architecture is introduced.
