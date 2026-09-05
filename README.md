# GmGneralMotors — Parametric V8 Engineering Project

> **Status:** PHASE 1 — DIMENSIONAL RECONSTRUCTION  
> **3D modeling:** LOCKED  
> **Blender:** LOCKED  
> **Baseline:** v0.5.0

This repository is the engineering source of truth for a modular, parametric V8 engine digital master. The goal is not to draw an engine by eye; it is to define enough geometry, interfaces, parameters, kinematics, resonance behavior, energy paths and validation rules that the engine becomes a reproducible consequence of the system.

## Engineering chain of authority

```text
MASTER PARAMETERS
      ↓
DIMENSIONAL RELATIONS
      ↓
MASTER SKELETON
      ↓
COMPONENT GEOMETRY
      ↓
STRUCTURAL / FLOW / NVH MODELS
      ↓
ASSEMBLY
      ↓
VALIDATION
      ↓
VISUAL / BLENDER MODEL
```

If a component only fits after manual nudging, scaling or arbitrary rotation, the error is upstream and must be fixed in the parameter, datum, constraint or interface definition.

If a structure is strong statically but lands on a harmful resonance in the operating envelope, it is **not** considered premium-ready.

## Current architecture

- V8
- 90° bank angle
- 8 cylinders / 4 per bank
- OHV / pushrod baseline
- longitudinal crankshaft
- **90° cross-plane crank — development direction, not production lock**
- liquid cooling
- wet-sump lubrication baseline
- central intake
- front accessory drive
- NVH / resonance treated as a first-class design system
- energy-path mapping from combustion source to structure, mounts, intake, exhaust and cabin

## Current phase — Dimensional reconstruction

The visual blueprint is being converted into a governed dimensional model.

Current visible bore/stroke:

- bore = `101.6 mm`
- stroke = `88.9 mm`
- cylinders = `8`

Derived exactly from those inputs:

- crank radius = `44.45 mm`
- bank half-angle = `45°`
- displacement = `5.765925746 L`
- displacement = `351.858377 CID`
- swept volume per cylinder = `720.740718 cc`

### Development dimensional authority

Phase 1 uses the explicit blueprint geometry `101.6 × 88.9 mm` as **DEVELOPMENT_AUTHORITY**. The visible `5.7 L / 350 CID` values are treated as nominal labels.

This is deliberately **not** a production manufacturing lock. Bore/stroke can still be revised later when durability, thermal, emissions, packaging, combustion and NVH evidence exists.

Alternative interpretations remain traceable:

1. development authority: `101.6 × 88.9 mm` → `5.765925746 L / 351.858377 CID`;
2. exact `350 CID` with bore fixed → stroke `88.430465 mm`;
3. exact `5.700 L` with bore fixed → stroke `87.883546 mm`.

Piston operating OD remains unresolved until a real piston-to-wall clearance is defined.

See:

- `docs/dimensional_reconstruction.md`
- `docs/dimensional_model.md`
- `parameters/dimensional_constraints.yaml`
- `engineering/dimensional.py`
- `scripts/dimensional_audit.py`

## Governing dimensional relations

The project can freeze equations before all numeric inputs are known.

```text
crank_radius = stroke / 2
bank_half_angle = bank_angle / 2
piston_operating_OD = bore - diametral_piston_clearance
deck_height = crank_radius + rod_length + compression_height + deck_clearance
compression_ratio = (swept_volume + clearance_volume) / clearance_volume
```

This allows uncertainty to stay explicit without allowing geometry to drift.

## Crank architecture development direction

Baseline 0.5.0 selects a **90° cross-plane crank** as the current development direction because the present program prioritizes controlled premium NVH, low fatigue/drone and deliberate low/mid-frequency character.

This choice accepts a higher counterweight/inertia burden in exchange for a more favorable development path for the current premium V8 objective. A flat-plane architecture remains explicitly preserved as a future high-RPM derivative path.

Development crank throw phase families:

```text
0° / 90° / 180° / 270°
```

This does **not** yet define cylinder-to-throw mapping or firing order.

The kinematics layer is now executable:

```text
x(θ) = r cos(θ) + sqrt(l² - r² sin²(θ))
travel_from_TDC = (r + l) - x(θ)
```

The tests verify TDC, BDC=stroke, 360° mechanical periodicity and cross-plane phase families without inventing an engine rod length.

See:

- `docs/crank_architecture_trade.md`
- `docs/kinematics.md`
- `parameters/crank_architecture.yaml`
- `engineering/kinematics.py`
- `tests/test_kinematics.py`

## Resonance / premium NVH policy

The project imports the **classical engineering layer** of `Blackmvmba88/archimedes-quantum-resonance-engine` as a research foundation for:

- FFT / spectral analysis
- harmonic distortion
- cavity modes
- pressure-field reasoning
- Reynolds / flow-regime checks
- Strouhal vortex-shedding frequency
- aero-acoustic coupling
- geometry-vs-resonance optimization

The quantum-matter modules remain a separate research domain. They are not used as evidence for a combustion-engine performance mechanism. Premium resonance claims must be backed by measurable classical structural dynamics, acoustics, fluid dynamics and test data.

### Frequency → geometry screening

