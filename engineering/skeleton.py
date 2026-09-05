"""Executable geometric relations for the V8 master skeleton.

This module intentionally computes relationships, not missing design dimensions.
All numeric dimensions supplied by callers must come from the governed parameter
registry or an explicitly labeled design study.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, pi, sin, sqrt
from typing import Iterable


Vector3 = tuple[float, float, float]


@dataclass(frozen=True)
class BankAxes:
    left: Vector3
    right: Vector3


def _norm(vector: Vector3) -> float:
    return sqrt(sum(component * component for component in vector))


def bank_axis_unit_vectors(bank_angle_deg: float) -> BankAxes:
    """Return left/right cylinder-axis unit vectors for a symmetric V engine.

    Coordinate convention:
    +X right, +Y rear/crank axis, +Z up.
    The banks are symmetric about the X=0 engine center plane.
    """
    if not 0.0 < bank_angle_deg < 180.0:
        raise ValueError("bank_angle_deg must be between 0 and 180 degrees")
    half = bank_angle_deg * pi / 360.0
    s = sin(half)
    c = cos(half)
    return BankAxes(left=(-s, 0.0, c), right=(s, 0.0, c))


def center_spacing_from_bore_and_bridge_mm(bore_mm: float, bridge_mm: float) -> float:
    """Cylinder center spacing = bore + inter-cylinder bridge width."""
    if bore_mm <= 0:
        raise ValueError("bore_mm must be positive")
    if bridge_mm < 0:
        raise ValueError("bridge_mm must be non-negative")
    return bore_mm + bridge_mm


def bridge_width_from_spacing_mm(center_spacing_mm: float, bore_mm: float) -> float:
    """Return inter-cylinder bridge width implied by spacing and bore."""
    if bore_mm <= 0 or center_spacing_mm <= 0:
        raise ValueError("bore_mm and center_spacing_mm must be positive")
    bridge = center_spacing_mm - bore_mm
    if bridge < 0:
        raise ValueError("center spacing cannot be smaller than bore")
    return bridge


def longitudinal_cylinder_centers_mm(
    front_center_y_mm: float,
    center_spacing_mm: float,
    count: int = 4,
) -> tuple[float, ...]:
    """Generate longitudinal cylinder-center Y coordinates for one bank."""
    if center_spacing_mm <= 0:
        raise ValueError("center_spacing_mm must be positive")
    if count <= 0:
        raise ValueError("count must be positive")
    return tuple(front_center_y_mm + index * center_spacing_mm for index in range(count))


def paired_bank_cylinder_centers_mm(
    left_front_center_y_mm: float,
    center_spacing_mm: float,
    right_minus_left_offset_mm: float,
    count: int = 4,
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    """Generate left/right bank longitudinal centers with explicit bank stagger."""
    left = longitudinal_cylinder_centers_mm(left_front_center_y_mm, center_spacing_mm, count)
    right_front = left_front_center_y_mm + right_minus_left_offset_mm
    right = longitudinal_cylinder_centers_mm(right_front, center_spacing_mm, count)
    return left, right


def point_along_axis_mm(base_point: Vector3, axis_unit: Vector3, distance_mm: float) -> Vector3:
    """Return base_point + distance * axis_unit.

    Useful for constructing a deck-plane reference point from a governed
    cylinder-axis base point and deck height. The caller owns the axis base
    point; this function therefore does not assume zero bore offset.
    """
    norm = _norm(axis_unit)
    if abs(norm - 1.0) > 1e-9:
        raise ValueError("axis_unit must be normalized")
    return tuple(base + distance_mm * direction for base, direction in zip(base_point, axis_unit))  # type: ignore[return-value]


def side_by_side_rod_center_separation_mm(
    left_big_end_width_mm: float,
    right_big_end_width_mm: float,
    inter_rod_side_clearance_mm: float,
) -> float:
    """Candidate center-plane separation for equal-journal side-by-side rods.

    separation = left_width/2 + clearance + right_width/2

    This is architecture-dependent and must not be used for fork-and-blade or
    other rod arrangements.
    """
    if left_big_end_width_mm <= 0 or right_big_end_width_mm <= 0:
        raise ValueError("rod big-end widths must be positive")
    if inter_rod_side_clearance_mm < 0:
        raise ValueError("inter_rod_side_clearance_mm must be non-negative")
    return (
        left_big_end_width_mm / 2.0
        + inter_rod_side_clearance_mm
        + right_big_end_width_mm / 2.0
    )


def plane_normal_for_crank_normal_plane() -> Vector3:
    """Flywheel/pulley plane normal under the +Y crank-axis convention."""
    return (0.0, 1.0, 0.0)


def engine_center_plane_normal() -> Vector3:
    """Engine longitudinal center-plane normal under the +X right convention."""
    return (1.0, 0.0, 0.0)


def assert_unit_vectors(vectors: Iterable[Vector3]) -> None:
    """Raise when any supplied vector is not unit length; useful for validators."""
    for vector in vectors:
        if abs(_norm(vector) - 1.0) > 1e-9:
            raise ValueError(f"not a unit vector: {vector}")
