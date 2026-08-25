# Kinematics Framework

**Status:** Draft — crank phasing and rod length unresolved.

## Master variable

The four-stroke engine cycle is controlled by:

`crank_angle ∈ [0°, 720°)`

The camshaft relation for a conventional four-stroke OHV architecture is:

`cam_angle = crank_angle / 2`

Therefore 720° crank rotation corresponds to 360° cam rotation.

## Slider-crank baseline

Let:

- `r` = crank radius
- `l` = connecting-rod center-to-center length
- `θ` = crank angle relative to the cylinder-axis reference

A standard zero-offset slider-crank center position can be represented as:

`x(θ) = r cos(θ) + sqrt(l² - r² sin²(θ))`

The project will define a datum-specific piston position convention before this equation is encoded into CAD expressions or animation drivers.

## Known kinematic parameter

`r = 44.45 mm` from the current 88.9 mm stroke reference.

## Unknown kinematic parameters

- connecting-rod length
- crank journal phases
- cylinder numbering-to-journal mapping
- firing order
- bank-specific angle offsets
- piston pin offset, if any
- cam lobe timing

## Engineering rule

Do not keyframe pistons independently. Piston, rod, valve and rocker motion must be downstream consequences of a common crank/cam state.

## Required 720° validation

The future rotating assembly must complete a continuous 720° cycle with:

- no constraint flips
- no discontinuities
- no unintended collisions
- no rod/piston inversion
- deterministic state at identical crank angles
