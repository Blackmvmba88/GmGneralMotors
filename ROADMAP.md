# V8 ENGINE — Engineering Roadmap

**Baseline:** 0.2.0  
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
- [x] Resonance / NVH treated as first-class architecture
- [x] Classical resonance research import documented
- [ ] Resolve all critical unknown dimensions
- [ ] Freeze crank phasing strategy
- [ ] Freeze operating RPM envelope
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

## Gate R0 — Resonance and energy-flow baseline

This gate runs before authoritative structural geometry is frozen.

Required work:

- define operating RPM range
- generate engine-order map across RPM
- identify dominant combustion, rotating, reciprocating and valvetrain excitations
- define preliminary modal-separation screening margin
- map source → path → receiver energy routes
- classify surfaces likely to behave as radiators
- identify intake/exhaust cavity and quarter-wave risks
- identify vortex-shedding / aero-acoustic risks
- define premium sound-signature objectives separately from structural safety objectives

Imported research foundations:

- FFT / spectra / THD
- rectangular acoustic modes
- Reynolds number
- Strouhal frequency
- Lighthill/Curle scaling concepts
- geometry-versus-resonance optimization

**Exit gate:** `NVH_BASELINE_READY`

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

Add a torsional-excitation map before freezing crank geometry.

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

Before detail freeze, perform the first structural modal study and identify antinodes that may require ribs, local stiffness changes or mass redistribution.

**Exit gate:** `SHORT_BLOCK_STRUCTURAL_PASS`

## Phase 5 — Cylinder heads

Resolve one bank first, validate it, then derive the opposite side where symmetry permits.

- chamber envelope
- intake/exhaust valves
- seats and guides
- pushrod clearances
- rocker geometry
- head/block interface
- head-cover and deck radiation risk

**Exit gate:** `HEAD_SYSTEM_PASS`

## Phase 6 — Valvetrain

- camshaft
- lifters
- pushrods
- rockers
- valves
- springs

For a four-stroke engine: `cam_angle = crank_angle / 2`.

Add valve-event/order excitation to the NVH map.

**Exit gate:** `VALVETRAIN_KINEMATIC_PASS`

## Phase 7 — Timing system

Define crank gear, cam gear, chain/drive strategy, tensioning envelope, front cover interface and tonal-whine risk.

**Exit gate:** `TIMING_PASS`

## Phase 8 — Lubrication

Define oil pan, pickup, pump, galleries, bearing feeds, return paths and sump-panel vibration risk.

**Exit gate:** `LUBRICATION_LAYOUT_PASS`

## Phase 9 — Cooling

Define water-jacket envelope, head passages, inlet/outlet, pump and thermostat interfaces. Review pump/blade-pass excitation and coolant-flow pulsation where applicable.

**Exit gate:** `COOLING_LAYOUT_PASS`

## Phase 10 — Intake and exhaust

Define plenum, runners, throttle interface, injector positions, ports and exhaust-manifold/header interfaces.

This phase explicitly includes:

- runner tuning
- plenum/cavity modes
- quarter-wave behavior
- Helmholtz resonator opportunities
- exhaust pulse timing
- desired acoustic signature
- unwanted drone bands

**Exit gate:** `AIRFLOW_GEOMETRY_PASS`

## Phase 11 — Accessory drive

Define crank pulley, water pump, alternator, tensioners, pulleys and belt path. Add accessory orders and blade/slot-pass frequencies to the excitation map.

**Exit gate:** `FRONT_DRIVE_PASS`

## Gate R1 — Integrated NVH screening

Before complete-assembly alpha:

- structural modal analysis
- harmonic-response screening
- torsional screening
- mount-path review
- intake/exhaust acoustic review
- radiator-panel review
- resonance coincidences ranked by severity

**Exit gate:** `NVH_INTEGRATED_PASS`

## Phase 12 — Complete assembly

Run:

- dimensional test
- alignment test
- symmetry test
- interference test
- envelope test
- full rotation test
- NVH integrated pass

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

Ribs and wall thickness changes must be justified by load path, casting/manufacturing constraints, modal response or thermal need—not decoration.

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
- optional visualizations of mode shapes and energy paths

Blender is not the authority for master dimensions or structural resonance claims.

## Phase 15 — Digital twin visual

Generate front, rear, left, right, top, bottom, isometric, exploded and cutaway outputs.

The digital twin should eventually carry measured or simulated NVH metadata per configuration.

## Phase 16 — Release

Target release: `V8_ENGINE_1.0.0`

Release must include source parameters, engineering geometry, validation reports, drawings, exports, renders, change history and an NVH evidence package.

## Critical path

```text
PARAMETERS
  ↓
DATUMS
  ↓
DIMENSIONAL MODEL
  ↓
NVH BASELINE / ORDER MAP
  ↓
MASTER SKELETON
  ↓
CRANKSHAFT
  ↓
ROD / PISTON
  ↓
BLOCK + MODAL STUDY
  ↓
HEADS / VALVETRAIN
  ↓
INTAKE / EXHAUST ACOUSTICS
  ↓
INTEGRATED NVH PASS
  ↓
COMPLETE ASSEMBLY
```
