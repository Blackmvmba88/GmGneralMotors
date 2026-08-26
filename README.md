# GmGneralMotors — Parametric V8 Engineering Project

> **Status:** PHASE 1 — DIMENSIONAL RECONSTRUCTION  
> **3D modeling:** LOCKED  
> **Blender:** LOCKED  
> **Baseline:** v0.3.0

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

Therefore the visible `5.7 L / 350 CID` label remains nominal/reference until a displacement authority mode is selected.

Three candidate interpretations are tracked:

1. preserve blueprint geometry: `101.6 × 88.9 mm`;
2. preserve bore and target exactly `350 CID`: stroke `88.430465 mm`;
3. preserve bore and target exactly `5.700 L`: stroke `87.883546 mm`.

No candidate is silently promoted to `LOCKED`.

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

See:

- `docs/nvh_resonance_architecture.md`
- `docs/nvh_engine_order_map.md`
- `docs/premium_acoustic_signature.md`
- `docs/structural_modal_analysis_plan.md`
- `docs/research/archimedes_resonance_import.md`
- `parameters/nvh_targets.yaml`
- `engineering/resonance.py`

## Repository map

```text
.
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── V8_ENGINE_TECHNICAL_CONTRACT.md
├── docs/
│   ├── dimensional_model.md
│   ├── dimensional_reconstruction.md
│   ├── skeleton_spec.md
│   ├── kinematics.md
│   ├── nvh_resonance_architecture.md
│   ├── nvh_engine_order_map.md
│   ├── premium_acoustic_signature.md
│   ├── structural_modal_analysis_plan.md
│   ├── validation.md
│   └── research/
├── engineering/
│   ├── dimensional.py
│   └── resonance.py
├── parameters/
│   ├── master_parameters.yaml
│   ├── derived_parameters.yaml
│   ├── dimensional_constraints.yaml
│   └── nvh_targets.yaml
├── scripts/
│   ├── dimensional_audit.py
│   ├── engine_order_map.py
│   ├── nvh_screen.py
│   └── validate_parameters.py
├── tests/
│   ├── test_dimensional.py
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
- [x] interface-control framework
- [x] kinematic framework
- [x] resonance/NVH architecture
- [x] engine-order screening
- [x] premium acoustic design intent
- [x] automated engineering tests

Still blocking authoritative CAD:

- [ ] displacement authority mode selected
- [ ] critical spatial dimensions resolved
- [ ] piston/deck stack resolved
- [ ] operating RPM envelope frozen
- [ ] crank phasing / firing order frozen
- [ ] master skeleton specification frozen
- [ ] modal-analysis material/boundary inputs available
- [ ] design baseline promoted to 1.0.0

## Rule

> **Geometry is the consequence of the system; premium behavior is the consequence of controlled energy flow.**

Until the dimensional model, skeleton and applicable resonance gates are approved: **do not model the engine by eye.**
