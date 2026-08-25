#!/usr/bin/env python3
"""Print the current V8 NVH baseline screening report."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engineering.resonance import engine_order_frequency, v8_firing_frequency


def main() -> int:
    config_path = ROOT / "parameters" / "nvh_targets.yaml"
    cfg = yaml.safe_load(config_path.read_text())

    envelope = cfg["operating_envelope"]
    rpm_min = envelope["rpm_min"]["value"]
    rpm_max = envelope["rpm_max"]["value"]
    screening_min = envelope["screening_rpm_min"]["value"]
    screening_max = envelope["screening_rpm_max"]["value"]
    orders = cfg["engine_orders"]["tracked_orders"]["value"]

    print("V8 NVH BASELINE SCREEN")
    print("=" * 60)
    print(f"Authoritative RPM envelope: {rpm_min} .. {rpm_max}")
    print(f"Reference screening envelope: {screening_min} .. {screening_max} rpm")
    print(f"Tracked orders: {orders}")
    print()

    for rpm in (screening_min, 1000, 2000, 3000, 4000, 5000, 6000, screening_max):
        if rpm < screening_min or rpm > screening_max:
            continue
        order_text = ", ".join(
            f"{order:g}X={engine_order_frequency(rpm, order):.1f} Hz" for order in orders
        )
        print(f"{rpm:>5} rpm | firing={v8_firing_frequency(rpm):>7.1f} Hz | {order_text}")

    natural = cfg["modal_screening"]["natural_frequencies_hz"]["value"]
    print()
    if not natural:
        print("BLOCKER: no structural natural frequencies registered yet.")
        print("Next evidence: FEA or measured modal data for block/head/sump/covers/mount system.")

    if rpm_min is None or rpm_max is None:
        print("BLOCKER: authoritative operating RPM envelope is still UNKNOWN.")

    print("NOTE: this is screening only; it does not replace modal, harmonic, torsional or acoustic test evidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
