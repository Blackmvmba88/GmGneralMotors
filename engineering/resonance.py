"""Classical resonance, NVH and flow-screening helpers.

Adapted from the classical engineering layer of:
Blackmvmba88/archimedes-quantum-resonance-engine

Scope boundary:
- This module is intentionally classical: structural dynamics, acoustics,
  engine orders and basic fluid/aero-acoustic screening.
- Quantum-matter models from the source research repository are not used to
  claim a quantum performance mechanism in the combustion engine.

All functions use SI units unless explicitly documented otherwise.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt
from typing import Iterable, Sequence


DEFAULT_SPEED_OF_SOUND_M_S = 343.0
DEFAULT_AIR_DENSITY_KG_M3 = 1.225
DEFAULT_AIR_DYNAMIC_VISCOSITY_PA_S = 1.81e-5


def engine_order_frequency(rpm: float, order: float) -> float:
    """Return excitation frequency in Hz for an engine order at RPM.

    order=1.0 means one event per crank revolution.
    """
    if rpm < 0:
        raise ValueError("rpm must be non-negative")
    if order < 0:
        raise ValueError("order must be non-negative")
    return order * rpm / 60.0


def firing_frequency_four_stroke(rpm: float, cylinders: int) -> float:
    """Combustion firing frequency for an evenly firing four-stroke engine.

    A four-stroke cylinder fires once every two crank revolutions, so the
    aggregate firing order is cylinders / 2 events per crank revolution.
    For a V8 this is the 4th engine order.
    """
    if cylinders <= 0:
        raise ValueError("cylinders must be positive")
    return engine_order_frequency(rpm, cylinders / 2.0)


def v8_firing_frequency(rpm: float) -> float:
    """Convenience wrapper for an evenly firing four-stroke V8."""
    return firing_frequency_four_stroke(rpm, 8)


def quarter_wave_frequency(length_m: float, speed_of_sound_m_s: float = DEFAULT_SPEED_OF_SOUND_M_S) -> float:
    """Fundamental quarter-wave resonance f = c / (4L)."""
    if length_m <= 0:
        raise ValueError("length_m must be positive")
    return speed_of_sound_m_s / (4.0 * length_m)


def helmholtz_resonator_frequency(
    neck_area_m2: float,
    cavity_volume_m3: float,
    effective_neck_length_m: float,
    speed_of_sound_m_s: float = DEFAULT_SPEED_OF_SOUND_M_S,
) -> float:
    """Ideal Helmholtz resonator frequency.

    f = c/(2π) * sqrt(A/(V*L_eff))

    End correction must be included in effective_neck_length_m by the caller.
    """
    if neck_area_m2 <= 0 or cavity_volume_m3 <= 0 or effective_neck_length_m <= 0:
        raise ValueError("Helmholtz geometry terms must be positive")
    return (speed_of_sound_m_s / (2.0 * pi)) * sqrt(
        neck_area_m2 / (cavity_volume_m3 * effective_neck_length_m)
    )


@dataclass(frozen=True, order=True)
class CavityMode:
    frequency_hz: float
    nx: int
    ny: int
    nz: int


def rectangular_cavity_modes(
    length_x_m: float,
    length_y_m: float,
    length_z_m: float,
    max_index: int = 4,
    speed_of_sound_m_s: float = DEFAULT_SPEED_OF_SOUND_M_S,
) -> list[CavityMode]:
    """Return ideal rigid-wall rectangular cavity mode frequencies.

    f = c/2 * sqrt((nx/Lx)^2 + (ny/Ly)^2 + (nz/Lz)^2)

    This is distinct from a necked Helmholtz resonator.
    """
    if min(length_x_m, length_y_m, length_z_m) <= 0:
        raise ValueError("cavity dimensions must be positive")
    if max_index < 1:
        raise ValueError("max_index must be >= 1")

    modes: list[CavityMode] = []
    for nx in range(max_index + 1):
        for ny in range(max_index + 1):
            for nz in range(max_index + 1):
                if nx == ny == nz == 0:
                    continue
                frequency = (speed_of_sound_m_s / 2.0) * sqrt(
                    (nx / length_x_m) ** 2
                    + (ny / length_y_m) ** 2
                    + (nz / length_z_m) ** 2
                )
                modes.append(CavityMode(frequency, nx, ny, nz))
    return sorted(modes)


def reynolds_number(
    velocity_m_s: float,
    characteristic_length_m: float,
    density_kg_m3: float = DEFAULT_AIR_DENSITY_KG_M3,
    dynamic_viscosity_pa_s: float = DEFAULT_AIR_DYNAMIC_VISCOSITY_PA_S,
) -> float:
    """Reynolds number Re = rho U L / mu."""
    if characteristic_length_m <= 0 or density_kg_m3 <= 0 or dynamic_viscosity_pa_s <= 0:
        raise ValueError("length, density and viscosity must be positive")
    return density_kg_m3 * velocity_m_s * characteristic_length_m / dynamic_viscosity_pa_s


def strouhal_frequency(
    velocity_m_s: float,
    characteristic_length_m: float,
    strouhal_number: float = 0.2,
) -> float:
    """Vortex-shedding estimate f = St U / D.

    St=0.2 is only a screening default, commonly useful near circular-cylinder
    shedding regimes; real intake/exhaust geometry requires CFD/measurement.
    """
    if characteristic_length_m <= 0:
        raise ValueError("characteristic_length_m must be positive")
    if strouhal_number <= 0:
        raise ValueError("strouhal_number must be positive")
    return strouhal_number * velocity_m_s / characteristic_length_m


def sdof_natural_frequency(mass_kg: float, stiffness_n_m: float) -> float:
    """Undamped single-degree-of-freedom natural frequency in Hz."""
    if mass_kg <= 0 or stiffness_n_m <= 0:
        raise ValueError("mass_kg and stiffness_n_m must be positive")
    return sqrt(stiffness_n_m / mass_kg) / (2.0 * pi)


def modal_separation_percent(excitation_hz: float, natural_hz: float) -> float:
    """Absolute frequency separation as a percent of the natural frequency."""
    if natural_hz <= 0:
        raise ValueError("natural_hz must be positive")
    return abs(natural_hz - excitation_hz) / natural_hz * 100.0


@dataclass(frozen=True)
class ResonanceCoincidence:
    rpm: float
    order: float
    excitation_hz: float
    natural_hz: float
    separation_percent: float


def resonance_coincidences(
    rpm_values: Iterable[float],
    orders: Sequence[float],
    natural_frequencies_hz: Sequence[float],
    margin_percent: float,
) -> list[ResonanceCoincidence]:
    """Screen order lines against known natural frequencies.

    This is a screening tool, not a substitute for modal/harmonic FEA or test.
    """
    if margin_percent < 0:
        raise ValueError("margin_percent must be non-negative")

    hits: list[ResonanceCoincidence] = []
    for rpm in rpm_values:
        for order in orders:
            excitation = engine_order_frequency(rpm, order)
            for natural in natural_frequencies_hz:
                separation = modal_separation_percent(excitation, natural)
                if separation <= margin_percent:
                    hits.append(
                        ResonanceCoincidence(
                            rpm=float(rpm),
                            order=float(order),
                            excitation_hz=excitation,
                            natural_hz=float(natural),
                            separation_percent=separation,
                        )
                    )
    return hits
