# Dimensional Model — Audit 0.3

**Phase:** 1 — Dimensional Reconstruction  
**Status:** ACTIVE / NOT VALIDATED  
**Primary detail:** `docs/dimensional_reconstruction.md`

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
| Displacement label | 5.7 L / 350 CID | REFERENCE / NOMINAL |
| Compression-ratio label | 10.0:1 | REFERENCE / UNVERIFIED |

## Derived values from visible bore/stroke

- crank radius = `44.45 mm`
- bank half-angle = `45°`
- displacement per cylinder = `720.740718 cc`
- total displacement = `5.765925746 L`
- total displacement = `351.858377 CID`

## Displacement authority remains open

Three mathematically coherent candidate modes are registered in `parameters/dimensional_constraints.yaml`:

1. preserve blueprint bore/stroke → `5.765926 L / 351.858 CID`;
2. preserve 101.6 mm bore and target exactly 350 CID → stroke `88.430465 mm`;
3. preserve 101.6 mm bore and target exactly 5.700 L → stroke `87.883546 mm`.

No mode is `LOCKED` yet.

## Governing relations now frozen

- `crank_radius = stroke / 2`
- `bank_half_angle = bank_angle / 2`
- `piston_operating_OD = bore - diametral_clearance`
- `deck_height = crank_radius + rod_length + compression_height + deck_clearance`
- `CR = (swept_volume + clearance_volume) / clearance_volume`

These relations may be authoritative even while their unresolved numeric inputs remain `UNKNOWN`.

## Critical blockers

- displacement authority selection
- cylinder center spacing
- bank longitudinal stagger
- deck stack closure
- piston operating clearance
- wrist-pin geometry
- crank journal dimensions
- crank station spacing/phasing
- camshaft axis location
- chamber/gasket/deck/piston-crown volume model
- flywheel/pulley reference planes

## Rule

Unknown dimensions remain explicit `UNKNOWN`; they are not silently invented to make the model fit.
