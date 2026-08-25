# Changelog

All notable engineering-baseline changes are recorded here.

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
