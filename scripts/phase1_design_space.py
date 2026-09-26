#!/usr/bin/env python3
"""Generate exploratory Phase 1 packaging/kinematic screening tables."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engineering.design_space import (
    cylinder_spacing_from_bridge,
    engine_order_frequency_hz,
    four_cylinder_bank_span_mm,
    mean_piston_speed_mps,
    rod_length_from_ratio,
)

BORE_MM = 101.6
STROKE_MM = 88.9
BANK_REFERENCE_LENGTH_MM = 530.0

BRIDGES_MM = (5.0, 7.5, 10.0, 12.5, 15.0)
ROD_RATIOS = (1.60, 1.65, 1.70, 1.75, 1.80)
RPM_POINTS = (6000, 6500, 7000, 7500, 8000)


def main() -> int:
    print("PHASE 1 DESIGN SPACE — SCREENING ONLY")
    print("No value in this report is CAD authority.\n")

    print("Cylinder packaging sweep")
    print("bridge_mm,spacing_mm,bank_center_span_mm,residual_vs_530_mm")
    for bridge in BRIDGES_MM:
        spacing = cylinder_spacing_from_bridge(BORE_MM, bridge)
        span = four_cylinder_bank_span_mm(spacing)
        residual = BANK_REFERENCE_LENGTH_MM - span
        print(f"{bridge:.1f},{spacing:.1f},{span:.1f},{residual:.1f}")

    print("\nRod-ratio sweep")
    print("rod_ratio,rod_length_mm")
    for ratio in ROD_RATIOS:
        print(f"{ratio:.2f},{rod_length_from_ratio(STROKE_MM, ratio):.3f}")

    print("\nRPM / piston-speed / 4X firing-frequency sweep")
    print("rpm,mean_piston_speed_mps,order_4x_hz")
    for rpm in RPM_POINTS:
        print(
            f"{rpm},{mean_piston_speed_mps(STROKE_MM, rpm):.3f},"
            f"{engine_order_frequency_hz(rpm, 4.0):.3f}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
