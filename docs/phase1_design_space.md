# Phase 1 Constrained Design Space

**Status:** SCREENING / DEVELOPMENT DECISION SUPPORT  
**CAD authority:** NO

## Purpose

Phase 1 has reached the point where several remaining unknowns cannot be
calculated from the current blueprint alone. Instead of copying dimensions from
another production engine, this project now explores explicit candidate spaces
and promotes a value only after the relevant structural, thermal, kinematic,
packaging and NVH evidence exists.

## 1. Cylinder packaging sweep

For the development bore:

`bore = 101.6 mm`

the relation is:

`center_spacing = bore + inter_cylinder_bridge`

Exploratory samples:

| Bridge mm | Spacing mm | L1→L4 center span mm | Residual vs 530 mm bank reference |
|---:|---:|---:|---:|
| 5.0 | 106.6 | 319.8 | 210.2 |
| 7.5 | 109.1 | 327.3 | 202.7 |
| 10.0 | 111.6 | 334.8 | 195.2 |
| 12.5 | 114.1 | 342.3 | 187.7 |
| 15.0 | 116.6 | 349.8 | 180.2 |

The residual column is **not** wall thickness or end clearance. The current
530 mm bank dimension is still a reference with unclear endpoints. This table
only shows sensitivity.

Before selecting a bridge, review at minimum:

- bore/liner architecture;
- coolant jacket requirement;
- head-gasket sealing land;
- head-bolt/stud corridor;
- casting/core feasibility;
- local stiffness and modal behavior;
- thermal gradient between adjacent cylinders.

## 2. Rod-ratio sweep

The relation is:

`rod_length = stroke × rod_to_stroke_ratio`

For `stroke = 88.9 mm`:

| Rod/stroke | Rod length mm |
|---:|---:|
| 1.60 | 142.240 |
| 1.65 | 146.685 |
| 1.70 | 151.130 |
| 1.75 | 155.575 |
| 1.80 | 160.020 |

These are mathematical sensitivity points, **not a recommended design range**.
A selected rod length must be reviewed against deck height, piston compression
height, skirt/package geometry, side thrust, peak acceleration, crankcase
clearance, mass and NVH.

## 3. RPM sensitivity

Mean piston speed:

`U_p = 2 × stroke × RPM / 60`

With `stroke = 88.9 mm`:

| RPM | Mean piston speed m/s | 4X firing frequency Hz |
|---:|---:|---:|
| 6000 | 17.780 | 400.000 |
| 6500 | 19.262 | 433.333 |
| 7000 | 20.743 | 466.667 |
| 7500 | 22.225 | 500.000 |
| 8000 | 23.707 | 533.333 |

The table does not define a safe redline. It exposes how an RPM decision moves
both mechanical speed and the primary evenly-firing V8 combustion-order line.

## 4. Bore-axis offset decision

For Phase 1 skeleton placement the project adopts:

`ZERO_OFFSET / 0.0 mm`

as a **DESIGN_TARGET**, not a production lock.

Rationale: zero offset is the neutral symmetric baseline and allows the
skeleton, kinematic and load-path models to advance without inventing a
side-thrust/friction strategy. A nonzero offset remains allowed later, but must
come with an explicit friction, piston-side-force, combustion, durability and
NVH case.

## Promotion rule

A screening candidate becomes authoritative only through the project's status
system:

`SCREENING_ONLY → DESIGN_TARGET → CALCULATED/VERIFIED → LOCKED`

No design-space table may be copied directly into authoritative CAD.
