#!/usr/bin/env python3
"""Create a starter planner/generator/evaluator harness scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path


PLANNER_PROMPT = """# Planner

You are the planner agent.

Read `harness/artifacts/request.md` and expand it into `harness/artifacts/product_spec.md`.

Requirements:
- Write only the product spec.
- Focus on user outcomes, major features, non-goals, and sprintable delivery order.
- Stay high level on implementation details.
- Do not write code.
"""


GENERATOR_PROMPT = """# Generator

You are the generator agent.

Read:
- `harness/artifacts/product_spec.md`
- `harness/artifacts/sprint_01_contract.md`
- `harness/artifacts/sprint_01_evaluator_report.md` when it contains review feedback

Requirements:
- Implement only the current sprint contract.
- Stay within scope.
- Run relevant checks before handoff.
- Update `harness/artifacts/sprint_01_generator_report.md` with completed work, checks run, known risks, and files changed.
"""


EVALUATOR_PROMPT = """# Evaluator

You are the evaluator agent.

Read:
- `harness/artifacts/product_spec.md`
- `harness/artifacts/sprint_01_contract.md`
- `harness/artifacts/sprint_01_generator_report.md`

Requirements:
- Do not modify application code.
- Verify the sprint contract independently.
- Prefer concrete failures over general impressions.
- Fail the sprint if any required behavior is missing.
- Write findings to `harness/artifacts/sprint_01_evaluator_report.md`.
"""


def write_file(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return f"skip  {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"write {path}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Repo root where harness/ will be created.")
    parser.add_argument("--prompt", required=True, help="User product prompt.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    harness = root / "harness"

    files = {
        harness / "prompts" / "planner.md": PLANNER_PROMPT,
        harness / "prompts" / "generator.md": GENERATOR_PROMPT,
        harness / "prompts" / "evaluator.md": EVALUATOR_PROMPT,
        harness / "artifacts" / "request.md": f"# Request\n\n{args.prompt.strip()}\n",
        harness / "artifacts" / "product_spec.md": """# Product Spec

## Overview

## Target Users

## Core Features

## Non-Goals

## Suggested Sprint Order

## Acceptance Ideas
""",
        harness / "artifacts" / "sprint_01_contract.md": """# Sprint 01 Contract

## Scope

## User-visible Outcomes

## Verification

## Out of Scope
""",
        harness / "artifacts" / "sprint_01_generator_report.md": """# Generator Report

## Completed

## Checks Run

## Known Risks

## Files Changed
""",
        harness / "artifacts" / "sprint_01_evaluator_report.md": """# Evaluator Report

## Result

## Findings

## Required Fixes

## Residual Risks
""",
    }

    for path, content in files.items():
        print(write_file(path, content, args.force))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
