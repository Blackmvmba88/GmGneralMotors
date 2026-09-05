# V8 ENGINE — Engineering Roadmap

**Baseline:** 0.6.0  
**Current phase:** Phase 1 — Dimensional Reconstruction  
**3D modeling:** LOCKED

## Phase 0 — Project baseline ✅

Completed:

- [x] units / coordinate conventions / datums
- [x] naming / repository / versioning policy
- [x] component hierarchy and validation framework
- [x] resonance / NVH as first-class architecture
- [x] critical unknown register and phase/gate ownership

**Exit gate:** `BASELINE_READY` — PASS

## Phase 1 — Dimensional reconstruction 🔄

Completed:

- [x] bore/stroke/displacement audit
- [x] blueprint bore/stroke selected as `DEVELOPMENT_AUTHORITY`
- [x] production lock explicitly withheld
- [x] crank radius / bank half-angle relations
- [x] piston/bore clearance relation
- [x] deck-stack / compression-ratio relations
- [x] executable dimensional audit and tests
- [x] 90° cross-plane crank selected as development direction
- [x] master-skeleton **spatial relation layer** formalized
- [x] cylinder-axis vectors mathematically defined
- [x] cylinder-spacing relation defined as `bore + bridge`
- [x] longitudinal cylinder-center relation defined
- [x] deck-plane construction relation defined
- [x] bore-axis offset made an explicit design decision
- [x] cylinder centers separated conceptually from crankpin stations

Still required:

- [ ] close overall envelope interpretation
- [ ] select inter-cylinder bridge / center spacing
- [ ] select front cylinder longitudinal datum
- [ ] define bank longitudinal stagger
- [ ] select zero/nonzero bore-axis offset and value
- [ ] close deck / rod / piston stack
- [ ] resolve piston operating clearance / wrist pin
- [ ] define crank journal dimensions and station positions
- [ ] define connecting-rod dimensions
- [ ] define camshaft X/Z position
- [ ] define head / chamber / gasket / crown-volume inputs
- [ ] define accessory/flywheel interface planes
- [ ] attach provenance/status to every critical input

No Blender. No authoritative CAD.

**Exit gate:** `DIMENSIONAL_MODEL_VALIDATED`

## Gate R0 — Resonance and energy-flow baseline 🔄

Completed:

- [x] engine-order map generator
- [x] source → path → receiver architecture
- [x] preliminary modal-separation screening
- [x] premium acoustic-signature intent
- [x] structural modal/harmonic plan
- [x] inverse quarter-wave / Helmholtz / engine-order relations
- [x] resonance geometry synthesis CLI
- [x] cross-plane vs flat-plane NVH development direction

Still required:

- [ ] freeze operating RPM range
- [ ] freeze cylinder-to-throw mapping and firing order
- [ ] add rotating/reciprocating force-order amplitudes
- [ ] add valvetrain event families
- [ ] add accessory speed/blade/tooth-pass families
- [ ] define benchmark-derived premium numeric targets

**Exit gate:** `NVH_BASELINE_READY`

## Phase 2 — Master skeleton 🔄 RELATION LAYER READY

Required entities:

- crankshaft axis
- camshaft axis
- eight cylinder axes
- left/right deck planes
- front/rear reference planes
- crank station planes
- flywheel plane
- pulley plane

### Completed before CAD

- [x] bank-axis direction equations
- [x] deck normal equations
- [x] cylinder-spacing dependency
- [x] longitudinal center-generation relation
- [x] explicit bank-stagger convention
- [x] explicit bore-axis offset policy
- [x] crank-normal package-plane normals
- [x] cam-axis parallelism relation for OHV baseline
- [x] executable relation helper module
- [x] skeleton relation unit tests
- [x] Phase 1 handoff split into relation layer vs numeric layer

### Numeric handoff still required

- [ ] center spacing / bridge
- [ ] front cylinder datum
- [ ] bank stagger
- [ ] bore-axis offset mode/value
- [ ] deck height
- [ ] cam axis X/Z
- [ ] crank station map
- [ ] cylinder-to-throw / rod-journal mapping
- [ ] flywheel / pulley Y positions

The relation layer being ready does **not** unlock CAD.

**Exit gate:** `SKELETON_LOCKED`

