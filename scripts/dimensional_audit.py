#!/usr/bin/env python3
"""Run the current dimensional reconstruction audit for the V8 baseline."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engineering.dimensional import (
    bank_half_angle_deg,
    crank_radius_mm,
    displacement_cid,
    displacement_l,
    displacement_per_cylinder_cc,
    stroke_for_target_cid,
    stroke_for_target_l,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, help="Optional output path for candidate authority modes")
    args = parser.parse_args()

    cfg = yaml.safe_load((ROOT / "parameters" / "master_parameters.yaml").read_text())
    bore = float(cfg["cylinder"]["bore_mm"]["value"])
    stroke = float(cfg["cylinder"]["stroke_mm"]["value"])
    cylinders = int(cfg["architecture"]["cylinders"]["value"])
    bank_angle = float(cfg["architecture"]["bank_angle_deg"]["value"])
    label_l = float(cfg["nominal"]["displacement_label_L"]["value"])

    current_l = displacement_l(bore, stroke, cylinders)
    current_cid = displacement_cid(bore, stroke, cylinders)
    per_cyl_cc = displacement_per_cylinder_cc(bore, stroke)
    radius = crank_radius_mm(stroke)
    half_bank = bank_half_angle_deg(bank_angle)

    exact_350_stroke = stroke_for_target_cid(350.0, bore, cylinders)
    exact_5700_stroke = stroke_for_target_l(5.700, bore, cylinders)

    candidates = [
        {
            "mode": "blueprint_geometry",
            "bore_mm": bore,
            "stroke_mm": stroke,
            "displacement_l": current_l,
            "displacement_cid": current_cid,
        },
        {
            "mode": "exact_350_cid_with_bore_fixed",
            "bore_mm": bore,
            "stroke_mm": exact_350_stroke,
            "displacement_l": displacement_l(bore, exact_350_stroke, cylinders),
            "displacement_cid": 350.0,
        },
        {
            "mode": "exact_5_700_l_with_bore_fixed",
            "bore_mm": bore,
            "stroke_mm": exact_5700_stroke,
            "displacement_l": 5.700,
            "displacement_cid": displacement_cid(bore, exact_5700_stroke, cylinders),
        },
    ]

    print("V8 DIMENSIONAL RECONSTRUCTION AUDIT")
    print("=" * 68)
    print(f"Blueprint bore/stroke: {bore:.6f} mm × {stroke:.6f} mm")
    print(f"Derived displacement: {current_l:.9f} L / {current_cid:.6f} CID")
    print(f"Blueprint label: {label_l:.3f} L")
    print(f"Per-cylinder swept volume: {per_cyl_cc:.6f} cc")
    print(f"Crank radius: {radius:.6f} mm")
    print(f"Bank half-angle: ±{half_bank:.6f}°")
    print()
    print("AUTHORITY CANDIDATES")
    for row in candidates:
        print(
            f"- {row['mode']}: bore={row['bore_mm']:.6f} mm, "
            f"stroke={row['stroke_mm']:.6f} mm, "
            f"disp={row['displacement_l']:.9f} L / {row['displacement_cid']:.6f} CID"
        )

    print()
    print("BLOCKERS FOR DIMENSIONAL_MODEL_VALIDATED")
    blockers = [
        "select displacement authority mode",
        "cylinder center spacing",
        "bank longitudinal offset",
        "deck stack: rod length + compression height + deck clearance",
        "piston-to-wall clearance",
        "wrist-pin geometry",
        "main/rod journal diameters",
        "crank station spacing and phasing",
        "camshaft axis location",
        "head/chamber/gasket/piston-crown volume model",
        "flywheel and pulley reference planes",
    ]
    for blocker in blockers:
        print(f"- {blocker}")

    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(candidates[0]))
            writer.writeheader()
            writer.writerows(candidates)
        print(f"\nWrote candidate table: {args.csv}")

    print("\nSTATUS: PHASE 1 ACTIVE / CAD GEOMETRY STILL LOCKED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
