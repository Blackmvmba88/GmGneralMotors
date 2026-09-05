# Kinematics Framework

**Status:** Phase 1/3 development — cross-plane direction selected; cylinder-to-throw mapping and rod length unresolved.

## Master variable

The four-stroke engine cycle is controlled by:

`crank_angle ∈ [0°, 720°)`

The camshaft relation for a conventional four-stroke OHV architecture is:

`cam_angle = crank_angle / 2`

Therefore 720° crank rotation corresponds to 360° cam rotation.

## Development crank architecture

Baseline 0.5.0 proceeds with a **90° cross-plane crank as the development direction**.

This is not a production lock.

Development throw phase families:

```text
T0   =   0°
T90  =  90°
T180 = 180°
T270 = 270°
```

These phases describe crank geometry only. Cylinders have not yet been assigned to throws and no firing order is frozen.

See:

- `parameters/crank_architecture.yaml`
- `docs/crank_architecture_trade.md`
- `engineering/kinematics.py`

## Slider-crank baseline

Let:

- `r` = crank radius
- `l` = connecting-rod center-to-center length
- `θ` = crank angle including the throw phase

A standard zero-offset slider-crank center position is:

`x(θ) = r cos(θ) + sqrt(l² - r² sin²(θ))`

The engineering implementation is now executable in `engineering/kinematics.py`.

Piston travel from TDC is defined as:

`travel(θ) = (r + l) - x(θ)`

This gives:

- TDC travel = `0`
- BDC travel = `2r = stroke`
- mechanical piston position repeats every `360°`
- four-stroke combustion state still requires the full `720°` cycle

## Known kinematic parameter

`r = 44.45 mm` from the current development-authority 88.9 mm stroke.

## Still unknown

- connecting-rod length
- cylinder-to-throw mapping
- rod journal pairing strategy
- numeric cylinder numbering, if adopted
- firing order
- bank-specific journal/cylinder offsets
- piston pin offset, if any
- cam lobe timing
- crank station spacing
- bank longitudinal stagger

## Combustion-event cadence

For an evenly firing four-stroke V8:

`720° / 8 = 90° per combustion event`

This event spacing is a calculated target, not a firing-order definition.

## Engineering rule

Do not keyframe pistons independently. Piston, rod, valve and rocker motion must be downstream consequences of a common crank/cam state.

Do not assign a firing order merely because a known manufacturer uses it. Cylinder identity, journal mapping and crank phasing must agree first.

## Required 720° validation

The future rotating assembly must complete a continuous 720° cycle with:

- no constraint flips
- no discontinuities
- no unintended collisions
- no rod/piston inversion
- deterministic state at identical crank angles
- deterministic cylinder event state after firing order is frozen

## Current executable validation

Unit tests already check the geometry-level invariants using a non-authoritative test rod length:

- four cross-plane throw phases are unique;
- TDC travel is zero;
- BDC travel equals stroke;
- mechanical position repeats after 360°;
- invalid rod geometry is rejected.

The test rod length is deliberately not written into the engine parameter registry.
