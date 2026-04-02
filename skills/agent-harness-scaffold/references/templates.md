# Harness Templates

Use these file shapes when generating the scaffold.

## `harness/prompts/planner.md`

Purpose: Turn a short product request into a high-level product spec.

Include:

- Role statement: planner only, no code changes
- Inputs: request file
- Output file: `harness/artifacts/product_spec.md`
- Required sections for the spec
- Rule to avoid over-specifying implementation details

## `harness/prompts/generator.md`

Purpose: Implement only the current sprint contract.

Include:

- Role statement: generator only
- Inputs: product spec, current sprint contract, evaluator report when present
- Output: code changes plus generator report
- Rule to stay within sprint scope
- Rule to run relevant local checks before handoff

## `harness/prompts/evaluator.md`

Purpose: Independently verify whether the sprint contract is satisfied.

Include:

- Role statement: evaluator only, no code changes
- Inputs: product spec, sprint contract, generator report
- Output file: current sprint evaluator report
- Rule to prefer concrete failures over impressions
- Rule to fail the sprint if any required behavior is missing

## `harness/artifacts/request.md`

Use:

```md
# Request

<user prompt>
```

## `harness/artifacts/product_spec.md`

Use:

```md
# Product Spec

## Overview

## Target Users

## Core Features

## Non-Goals

## Suggested Sprint Order

## Acceptance Ideas
```

Write a first draft specific to the request. Do not leave placeholder notes.

## `harness/artifacts/sprint_01_contract.md`

Use:

```md
# Sprint 01 Contract

## Scope

## User-visible Outcomes

## Verification

## Out of Scope
```

Sprint 01 should be the smallest slice that creates a meaningful, testable workflow.

## `harness/artifacts/sprint_01_generator_report.md`

Use:

```md
# Generator Report

## Completed

## Checks Run

## Known Risks

## Files Changed
```

Leave this as a template. Do not claim work has already been done.

## `harness/artifacts/sprint_01_evaluator_report.md`

Use:

```md
# Evaluator Report

## Result

## Findings

## Required Fixes

## Residual Risks
```

Leave this as a template. Do not pre-fill pass or fail.
