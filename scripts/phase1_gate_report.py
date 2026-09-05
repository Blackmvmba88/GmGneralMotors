#!/usr/bin/env python3
"""Report Phase 1 numeric-handoff readiness from the closure registry."""

from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engineering.phase1_gate import evaluate_gate, status_map_to_items


def main() -> int:
    path = ROOT / "parameters" / "phase1_closure.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    handoff = data["required_numeric_handoff"]
    items = status_map_to_items(handoff)
    report = evaluate_gate(items)

    print(f"Gate: {report.gate}")
    print(f"Status: {'PASS' if report.passed else 'BLOCKED'}")
    print(f"Resolved: {len(report.resolved)}")
    print(f"Blockers: {len(report.blockers)}")

    if report.blockers:
        print("\nBlocking numeric inputs:")
        for item in report.blockers:
            suffix = f" — {item.rationale}" if item.rationale else ""
            print(f"- {item.name}: {item.status}{suffix}")

    # This report is diagnostic during Phase 1. A blocked engineering gate is
    # expected and must not make CI red while the project is intentionally
    # carrying explicit UNKNOWNs.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
