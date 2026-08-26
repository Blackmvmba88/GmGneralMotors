"""Deterministic dimensional relations for the V8 design baseline.

This module contains only geometry/kinematic relations that can be defended from
current project inputs. It must not silently invent unresolved design dimensions.
"""

from __future__ import annotations

from math import pi

MM_PER_IN = 25.4
CC_PER_CUBIC_INCH = 16.387064


def displacement_l(bore_mm: float, stroke_mm: float, cylinders: int) -> float:
    """Engine displacement in liters from bore, stroke and cylinder count."""
    if bore_mm <= 0 or stroke_mm <= 0 or cylinders <= 0:
        raise ValueError("bore, stroke and cylinders must be positive")
    return (pi / 4.0) * bore_mm**2 * stroke_mm * cylinders / 1_000_000.0


def displacement_cid(bore_mm: float, stroke_mm: float, cylinders: int) -> float:
    """Engine displacement in cubic inches."""
    return displacement_l(bore_mm, stroke_mm, cylinders) * 1000.0 / CC_PER_CUBIC_INCH


def displacement_per_cylinder_cc(bore_mm: float, stroke_mm: float) -> float:
    """Swept volume of one cylinder in cubic centimeters."""
    if bore_mm <= 0 or stroke_mm <= 0:
        raise ValueError("bore and stroke must be positive")
    return (pi / 4.0) * bore_mm**2 * stroke_mm / 1000.0


def crank_radius_mm(stroke_mm: float) -> float:
    if stroke_mm <= 0:
        raise ValueError("stroke must be positive")
    return stroke_mm / 2.0


def bank_half_angle_deg(bank_angle_deg: float) -> float:
    if not 0 < bank_angle_deg < 180:
        raise ValueError("bank angle must be between 0 and 180 degrees")
    return bank_angle_deg / 2.0


def stroke_for_target_l(target_l: float, bore_mm: float, cylinders: int) -> float:
    """Solve stroke in mm for a target displacement in liters at fixed bore."""
    if target_l <= 0 or bore_mm <= 0 or cylinders <= 0:
        raise ValueError("target displacement, bore and cylinders must be positive")
    return target_l * 1_000_000.0 / ((pi / 4.0) * bore_mm**2 * cylinders)


def stroke_for_target_cid(target_cid: float, bore_mm: float, cylinders: int) -> float:
    """Solve stroke in mm for a target cubic-inch displacement at fixed bore."""
    if target_cid <= 0:
        raise ValueError("target_cid must be positive")
    return stroke_for_target_l(target_cid * CC_PER_CUBIC_INCH / 1000.0, bore_mm, cylinders)


def piston_operating_od_mm(bore_mm: float, diametral_clearance_mm: float) -> float:
    """Piston OD from bore and total diametral piston-to-wall clearance."""
    if bore_mm <= 0 or diametral_clearance_mm < 0:
        raise ValueError("bore must be positive and clearance non-negative")
    od = bore_mm - diametral_clearance_mm
    if od <= 0:
        raise ValueError("clearance cannot consume the bore")
    return od


def deck_height_mm(
    stroke_mm: float,
    connecting_rod_length_mm: float,
    piston_compression_height_mm: float,
    deck_clearance_mm: float,
) -> float:
    """Crank-axis to deck distance along a cylinder axis at TDC.

    Positive deck_clearance means piston crown is below the deck at TDC.
    """
    if connecting_rod_length_mm <= 0 or piston_compression_height_mm <= 0:
        raise ValueError("rod length and compression height must be positive")
    return (
        crank_radius_mm(stroke_mm)
        + connecting_rod_length_mm
        + piston_compression_height_mm
        + deck_clearance_mm
    )


def compression_ratio(swept_volume_cc: float, clearance_volume_cc: float) -> float:
    """Static geometric compression ratio."""
    if swept_volume_cc <= 0 or clearance_volume_cc <= 0:
        raise ValueError("volumes must be positive")
    return (swept_volume_cc + clearance_volume_cc) / clearance_volume_cc
