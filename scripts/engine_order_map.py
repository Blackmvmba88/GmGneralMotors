#!/usr/bin/env python3
"""Generate the current V8 engine-order screening map.

Authoritative operating RPM values are never invented. If they are still
UNKNOWN, the script uses the explicit screening envelope and labels output
SCREENING_ONLY.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from engineering.nvh import (
    generate_order_map,
    load_nvh_targets,
    maximum_tracked_excitation_hz,
    recommended_modal_screening_upper_hz,
    resolve_operating_envelope,
    tracked_orders,
)


def write_csv(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["rpm", "order", "frequency_hz", "authority"])
        for row in rows:
            writer.writerow([row.rpm, row.order, f"{row.frequency_hz:.6f}", row.authority])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--targets", default="parameters/nvh_targets.yaml")
    parser.add_argument("--csv", type=Path, default=None)
    args = parser.parse_args()

    targets = load_nvh_targets(args.targets)
    envelope = resolve_operating_envelope(targets)
    rows = generate_order_map(targets)

    print("V8 NVH ENGINE-ORDER MAP")
    print(f"authority={envelope.authority}")
    print(f"rpm={envelope.rpm_min}..{envelope.rpm_max} step={envelope.rpm_step}")
    print(f"orders={tracked_orders(targets)}")
    print(f"max_tracked_excitation_hz={maximum_tracked_excitation_hz(targets):.2f}")
    print(f"recommended_modal_screening_upper_hz={recommended_modal_screening_upper_hz(targets):.2f}")

    if args.csv:
        write_csv(args.csv, rows)
        print(f"csv={args.csv}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
