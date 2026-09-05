# V8 ENGINE — Engineering Roadmap

**Baseline:** 0.4.0  
**Current phase:** Phase 1 — Dimensional Reconstruction  
**3D modeling:** LOCKED

## Phase 0 — Project baseline ✅

Define the problem before defining geometry.

Completed:

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
- [x] Critical unknown register established
- [x] Phase/gate ownership defined

The unresolved dimensions, crank phasing, RPM envelope and skeleton geometry are intentionally carried into their owning downstream phases instead of blocking the project-baseline freeze.

**Exit gate:** `BASELINE_READY` — PASS

## Phase 1 — Dimensional reconstruction 🔄

Convert the reference blueprint into a coherent dimensional system.

Completed:

- [x] bore/stroke/displacement audit
- [x] exact displacement derived from visible geometry
- [x] displacement authority alternatives calculated
- [x] blueprint bore/stroke selected as `DEVELOPMENT_AUTHORITY`
- [x] production lock explicitly withheld
- [x] crank-radius relation frozen
- [x] bank half-angle relation frozen
- [x] piston/bore clearance relation frozen
- [x] deck-stack relation frozen
- [x] compression-ratio dependency relation frozen
- [x] executable dimensional audit added
- [x] dimensional unit tests added

Still required:

- [ ] close overall envelope interpretation
- [ ] define cylinder center spacing
- [ ] define longitudinal bank stagger
- [ ] close deck stack
- [ ] resolve piston operating clearance / wrist pin
- [ ] define crank journal dimensions
- [ ] define crank station spacing
- [ ] define connecting-rod length
- [ ] define camshaft position
- [ ] define head thickness and chamber volume model
- [ ] define gasket/deck/piston-crown volume inputs
- [ ] define accessory/flywheel interface planes
- [ ] attach provenance/status to every critical input

No Blender. No aesthetic mesh work.

**Exit gate:** `DIMENSIONAL_MODEL_VALIDATED`

## Gate R0 — Resonance and energy-flow baseline 🔄

This gate runs in parallel with Phase 1 before authoritative structural geometry is frozen.

Completed:

- [x] engine-order map generator
- [x] source → path → receiver architecture
- [x] preliminary modal-separation screening
- [x] premium acoustic-signature design intent
- [x] structural modal/harmonic analysis plan
- [x] intake/exhaust resonance model families identified
- [x] inverse engine-order crossing relation
- [x] inverse quarter-wave geometry relation
- [x] inverse Helmholtz geometry relations
- [x] resonance geometry synthesis CLI
- [x] modal exclusion-band screening helper

Still required:

- [ ] freeze operating RPM range
- [ ] freeze crank phasing/firing order
- [ ] add rotating/reciprocating force-order amplitudes
- [ ] add valvetrain event families
- [ ] add accessory speed/blade/tooth-pass families
- [ ] define benchmark-derived premium numeric targets

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

The skeleton may not be frozen until Phase 1 supplies every required spatial input.

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

Before detail freeze:

- use an explicit sourced material-set revision;
- perform the first structural modal study;
- identify antinodes that may require ribs, local stiffness changes or mass redistribution;
- record boundary conditions, mesh evidence and damping confidence.

The material provenance schema and validator are already established in baseline 0.4.0; numeric material properties remain intentionally unresolved until sourced.

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
- frequency-to-geometry screening candidates generated before CAD freeze

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
PROJECT BASELINE ✅
  ↓
DIMENSIONAL RECONSTRUCTION ← CURRENT
  ↘
   NVH BASELINE / RESONANCE SYNTHESIS
  ↓
MASTER SKELETON
  ↓
CRANKSHAFT
  ↓
ROD / PISTON
  ↓
BLOCK + SOURCED MATERIAL SET + MODAL STUDY
  ↓
HEADS / VALVETRAIN
  ↓
INTAKE / EXHAUST ACOUSTICS
  ↓
INTEGRATED NVH PASS
  ↓
COMPLETE ASSEMBLY
```
