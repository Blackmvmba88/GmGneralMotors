# Master Skeleton Specification

**Object:** `V8_MASTER_SKELETON`  
**Status:** RELATION LAYER READY / NUMERIC INPUTS NOT FROZEN

## Purpose

The skeleton is the smallest geometric object from which the major engine assembly can be derived without visual guesswork.

Baseline 0.6.0 separates two questions:

1. **What relation defines an entity?** — now executable where possible.
2. **What numeric input positions it?** — remains `UNKNOWN` until sourced, derived or explicitly selected.

## Global coordinate frame

```text
+X = right
+Y = rear / crankshaft longitudinal direction
+Z = up
```

Authoritative relation normals:

- crank axis direction: `(0, 1, 0)`
- flywheel / pulley plane normal: `(0, 1, 0)`
- engine longitudinal center-plane normal: `(1, 0, 0)`

## Required entities

### Global

- `AXIS_CRANK`
- `AXIS_CAM`
- `PLANE_ENGINE_CENTER`
- `PLANE_FRONT`
- `PLANE_REAR`
- `PLANE_FLYWHEEL`
- `PLANE_PULLEY`

### Left bank

- `AXIS_CYL_L1`
- `AXIS_CYL_L2`
- `AXIS_CYL_L3`
- `AXIS_CYL_L4`
- `PLANE_DECK_LEFT`

### Right bank

- `AXIS_CYL_R1`
- `AXIS_CYL_R2`
- `AXIS_CYL_R3`
- `AXIS_CYL_R4`
- `PLANE_DECK_RIGHT`

### Crank stations

Four crankpin phase families are now defined by the cross-plane development direction, but longitudinal crankpin station planes remain unresolved until cylinder-to-throw mapping, rod-journal pairing, bank stagger and crank station geometry are frozen.

Do not equate a cylinder longitudinal center with a crankpin station by default.

## Executable bank-axis relation

For bank angle `β`:

`α = β / 2`

Left cylinder-axis direction:

`u_L = (-sin α, 0, cos α)`

Right cylinder-axis direction:

`u_R = (+sin α, 0, cos α)`

For the current 90° V8 reference:

`α = 45°`

The deck plane normal for each bank is the corresponding cylinder-axis unit vector.

Implementation:

- `engineering/skeleton.py::bank_axis_unit_vectors`

## Cylinder spacing relation

Do not select center spacing by appearance.

The relation is:

`cylinder_center_spacing = bore + inter_cylinder_bridge`

Current bore is development-authority `101.6 mm`; the bridge width remains unresolved.

Therefore center spacing remains unresolved.

Implementation:

- `center_spacing_from_bore_and_bridge_mm`
- `bridge_width_from_spacing_mm`

## Longitudinal cylinder centers

For one bank:

`Y_i = Y_front + i × spacing`, for `i = 0..3`

For the right bank:

`Y_front_right = Y_front_left + bank_offset_right_minus_left`

The bank offset is an explicit parameter. It is not hidden inside the cylinder sequence.

Implementation:

- `longitudinal_cylinder_centers_mm`
- `paired_bank_cylinder_centers_mm`

## Bank stagger relation candidate

If the final common-crankpin architecture uses side-by-side rods, a first geometric relation for rod-center separation is:

`offset = left_big_end_width/2 + inter_rod_clearance + right_big_end_width/2`

This relation is **architecture-dependent**. It is not valid for fork-and-blade or other rod arrangements.

It is therefore a candidate relation, not an authoritative bank-offset value.

## Deck reference construction

A deck plane can be generated from:

- a governed point on the cylinder axis;
- the bank cylinder-axis unit vector;
- deck height measured along that axis.

`P_deck = P_axis_base + deck_height × u_bank`

The caller owns `P_axis_base`. This is deliberate: the project has **not** yet selected zero bore offset versus deliberate cylinder-axis/crank offset.

Implementation:

- `point_along_axis_mm`

## Bore-axis offset policy

Do not assume all cylinder axes intersect the crankshaft centerline.

The project must explicitly select either:

- zero bore offset; or
- a nonzero offset architecture with signed magnitude and rationale.

Until then, bore-axis offset remains `UNKNOWN`.

## Cam axis relation

For the current central OHV development baseline:

- cam axis is parallel to crank axis;
- direction = `(0, 1, 0)`.

Its actual X/Z position remains unresolved.

The Y coordinate does not independently locate an infinite axis parallel to Y; package references may still define finite feature extents later.

## Required numeric parameter inputs before lock

- inter-cylinder bridge or verified cylinder center spacing
- front cylinder-center longitudinal datum
- bank longitudinal stagger
- bore-axis offset architecture/value
- deck height
- crank station positions / spacing
- rod-journal pairing geometry
- cam axis X/Z location
- flywheel plane Y
- pulley plane Y
- front/rear package limits

## Relation sources

- `parameters/skeleton_relations.yaml`
- `engineering/skeleton.py`
- `tests/test_skeleton.py`
- `parameters/master_parameters.yaml`
- `parameters/crank_architecture.yaml`

## Lock conditions

The relation layer may be considered ready while numeric inputs remain unknown.

The actual `V8_MASTER_SKELETON` cannot become `LOCKED` until:

- every required spatial input has a governed value;
- cylinder-to-throw and crank station semantics agree;
- bore-offset architecture is explicit;
- package planes are resolved;
- parameter and relation validators agree;
- no manual translation/rotation is required to make entities fit.

## Modeling prohibition

Do not use decorative engine surfaces as parents for skeleton entities. Surfaces are downstream of the skeleton, never the other way around.

Do not open authoritative CAD merely because the relations are executable; the numeric gate still applies.
