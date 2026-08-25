# Dimensional Model — Audit 0.1

## Purpose

Separate what is visible in the current blueprint from what is mathematically derived and what remains unknown.

## Reference values

| Parameter | Value | State |
|---|---:|---|
| Bore | 101.6 mm | REFERENCE |
| Stroke | 88.9 mm | REFERENCE |
| Bank angle | 90° | REFERENCE |
| Cylinders | 8 | LOCKED architecture |
| Overall width | 680 mm | REFERENCE |
| Overall length | 810 mm | REFERENCE |
| Overall height | 620 mm | REFERENCE |
| Bank reference length | 530 mm | REFERENCE |
| Bank reference height | 255 mm | REFERENCE |
| Piston diameter label | 101.6 mm | REFERENCE / AMBIGUOUS |
| Piston height label | 64.8 mm | REFERENCE |
| Displacement label | 5.7 L | REFERENCE / NOMINAL |

## Derived checks

### Crank radius

`r = stroke / 2`

`r = 88.9 / 2 = 44.45 mm`

### Displacement

For eight equal cylinders:

`V = (π/4) × bore² × stroke × 8`

Using 101.6 mm bore and 88.9 mm stroke:

`V ≈ 5.765926 L`

This differs from the 5.7 L label by about 0.0659 L or 1.16%. For now the label is treated as a nominal family value, not a contradictory hard failure.

### Piston/bore issue

A piston reference diameter of 101.6 mm exactly matching a 101.6 mm bore produces zero nominal radial clearance if both numbers are interpreted as finished operating diameters. That is not acceptable as a locked functional assumption.

Therefore:

- bore remains `REFERENCE`
- piston diameter remains `REFERENCE / AMBIGUOUS`
- operating piston OD remains unresolved
- clearance must be introduced only from a validated design target

## Critical unknowns before skeleton lock

- cylinder center spacing
- deck height relative to crank axis
- crank station spacing
- main journal diameter
- rod journal diameter
- crank phasing
- connecting-rod center-to-center length
- piston compression height
- wrist-pin diameter/location
- camshaft axis location
- head thickness
- chamber geometry
- valve included angle/orientation
- flywheel plane
- front pulley plane

## Rule

Unknown dimensions remain explicit `UNKNOWN`; they are not silently invented to make the model fit.
