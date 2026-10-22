"""Generate internal cross-plane V8 firing-sequence candidates.

The candidate space is derived only from the project's own common-pin topology:
four longitudinal stations, four 90-degree phase families, and two cylinders per
station that must fire 360 crank degrees apart.

This module does not select a production firing order.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from typing import Mapping, Sequence


STATION_ORDER = ("S1", "S2", "S3", "S4")
PHASE_FAMILIES_DEG = (0, 90, 180, 270)
DEFAULT_PAIRS = {
    "S1": ("L1", "R1"),
    "S2": ("L2", "R2"),
    "S3": ("L3", "R3"),
    "S4": ("L4", "R4"),
}


@dataclass(frozen=True)
class FiringEvent:
    angle_deg: int
    cylinder: str
    station: str

    @property
    def bank(self) -> str:
        return self.cylinder[0]


@dataclass(frozen=True)
class CandidateMetrics:
    max_bank_gap_deg: int
    min_bank_gap_deg: int
    bank_gap_squared_error: int
    same_bank_adjacencies: int


@dataclass(frozen=True)
class FiringCandidate:
    station_phase_deg: tuple[tuple[str, int], ...]
    first_member: tuple[tuple[str, str], ...]
    events: tuple[FiringEvent, ...]
    metrics: CandidateMetrics


def _validate_phase_map(station_phase_deg: Mapping[str, int]) -> None:
    if set(station_phase_deg) != set(STATION_ORDER):
        raise ValueError("station phase map must define S1..S4 exactly")
    if tuple(sorted(station_phase_deg.values())) != PHASE_FAMILIES_DEG:
        raise ValueError("station phases must be a permutation of 0/90/180/270 degrees")


def circular_gaps_deg(angles_deg: Sequence[int], cycle_deg: int = 720) -> tuple[int, ...]:
    """Return circular angular gaps around a cycle."""
    if not angles_deg:
        raise ValueError("angles_deg must not be empty")
    ordered = sorted(angles_deg)
    if ordered[0] < 0 or ordered[-1] >= cycle_deg:
        raise ValueError("angles must be inside the cycle")
    gaps = [ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1)]
    gaps.append(ordered[0] + cycle_deg - ordered[-1])
    return tuple(gaps)


def bank_pulse_gaps_deg(events: Sequence[FiringEvent], bank: str) -> tuple[int, ...]:
    """Return the four pulse gaps for one bank over the 720-degree cycle."""
    bank = bank.upper()
    if bank not in {"L", "R"}:
        raise ValueError("bank must be L or R")
    angles = [event.angle_deg for event in events if event.bank == bank]
    if len(angles) != 4:
        raise ValueError("expected four firing events per bank")
    return circular_gaps_deg(angles)


def build_candidate(
    station_phase_deg: Mapping[str, int],
    first_member: Mapping[str, str],
    station_pairs: Mapping[str, tuple[str, str]] = DEFAULT_PAIRS,
) -> FiringCandidate:
    """Build one evenly firing 720-degree candidate.

    For each common-pin station, the selected first cylinder fires at that
    station's phase and its paired cylinder fires exactly 360 degrees later.
    """
    _validate_phase_map(station_phase_deg)
    if set(first_member) != set(STATION_ORDER):
        raise ValueError("first_member must define S1..S4 exactly")

    events: list[FiringEvent] = []
    for station in STATION_ORDER:
        pair = station_pairs[station]
        lead = first_member[station]
        if lead not in pair:
            raise ValueError(f"{lead} is not a member of {station}")
        follow = pair[1] if lead == pair[0] else pair[0]
        phase = station_phase_deg[station]
        events.append(FiringEvent(phase, lead, station))
        events.append(FiringEvent(phase + 360, follow, station))

    events.sort(key=lambda event: event.angle_deg)
    event_gaps = circular_gaps_deg([event.angle_deg for event in events])
    if event_gaps != (90, 90, 90, 90, 90, 90, 90, 90):
        raise ValueError("candidate is not evenly firing at 90-degree cadence")

    left_gaps = bank_pulse_gaps_deg(events, "L")
    right_gaps = bank_pulse_gaps_deg(events, "R")
    all_bank_gaps = left_gaps + right_gaps
    squared_error = sum((gap - 180) ** 2 for gap in all_bank_gaps)
    same_bank = sum(
        1
        for index, event in enumerate(events)
        if event.bank == events[(index + 1) % len(events)].bank
    )

    metrics = CandidateMetrics(
        max_bank_gap_deg=max(all_bank_gaps),
        min_bank_gap_deg=min(all_bank_gaps),
        bank_gap_squared_error=squared_error,
        same_bank_adjacencies=same_bank,
    )
    return FiringCandidate(
        station_phase_deg=tuple((station, station_phase_deg[station]) for station in STATION_ORDER),
        first_member=tuple((station, first_member[station]) for station in STATION_ORDER),
        events=tuple(events),
        metrics=metrics,
    )


def enumerate_candidates() -> tuple[FiringCandidate, ...]:
    """Enumerate the complete internal candidate space: 24 × 16 = 384."""
    candidates: list[FiringCandidate] = []
    for phase_perm in permutations(PHASE_FAMILIES_DEG):
        phase_map = dict(zip(STATION_ORDER, phase_perm))
        for lead_bits in product((0, 1), repeat=4):
            lead_map = {
                station: DEFAULT_PAIRS[station][bit]
                for station, bit in zip(STATION_ORDER, lead_bits)
            }
            candidates.append(build_candidate(phase_map, lead_map))
    return tuple(candidates)


def screening_rank(candidate: FiringCandidate) -> tuple[int, int, int, int]:
    """Heuristic ranking key for review, not a production optimization objective."""
    m = candidate.metrics
    return (
        m.max_bank_gap_deg,
        m.bank_gap_squared_error,
        m.same_bank_adjacencies,
        -m.min_bank_gap_deg,
    )


def event_sequence(candidate: FiringCandidate) -> tuple[str, ...]:
    return tuple(event.cylinder for event in candidate.events)
