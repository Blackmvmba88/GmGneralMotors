# Coordinate System and Datums

## Global axes

```text
X = left / right
Y = front / rear
Z = down / up
```

Directions:

- front = `Y-`
- rear = `Y+`
- left bank = `X-`
- right bank = `X+`
- up = `Z+`
- down = `Z-`

## Global origin

The authoritative origin is the intersection of:

1. crankshaft centerline
2. longitudinal engine center plane
3. `DATUM_C` — the left-bank front-cylinder center plane

Every CAD/DCC export must preserve this convention or include an explicit transform document.

### Why DATUM_C is Y = 0

This is a coordinate definition, not a claimed physical clearance. Locking the left-bank front-cylinder center plane to `Y = 0.0 mm` removes one arbitrary placement degree of freedom while leaving the actual front package, pulley and accessory planes free to be solved later.

Because bank stagger is still unresolved, the right-bank front cylinder is **not** assumed to share `Y = 0`; its position remains `bank_longitudinal_offset_mm` from DATUM_C.

For the symmetric OHV development baseline, the camshaft axis is also constrained to the engine longitudinal center plane at `X = 0.0 mm`. Its vertical `Z` position remains unresolved.

## Primary datums

| ID | Definition | Status |
|---|---|---|
| DATUM_A | Crankshaft centerline | LOCKED concept |
| DATUM_B | Engine longitudinal center plane | LOCKED concept |
| DATUM_C | Left-bank front-cylinder center plane, `Y = 0.0 mm` | LOCKED datum |
| DATUM_D | Left deck plane | position TBD |
| DATUM_E | Right deck plane | position TBD |
| DATUM_F | Flywheel mounting plane | position TBD |

## Bank geometry

For a 90° included bank angle, the nominal cylinder-axis orientation is ±45° from the engine center plane when represented symmetrically.

The actual deck offsets remain parameter-dependent and must not be inferred from the illustration alone.

## Export policy

Fusion 360 and Blender must agree on:

- unit scale
- handedness
- origin
- axis mapping
- forward/up convention

A mesh that visually matches but changes the mechanical origin is not an authoritative engineering export.
