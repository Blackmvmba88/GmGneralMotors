# V8 ENGINE — Engineering Roadmap

**Baseline:** 0.1.0  
**Current phase:** Phase 0 — Project Baseline  
**3D modeling:** LOCKED

## Phase 0 — Project baseline

Define the problem before defining geometry.

- [x] Units convention
- [x] Global XYZ convention
- [x] Front/rear convention
- [x] Primary datums
- [x] Naming convention
- [x] Repository architecture
- [x] Initial blueprint parameter registry
- [x] Parameter state model
- [x] Versioning policy
- [x] Component hierarchy
- [x] Validation framework
- [ ] Resolve all critical unknown dimensions
- [ ] Freeze crank phasing strategy
- [ ] Approve master skeleton specification

**Exit gate:** `BASELINE_READY`

## Phase 1 — Dimensional reconstruction

Convert the reference blueprint into a coherent dimensional system.

Required work:

- overall envelope audit
- bore/stroke/displacement audit
- deck geometry
- cylinder center spacing
- crank station spacing
- crank journal dimensions
- connecting-rod length
- piston compression height and wrist-pin geometry
- camshaft position
- head thickness and chamber envelope
- accessory/flywheel interface planes

No Blender. No aesthetic mesh work.

**Exit gate:** `DIMENSIONAL_MODEL_VALIDATED`

## Phase 2 — Master skeleton

Create the minimum authoritative geometry:

- crankshaft axis
- camshaft axis
- eight cylinder axes
- left/right deck planes
- front/rear planes
- crank stations
- flywheel plane
- pulley plane

All entities must be parameter-driven.

**Exit gate:** `SKELETON_LOCKED`

## Phase 3 — Rotating assembly

Build and validate:

1. crankshaft
2. connecting rods
3. pistons
4. wrist pins

Run a complete 0°–720° crank cycle without contradictory constraints, discontinuities, or unintended interference.

**Exit gate:** `ROTATING_ASSEMBLY_PASS`

## Phase 4 — Engine block

Order:

1. crankcase envelope
2. cylinder banks
3. bores
4. main-bearing region
5. deck surfaces
6. lifter valley
7. cam tunnel
8. lubrication envelope
9. head interface

**Exit gate:** `SHORT_BLOCK_STRUCTURAL_PASS`

## Phase 5 — Cylinder heads

Resolve one bank first, validate it, then derive the opposite side where symmetry permits.

- chamber envelope
- intake/exhaust valves
- seats and guides
- pushrod clearances
- rocker geometry
- head/block interface

**Exit gate:** `HEAD_SYSTEM_PASS`

## Phase 6 — Valvetrain

- camshaft
- lifters
- pushrods
- rockers
- valves
- springs

For a four-stroke engine: `cam_angle = crank_angle / 2`.

**Exit gate:** `VALVETRAIN_KINEMATIC_PASS`

## Phase 7 — Timing system

Define crank gear, cam gear, chain/drive strategy, tensioning envelope, and front cover interface.

**Exit gate:** `TIMING_PASS`

## Phase 8 — Lubrication

Define oil pan, pickup, pump, galleries, bearing feeds, and return paths.

**Exit gate:** `LUBRICATION_LAYOUT_PASS`

## Phase 9 — Cooling

Define water-jacket envelope, head passages, inlet/outlet, pump and thermostat interfaces.

**Exit gate:** `COOLING_LAYOUT_PASS`

## Phase 10 — Intake and exhaust

Define plenum, runners, throttle interface, injector positions, ports and exhaust-manifold/header interfaces.

**Exit gate:** `AIRFLOW_GEOMETRY_PASS`

## Phase 11 — Accessory drive

Define crank pulley, water pump, alternator, tensioners, pulleys and belt path.

**Exit gate:** `FRONT_DRIVE_PASS`

## Phase 12 — Complete assembly

Run:

- dimensional test
- alignment test
- symmetry test
- interference test
- envelope test
- full rotation test

**Exit gate:** `V8_ASSEMBLY_ALPHA`

## Phase 13 — Engineering detail

Only after functional geometry passes:

- fasteners
- bosses
- ribs
- gaskets
- passages
- threaded features
- production fillets
- casting detail

**Exit gate:** `V8_ASSEMBLY_BETA`

## Phase 14 — Blender entry gate

Blender becomes available for visualization after the engineering geometry is stable.

Blender responsibilities:

- materials
- shading
- animation
- cameras
- lighting
- exploded sequences
- cutaways
- technical/cinematic rendering

Blender is not the authority for master dimensions.

## Phase 15 — Digital twin visual

Generate front, rear, left, right, top, bottom, isometric, exploded and cutaway outputs.

## Phase 16 — Release

Target release: `V8_ENGINE_1.0.0`

Release must include source parameters, engineering geometry, validation reports, drawings, exports, renders and change history.

## Critical path

```text
PARAMETERS
  ↓
DATUMS
  ↓
MASTER SKELETON
  ↓
CRANKSHAFT
  ↓
ROD / PISTON
  ↓
BLOCK
  ↓
HEADS
  ↓
VALVETRAIN
  ↓
COMPLETE ASSEMBLY
```
