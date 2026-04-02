---
name: agent-harness-scaffold
description: Generate a planner-generator-evaluator coding harness scaffold from a user's product prompt. Use when Codex needs to turn a new app idea, prototype request, or long-running coding task into initial `harness/` prompts, artifacts, and first-pass spec/contract/report files in the current repo.
---

# Agent Harness Scaffold

Create a first-pass multi-agent harness that another Codex or Claude Code session can run manually.

Default to creating the scaffold under `harness/` at the current repo root. If the user names a different target directory, use that instead.

## Workflow

1. Read the user request and normalize it into a short product prompt.
2. Run `scripts/init_harness_scaffold.py --target <dir> --prompt "<normalized prompt>"` to create the directory structure and base files.
3. Tailor the generated files so they are specific to the user's request.
4. Keep Sprint 01 narrow, user-visible, and directly testable.
5. Do not create extra documentation such as `README.md` or changelogs.

## Files To Produce

Create or update these files:

- `harness/prompts/planner.md`
- `harness/prompts/generator.md`
- `harness/prompts/evaluator.md`
- `harness/artifacts/request.md`
- `harness/artifacts/product_spec.md`
- `harness/artifacts/sprint_01_contract.md`
- `harness/artifacts/sprint_01_generator_report.md`
- `harness/artifacts/sprint_01_evaluator_report.md`

Use the exact section expectations in [references/templates.md](references/templates.md).

## Tailoring Rules

- Put the user's request verbatim in `request.md`.
- Expand `product_spec.md` into a concrete first draft, not placeholders.
- Write `sprint_01_contract.md` for the smallest useful vertical slice.
- Keep `Out of Scope` explicit so later sprints remain available.
- Leave the report files as fill-in-ready templates; do not fake completed work.

## Existing Repos

If `harness/` already exists:

- Read the existing files before editing.
- Preserve useful project-specific content.
- Update only what is necessary to align the scaffold with the new request.

## Validation

Before finishing:

1. Ensure every generated markdown file has the required sections.
2. Ensure Sprint 01 can be validated by direct product behavior.
3. Ensure the prompts describe distinct roles for planner, generator, and evaluator.
