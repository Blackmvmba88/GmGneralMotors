#!/usr/bin/env python3
"""Validate the textual V8 engineering baseline.

This intentionally checks only information that is authoritative in the parameter
registry. Geometry checks will be added when CAD artifacts exist.
"""

from __future__ import annotations

import math
import pathlib
import sys
from typing import Any

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PARAM_FILE = ROOT / "parameters" / "master_parameters.yaml"
ALLOWED_STATES = {
    "UNKNOWN",
    "ESTIMATED",
    "REFERENCE",
    "CALCULATED",
    "VERIFIED",
    "LOCKED",
    "DECISION_PENDING",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def value(node: dict[str, Any], key: str) -> Any:
    return node[key]["value"]


def walk_states(node: Any, path: str = "root") -> None:
    if isinstance(node, dict):
        if "status" in node:
            status = node["status"]
            if status not in ALLOWED_STATES:
                fail(f"{path}: illegal status {status!r}")
            if status == "LOCKED" and node.get("value") is None:
                fail(f"{path}: LOCKED parameter cannot have null value")
        for key, child in node.items():
            walk_states(child, f"{path}.{key}")
    elif isinstance(node, list):
        for index, child in enumerate(node):
            walk_states(child, f"{path}[{index}]")


def main() -> int:
    with PARAM_FILE.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    walk_states(data)

    cylinders = value(data["architecture"], "cylinders")
    cylinders_per_bank = value(data["architecture"], "cylinders_per_bank")
    bank_angle = value(data["architecture"], "bank_angle_deg")
    bore = value(data["cylinder"], "bore_mm")
    stroke = value(data["cylinder"], "stroke_mm")
    nominal = value(data["nominal"], "displacement_label_L")
    piston_diameter = value(data["piston"], "diameter_reference_mm")

    if cylinders != 8:
        fail(f"architecture.cylinders expected 8, got {cylinders}")
    if cylinders_per_bank * 2 != cylinders:
        fail("cylinders_per_bank does not sum to total cylinders")
    if not 0 < bank_angle < 180:
        fail(f"bank angle out of range: {bank_angle}")
    if bore <= 0 or stroke <= 0:
        fail("bore and stroke must be positive")

    displacement_l = math.pi / 4.0 * bore**2 * stroke * cylinders / 1_000_000.0
    crank_radius = stroke / 2.0
    delta_percent = abs(displacement_l - nominal) / nominal * 100.0

    print("V8 parameter baseline")
    print(f"  phase:                {data.get('phase')}")
    print(f"  bore:                 {bore:.3f} mm")
    print(f"  stroke:               {stroke:.3f} mm")
    print(f"  crank radius:         {crank_radius:.3f} mm")
    print(f"  calculated displacement: {displacement_l:.6f} L")
    print(f"  nominal label:        {nominal:.3f} L")
    print(f"  nominal delta:        {delta_percent:.3f}%")

    if piston_diameter >= bore:
        print("WARNING: piston diameter reference is >= bore; operating clearance is unresolved.")

    if delta_percent > 2.0:
        fail("calculated displacement differs from nominal label by more than 2%")

    unknown_paths: list[str] = []
    pending_paths: list[str] = []

    def collect_open_items(node: Any, path: str = "root") -> None:
        if isinstance(node, dict):
            status = node.get("status")
            if status == "UNKNOWN":
                unknown_paths.append(path)
            elif status == "DECISION_PENDING":
                pending_paths.append(path)
            for key, child in node.items():
                collect_open_items(child, f"{path}.{key}")
        elif isinstance(node, list):
            for index, child in enumerate(node):
                collect_open_items(child, f"{path}[{index}]")

    collect_open_items(data)
    print(f"  unresolved parameters: {len(unknown_paths)}")
    for path in unknown_paths:
        print(f"    - {path}")

    print(f"  pending design decisions: {len(pending_paths)}")
    for path in pending_paths:
        print(f"    - {path}")

    print("PASS: textual engineering baseline is internally valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