The engineering layer can invert several resonance relations before CAD:

- target frequency → engine-order crossing RPM;
- target frequency → quarter-wave effective length;
- target frequency + neck geometry → Helmholtz cavity volume;
- target frequency + cavity geometry → Helmholtz neck area;
- natural frequency → provisional modal exclusion band.

These outputs are design candidates only. They do not become approved geometry until package, CFD/acoustic, structural, thermal, fatigue, manufacturing and physical validation gates pass.

See:

- `docs/nvh_resonance_architecture.md`
- `docs/nvh_engine_order_map.md`
- `docs/premium_acoustic_signature.md`
- `docs/structural_modal_analysis_plan.md`
- `docs/resonance_geometry_synthesis.md`
- `docs/research/archimedes_resonance_import.md`
- `parameters/nvh_targets.yaml`
- `engineering/resonance.py`
- `scripts/resonance_geometry_design.py`

## Material / FEA provenance policy

Authoritative simulation may not use anonymous `aluminum`, `steel`, `iron` or similar generic material labels.

`parameters/materials.yaml` defines the property and provenance contract required before the first credible modal/thermal model. Numeric properties must identify source, revision, temperature and status; damping additionally requires confidence metadata.

No material constants have been invented yet. Component assignments remain `UNKNOWN` until sourced candidates are reviewed.

See:

- `parameters/materials.yaml`
- `docs/material_selection.md`
- `scripts/validate_materials.py`

## Repository map

```text
.
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── V8_ENGINE_TECHNICAL_CONTRACT.md
├── docs/
│   ├── crank_architecture_trade.md
│   ├── dimensional_model.md
│   ├── dimensional_reconstruction.md
│   ├── skeleton_spec.md
│   ├── kinematics.md
│   ├── nvh_resonance_architecture.md
│   ├── nvh_engine_order_map.md
│   ├── premium_acoustic_signature.md
│   ├── structural_modal_analysis_plan.md
│   ├── resonance_geometry_synthesis.md
│   ├── material_selection.md
│   ├── validation.md
│   └── research/
├── engineering/
│   ├── dimensional.py
│   ├── kinematics.py
│   └── resonance.py
├── parameters/
│   ├── master_parameters.yaml
│   ├── crank_architecture.yaml
│   ├── derived_parameters.yaml
│   ├── dimensional_constraints.yaml
│   ├── materials.yaml
│   └── nvh_targets.yaml
├── scripts/
│   ├── dimensional_audit.py
│   ├── engine_order_map.py
│   ├── nvh_screen.py
│   ├── resonance_geometry_design.py
│   ├── validate_materials.py
│   └── validate_parameters.py
├── tests/
│   ├── test_dimensional.py
│   ├── test_kinematics.py
│   └── test_resonance.py
└── .github/workflows/
    └── validate.yml
```

CAD and Blender source directories will be introduced only after their design-definition gates are passed.

## Modeling maturity

- **L0 — Envelope:** bounding volumes only
- **L1 — Functional skeleton:** axes, datums, interfaces, pivots
- **L2 — Mechanical geometry:** functional solids and moving relationships
- **L2-NVH — Dynamic screening:** dominant engine orders, modal separation, flow resonance and energy-path review
- **L3 — Production detail:** bosses, ribs, holes, passages, fasteners, fillets
- **L4 — Visual detail:** materials, finishes, logos, cosmetic detail

No L4 work is permitted before the relevant system passes L2 and its applicable NVH gate.

## First modeling target

The first authoritative 3D object will still be `V8_MASTER_SKELETON`, not the engine block.

It must define at minimum:

- crankshaft axis
- camshaft axis
- eight cylinder axes
- left/right deck planes
- bank angle
- crank stations
- front/rear datums
- flywheel plane
- pulley plane

Phase 1 exists specifically to close the numeric inputs needed to create that skeleton without visual guesswork.

## Current gates

Completed:

- [x] conceptual blueprint
- [x] source-of-truth policy
- [x] component hierarchy
- [x] coordinate convention
- [x] technical contract
- [x] parameter registry
- [x] dimensional dependency model
- [x] executable dimensional audit
- [x] development displacement authority selected
- [x] cross-plane crank selected as development direction
- [x] executable slider-crank kinematics core
- [x] interface-control framework
- [x] resonance/NVH architecture
- [x] engine-order screening
- [x] inverse resonance geometry screening
- [x] premium acoustic design intent
- [x] material provenance contract
- [x] automated engineering tests

Still blocking authoritative CAD:

- [ ] critical spatial dimensions resolved
- [ ] piston/deck stack resolved
- [ ] piston operating clearance resolved
- [ ] operating RPM envelope frozen
- [ ] cylinder-to-throw mapping frozen
- [ ] firing order frozen
- [ ] crank station / bank stagger geometry frozen
- [ ] master skeleton specification frozen
- [ ] sourced material properties selected for modal analysis
- [ ] modal-analysis boundary inputs available
- [ ] design baseline promoted to 1.0.0

## Rule

> **Geometry is the consequence of the system; premium behavior is the consequence of controlled energy flow.**

Until the dimensional model, skeleton and applicable resonance gates are approved: **do not model the engine by eye.**
