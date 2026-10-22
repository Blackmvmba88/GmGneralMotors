#!/usr/bin/env python3
"""Report internally generated cross-plane V8 firing candidates."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engineering.firing_candidates import (
    bank_pulse_gaps_deg,
    enumerate_candidates,
    event_sequence,
    screening_rank,
)


def main() -> int:
    candidates = enumerate_candidates()
    ranked = sorted(candidates, key=screening_rank)

    print("V8 FIRING-SEQUENCE CANDIDATES — SCREENING ONLY")
    print(f"Candidate count: {len(candidates)}")
    print("No manufacturer firing order is imported.\n")

    for index, candidate in enumerate(ranked[:12], start=1):
        phases = dict(candidate.station_phase_deg)
        leads = dict(candidate.first_member)
        sequence = "-".join(event_sequence(candidate))
        left = "/".join(str(v) for v in bank_pulse_gaps_deg(candidate.events, "L"))
        right = "/".join(str(v) for v in bank_pulse_gaps_deg(candidate.events, "R"))
        m = candidate.metrics
        print(
            f"{index:02d} sequence={sequence} "
            f"phases={phases} leads={leads} "
            f"L_gaps={left} R_gaps={right} "
            f"max_gap={m.max_bank_gap_deg} "
            f"gap_error={m.bank_gap_squared_error} "
            f"same_bank={m.same_bank_adjacencies}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