## Phase 3 — Rotating assembly 🔄 PREPARATION

Completed:

- [x] 90° cross-plane development direction
- [x] throw phases `0° / 90° / 180° / 270°`
- [x] executable zero-offset slider-crank relation
- [x] TDC / BDC / stroke / 360° periodicity tests
- [x] evenly firing four-stroke event cadence = `90°`

Still required:

- [ ] connecting-rod center-to-center length
- [ ] cylinder-to-throw mapping
- [ ] rod-journal pairing
- [ ] firing order
- [ ] crank station spacing / bank stagger
- [ ] journal diameters
- [ ] counterweight strategy
- [ ] rotating / reciprocating mass model
- [ ] torsional excitation map
- [ ] damper strategy

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

Before detail freeze use an explicit sourced material-set revision and perform structural modal analysis with boundary/mesh/damping provenance.

**Exit gate:** `SHORT_BLOCK_STRUCTURAL_PASS`

## Phase 5 — Cylinder heads

Resolve one bank, validate, then derive the opposite side where symmetry permits.

**Exit gate:** `HEAD_SYSTEM_PASS`

## Phase 6 — Valvetrain

For a four-stroke engine: `cam_angle = crank_angle / 2`.

Add valve-event/order excitation to the NVH map.

**Exit gate:** `VALVETRAIN_KINEMATIC_PASS`

## Phase 7 — Timing system

Define crank/cam drive, tensioning, front cover and tonal-whine risk.

**Exit gate:** `TIMING_PASS`

## Phase 8 — Lubrication

Define pan, pickup, pump, galleries, feeds, returns and sump-panel vibration risk.

**Exit gate:** `LUBRICATION_LAYOUT_PASS`

## Phase 9 — Cooling

Define water-jacket envelope, passages, pump and thermostat interfaces; review flow pulsation and blade-pass excitation.

**Exit gate:** `COOLING_LAYOUT_PASS`

## Phase 10 — Intake and exhaust

Includes runner/plenum tuning, cavity modes, quarter-wave, Helmholtz opportunities, exhaust pulse timing, desired signature and anti-drone behavior.

Bank-specific pulse analysis starts after firing order is frozen.

**Exit gate:** `AIRFLOW_GEOMETRY_PASS`

## Phase 11 — Accessory drive

Define pulleys, belt path and accessory order/blade/tooth-pass families.

**Exit gate:** `FRONT_DRIVE_PASS`

## Gate R1 — Integrated NVH screening

Requires modal, harmonic, torsional, mount-path, intake/exhaust acoustic and radiator-panel review.

**Exit gate:** `NVH_INTEGRATED_PASS`

## Phase 12 — Complete assembly

Run dimensional, alignment, symmetry, interference, envelope, full-rotation and NVH checks.

**Exit gate:** `V8_ASSEMBLY_ALPHA`

## Phase 13 — Engineering detail

Fasteners, bosses, ribs, gaskets, passages, threaded features, production fillets and casting details only after functional validation.

**Exit gate:** `V8_ASSEMBLY_BETA`

## Phase 14 — Blender entry gate

Blender owns visualization, materials, animation, cameras, lighting, exploded/cutaway and mode/energy-path visualization. It does not own master dimensions or resonance claims.

## Phase 15 — Digital twin visual

Generate orthographic, isometric, exploded and cutaway outputs with future NVH metadata.

## Phase 16 — Release

Target: `V8_ENGINE_1.0.0`

## Critical path

```text
PROJECT BASELINE ✅
  ↓
DIMENSIONAL RECONSTRUCTION ← CURRENT
  ↘
   NVH / RESONANCE SYNTHESIS
  ↓
CROSS-PLANE DEVELOPMENT DIRECTION ✅
  ↓
SKELETON RELATION LAYER ✅
  ↓
NUMERIC SPATIAL HANDOFF
  ↓
CYLINDER ↔ THROW / FIRING ORDER
  ↓
MASTER SKELETON
  ↓
ROTATING ASSEMBLY
  ↓
BLOCK + MATERIAL SET + MODAL STUDY
  ↓
HEADS / VALVETRAIN
  ↓
INTAKE / EXHAUST ACOUSTICS
  ↓
INTEGRATED NVH PASS
  ↓
COMPLETE ASSEMBLY
```
