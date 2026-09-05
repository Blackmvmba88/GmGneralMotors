#!/usr/bin/env python3
"""Generate first-pass resonance geometry candidates from target frequencies.

This tool is screening-only. It does not replace CFD, FEA, thermal analysis,
packaging checks, manufacturing review, or physical testing.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engineering.resonance import (
    helmholtz_cavity_volume_for_frequency,
    modal_exclusion_band,
    quarter_wave_length,
    rpm_for_engine_order_frequency,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("frequency_hz", type=float, help="Target frequency in Hz")
    parser.add_argument("--order", type=float, default=4.0, help="Engine order to map against target frequency")
    parser.add_argument("--sound-speed", type=float, default=343.0, help="Speed of sound in m/s")
    parser.add_argument("--neck-area-mm2", type=float, default=1000.0, help="Candidate Helmholtz neck area in mm^2")
    parser.add_argument("--neck-length-mm", type=float, default=50.0, help="Effective Helmholtz neck length in mm")
    parser.add_argument("--modal-margin-percent", type=float, default=10.0, help="Screening exclusion margin around a mode")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.frequency_hz <= 0:
        raise SystemExit("frequency_hz must be positive")

    q_length_m = quarter_wave_length(args.frequency_hz, args.sound_speed)
    crossing_rpm = rpm_for_engine_order_frequency(args.frequency_hz, args.order)
    neck_area_m2 = args.neck_area_mm2 * 1e-6
    neck_length_m = args.neck_length_mm * 1e-3
    cavity_m3 = helmholtz_cavity_volume_for_frequency(
        args.frequency_hz,
        neck_area_m2,
        neck_length_m,
        args.sound_speed,
    )
    low_hz, high_hz = modal_exclusion_band(args.frequency_hz, args.modal_margin_percent)

    print("V8 RESONANCE GEOMETRY SCREEN")
    print("=" * 64)
    print(f"Target frequency:              {args.frequency_hz:.3f} Hz")
    print(f"Engine-order crossing:         {args.order:g}X @ {crossing_rpm:.1f} rpm")
    print(f"Quarter-wave effective length: {q_length_m * 1000.0:.2f} mm")
    print(f"Helmholtz neck area:           {args.neck_area_mm2:.2f} mm^2")
    print(f"Helmholtz effective neck:      {args.neck_length_mm:.2f} mm")
    print(f"Helmholtz cavity volume:       {cavity_m3 * 1e6:.2f} cc")
    print(f"Modal exclusion band:          {low_hz:.2f} .. {high_hz:.2f} Hz")
    print()
    print("SCREENING ONLY — candidate geometry must still pass packaging, CFD/FEA,")
    print("thermal, manufacturing, fatigue and physical validation gates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
