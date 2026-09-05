"""Deterministic V8 rotating-assembly kinematics helpers.

The functions in this module are geometry relations, not production dimensions.
Authoritative rod length, cylinder-to-throw mapping and firing order remain
external parameters until their engineering gates are closed.
"""

from __future__ import annotations

from math import cos, pi, sin, sqrt


CROSS_PLANE_THROW_PHASES_DEG = (0.0, 90.0, 180.0, 270.0)


def normalize_angle_deg(angle_deg: float, period_deg: float = 360.0) -> float:
    """Normalize an angle to [0, period)."""
    if period_deg <= 0:
        raise ValueError("period_deg must be positive")
    return angle_deg % period_deg


def slider_crank_center_position_mm(
    crank_angle_deg: float,
    crank_radius_mm: float,
    rod_length_mm: float,
    phase_deg: float = 0.0,
) -> float:
    """Piston-pin center distance from crank center along the cylinder axis.

    Uses a zero-offset slider-crank relation:

    x(θ) = r cos θ + sqrt(l² - r² sin² θ)

    where θ includes the crank-throw phase.
    """
    if crank_radius_mm <= 0:
        raise ValueError("crank_radius_mm must be positive")
    if rod_length_mm <= crank_radius_mm:
        raise ValueError("rod_length_mm must be greater than crank_radius_mm")

    theta = (crank_angle_deg + phase_deg) * pi / 180.0
    radicand = rod_length_mm**2 - (crank_radius_mm * sin(theta)) ** 2
    if radicand < 0:
        raise ValueError("invalid slider-crank geometry")
    return crank_radius_mm * cos(theta) + sqrt(radicand)


def piston_travel_from_tdc_mm(
    crank_angle_deg: float,
    crank_radius_mm: float,
    rod_length_mm: float,
    phase_deg: float = 0.0,
) -> float:
    """Return piston travel from TDC along the cylinder axis.

    Zero is TDC. At 180° from the throw's TDC the ideal zero-offset travel is
    exactly twice the crank radius (the stroke).
    """
    tdc_position = crank_radius_mm + rod_length_mm
    current = slider_crank_center_position_mm(
        crank_angle_deg,
        crank_radius_mm,
        rod_length_mm,
        phase_deg,
    )
    return tdc_position - current


def cross_plane_throw_phases_deg() -> tuple[float, float, float, float]:
    """Return the four development cross-plane throw phase families."""
    return CROSS_PLANE_THROW_PHASES_DEG
