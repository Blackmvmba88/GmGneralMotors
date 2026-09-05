# Changelog

All notable engineering-baseline changes are recorded here.

## [0.6.0] — 2026-09-04

### Advanced

- master-skeleton geometry split into an executable relation layer and unresolved numeric handoff layer
- cylinder-axis directions made deterministic from bank angle
- cylinder center spacing made dependent on bore + explicit inter-cylinder bridge
- bank longitudinal stagger made explicit instead of hidden in placement
- bore-axis offset promoted to an explicit design decision
- cylinder longitudinal centers separated from crankpin station semantics

### Added

- `parameters/skeleton_relations.yaml`
- `engineering/skeleton.py`
- `tests/test_skeleton.py`
- executable bank-axis vector relations
- longitudinal cylinder-center generator
- cylinder spacing / bridge inverse relations
- explicit side-by-side rod center-separation candidate relation
- deck-plane point construction helper
- package-plane and engine-center-plane normals
- Phase 1 handoff relation/numeric split
- expanded skeleton specification

### Master parameter additions

- inter-cylinder bridge
- left-bank front cylinder datum
- explicit bank-offset convention
- bore-axis offset mode/value
- rod big-end width / inter-rod side clearance
- crank station position array
- OHV cam-axis direction relation
- package-plane normals

### Guardrails

- no cylinder spacing or bridge width invented
- no bank stagger invented
- no deck height invented
- no crank station position invented
- no zero bore-offset assumption made
- relation-layer readiness does not unlock CAD or Blender

## [0.5.0] — 2026-09-04

### Development direction

- selected `CROSS_PLANE_90_DEG` as the current crank development direction
- explicitly kept production lock disabled
- retained flat-plane as a future high-RPM variant path
- preserved bank-local cylinder IDs `L1–L4` / `R1–R4`
- left cylinder-to-throw mapping and firing order unresolved until they are mathematically coherent

### Added

- `parameters/crank_architecture.yaml`
- cross-plane vs flat-plane trade study
- deterministic slider-crank kinematics core
- cross-plane throw-phase family helper
- piston travel-from-TDC relation
- kinematics unit tests for TDC, BDC, stroke and 360° periodicity
- kinematics documentation tied to the 720° four-stroke cycle

### Calculated / frozen at development level

- cross-plane throw phase families: `0° / 90° / 180° / 270°`
- evenly firing V8 event cadence: `90°` crank per combustion event

### Guardrails

- no rod length was invented
- no cylinder-to-throw mapping was invented
- no firing order was frozen
- crank architecture remains a development direction rather than production authority
- CAD and Blender remain locked

## [0.4.0] — 2026-09-04

### Advanced

- explicit blueprint bore/stroke promoted to `DEVELOPMENT_AUTHORITY` for Phase 1 calculations
- visible `5.7 L / 350 CID` values retained as nominal labels rather than geometry authority
- production bore/stroke remain unlocked pending later durability, thermal, emissions, packaging and NVH evidence

### Added

- inverse engine-order crossing relation
- inverse quarter-wave geometry relation
- inverse Helmholtz cavity-volume relation
- inverse Helmholtz neck-area relation
- modal exclusion-band helper
- resonance geometry synthesis CLI
- resonance inverse-relation tests
- resonance geometry synthesis design contract
- material provenance registry contract
- material registry validator
- material selection / FEA evidence contract
- CI hooks for material provenance and resonance synthesis smoke tests

### Guardrails

- piston operating OD / wall clearance remains unresolved
- no material property values were invented
- no resonance-derived candidate geometry is treated as final without CFD/FEA/thermal/fatigue/manufacturing/test evidence
- CAD and Blender remain locked

## [0.3.0] — 2026-08-25

### Phase transition

- Phase 0 project baseline promoted to `BASELINE_READY`
- Phase 1 `DIMENSIONAL_RECONSTRUCTION` activated
- CAD / Blender remain locked

### Added

- authoritative dimensional-relation module
- executable dimensional audit and candidate CSV export
- dimensional unit tests
- `parameters/dimensional_constraints.yaml`
- explicit displacement-authority decision matrix
- exact calculations for visible bore/stroke geometry
- deck-stack relation
- piston/bore clearance relation
- compression-ratio dependency relation
- explicit bank longitudinal-offset unknown
- package-plane unknowns for flywheel and pulley
- CI hooks for dimensional audit

### Calculated

Visible blueprint geometry `101.6 mm × 88.9 mm × 8` derives to:

- `5.765925746 L`
- `351.858377 CID`
- `720.740718 cc` per cylinder
- crank radius `44.45 mm`
- bank half-angle `45°`

Alternative fixed-bore targets were calculated without selecting them:

- exact 350 CID → stroke `88.430465 mm`
- exact 5.700 L → stroke `87.883546 mm`

### Guardrails

- no displacement authority candidate is production-locked yet
- piston operating OD remains unknown until clearance is defined
- 10.0:1 compression ratio remains unverified until clearance-volume geometry is resolved
- missing skeleton dimensions remain explicit `UNKNOWN`

## [0.2.0] — 2026-08-25

### Added

- resonance/NVH as a first-class design system
- source/path/receiver energy-flow architecture
- documented import from `archimedes-quantum-resonance-engine`
- explicit separation between classical automotive NVH evidence and quantum research modules
- engine-order frequency utilities
- rectangular cavity-mode utilities
- quarter-wave and Helmholtz-resonator utilities
- Reynolds and Strouhal screening utilities
- SDOF natural-frequency and modal-separation utilities
- NVH target registry
- command-line NVH screening report
- resonance unit tests
- CI hooks for resonance tests and NVH screening
- new roadmap gates `NVH_BASELINE_READY` and `NVH_INTEGRATED_PASS`

### Design decision

Premium qualification will require measurable structural/acoustic behavior. The word `quantum` remains a research lineage identifier and is not treated as proof of an automotive performance mechanism.

## [0.1.0] — 2026-08-25

### Added

- repository engineering baseline
- operational README
- phased engineering roadmap
- technical modeling contract
- master and derived parameter registries
- dimensional-audit document
- coordinate and datum convention
- interface-control document
- kinematics framework
- validation gates
- master skeleton specification draft
- authoritative-geometry ADR
- automated parameter validator
- GitHub Actions validation workflow

### Known unresolved items

- exact 5.7 L label conflicts with calculated 5.766 L from visible bore/stroke values
- piston diameter reference equals bore and therefore cannot yet be interpreted as a locked operating OD
- connecting-rod length unknown
- cylinder center spacing unknown
- crank station spacing unknown
- journal sizes unknown
- deck height unknown
- head/chamber geometry unknown
- crank phasing and firing order not frozen
