"""Phase 1 design-space screening helpers.

All outputs from this module are exploratory unless the caller explicitly
promotes a value through the project's provenance/status process.
"""

from __future__ import annotations


def mean_piston_speed_mps(stroke_mm: float, rpm: float) -> float:
    """Return mean piston speed in m/s."""
    if stroke_mm <= 0 or rpm < 0:
        raise ValueError("stroke must be > 0 and rpm must be >= 0")
    return 2.0 * (stroke_mm / 1000.0) * rpm / 60.0


def rod_length_from_ratio(stroke_mm: float, rod_to_stroke_ratio: float) -> float:
    """Return connecting-rod center-to-center length from rod/stroke ratio."""
    if stroke_mm <= 0 or rod_to_stroke_ratio <= 0:
        raise ValueError("stroke and ratio must be > 0")
    return stroke_mm * rod_to_stroke_ratio


def cylinder_spacing_from_bridge(bore_mm: float, bridge_mm: float) -> float:
    """Return cylinder center spacing from bore plus inter-cylinder bridge."""
    if bore_mm <= 0 or bridge_mm < 0:
        raise ValueError("bore must be > 0 and bridge must be >= 0")
    return bore_mm + bridge_mm


def four_cylinder_bank_span_mm(center_spacing_mm: float) -> float:
    """Return center-to-center span from cylinder 1 to 4 for one bank."""
    if center_spacing_mm <= 0:
        raise ValueError("center spacing must be > 0")
    return 3.0 * center_spacing_mm


def engine_order_frequency_hz(rpm: float, order: float) -> float:
    """Return engine-order frequency in Hz."""
    if rpm < 0 or order < 0:
        raise ValueError("rpm and order must be >= 0")
    return rpm * order / 60.0
