"""NVH baseline utilities driven by the project parameter registry.

This module intentionally keeps unknown design decisions unknown. When the
operating RPM envelope is not frozen, screening values are used and clearly
reported as screening-only.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from engineering.resonance import engine_order_frequency


@dataclass(frozen=True)
class OperatingEnvelope:
    rpm_min: int
    rpm_max: int
    rpm_step: int
    authority: str


@dataclass(frozen=True)
class EngineOrderPoint:
    rpm: int
    order: float
    frequency_hz: float
    authority: str


def load_nvh_targets(path: str | Path = "parameters/nvh_targets.yaml") -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def resolve_operating_envelope(targets: dict[str, Any]) -> OperatingEnvelope:
    envelope = targets["operating_envelope"]
    rpm_min = envelope["rpm_min"]["value"]
    rpm_max = envelope["rpm_max"]["value"]

    if rpm_min is not None and rpm_max is not None:
        return OperatingEnvelope(
            rpm_min=int(rpm_min),
            rpm_max=int(rpm_max),
            rpm_step=int(envelope["screening_step"]["value"]),
            authority="OPERATING_ENVELOPE",
        )

    return OperatingEnvelope(
        rpm_min=int(envelope["screening_rpm_min"]["value"]),
        rpm_max=int(envelope["screening_rpm_max"]["value"]),
        rpm_step=int(envelope["screening_step"]["value"]),
        authority="SCREENING_ONLY",
    )


def tracked_orders(targets: dict[str, Any]) -> list[float]:
    return [float(value) for value in targets["engine_orders"]["tracked_orders"]["value"]]


def generate_order_map(targets: dict[str, Any]) -> list[EngineOrderPoint]:
    envelope = resolve_operating_envelope(targets)
    rows: list[EngineOrderPoint] = []
    for rpm in range(envelope.rpm_min, envelope.rpm_max + 1, envelope.rpm_step):
        for order in tracked_orders(targets):
            rows.append(
                EngineOrderPoint(
                    rpm=rpm,
                    order=order,
                    frequency_hz=engine_order_frequency(rpm, order),
                    authority=envelope.authority,
                )
            )
    return rows


def maximum_tracked_excitation_hz(targets: dict[str, Any]) -> float:
    envelope = resolve_operating_envelope(targets)
    return max(engine_order_frequency(envelope.rpm_max, order) for order in tracked_orders(targets))


def recommended_modal_screening_upper_hz(targets: dict[str, Any]) -> float:
    factor = float(targets["modal_screening"]["analysis_band_multiplier"]["value"])
    return maximum_tracked_excitation_hz(targets) * factor
