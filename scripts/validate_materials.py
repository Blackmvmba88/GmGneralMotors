#!/usr/bin/env python3
"""Validate material registry structure and provenance guardrails."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "parameters" / "materials.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    required = set(data["required_properties"])
    forbidden = {name.lower() for name in data["rules"]["generic_material_names_forbidden"]}
    materials: dict[str, Any] = data.get("materials", {})
    assignments: dict[str, Any] = data.get("component_assignments", {})

    for material_id, material in materials.items():
        if material_id.lower() in forbidden:
            fail(f"generic material id is forbidden: {material_id}")
        properties = material.get("properties", {})
        missing = sorted(required - set(properties))
        if missing:
            fail(f"{material_id}: missing required properties: {', '.join(missing)}")
        for prop_name, prop in properties.items():
            if not isinstance(prop, dict):
                fail(f"{material_id}.{prop_name}: property must be a mapping")
            if prop.get("value") is not None:
                for field in ("unit", "source", "source_revision", "temperature_c", "status"):
                    if field not in prop:
                        fail(f"{material_id}.{prop_name}: numeric value missing {field}")
            if prop_name == "damping_loss_factor" and prop.get("value") is not None:
                if "confidence" not in prop:
                    fail(f"{material_id}.{prop_name}: damping value missing confidence")

    unresolved = 0
    for component, assignment in assignments.items():
        material_id = assignment.get("material_id")
        if material_id is None:
            unresolved += 1
            continue
        if material_id.lower() in forbidden:
            fail(f"{component}: generic material assignment forbidden: {material_id}")
        if material_id not in materials:
            fail(f"{component}: unknown material_id {material_id}")

    print("V8 material registry")
    print(f"  defined materials: {len(materials)}")
    print(f"  unresolved component assignments: {unresolved}")
    print("PASS: material provenance contract is structurally valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
