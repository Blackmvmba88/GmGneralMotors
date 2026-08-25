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
3. primary front reference plane

Every CAD/DCC export must preserve this convention or include an explicit transform document.

## Primary datums

| ID | Definition | Status |
|---|---|---|
| DATUM_A | Crankshaft centerline | LOCKED concept |
| DATUM_B | Engine longitudinal center plane | LOCKED concept |
| DATUM_C | Front reference plane | LOCKED concept |
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
