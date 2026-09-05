# Changelog

All notable engineering-baseline changes are recorded here.

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
