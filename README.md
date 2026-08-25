# GmGneralMotors — Parametric V8 Engineering Project

> **Status:** DESIGN DEFINITION  
> **3D modeling:** LOCKED  
> **Blender:** LOCKED  
> **Baseline:** v0.2.0

This repository is the engineering source of truth for a modular, parametric V8 engine digital master. The immediate goal is **not** to make a pretty mesh. The goal is to define enough geometry, interfaces, parameters, kinematics, resonance behavior, energy paths, and validation rules that the final engine becomes a consequence of the system.

## Engineering chain of authority

```text
MASTER PARAMETERS
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

If a component only fits after manual nudging, scaling, or arbitrary rotation, the error is upstream and must be fixed in the parameter, datum, constraint, or interface definition.

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

## Resonance / premium NVH policy

The project now imports the **classical engineering layer** of `Blackmvmba88/archimedes-quantum-resonance-engine` as a research foundation for:

- FFT / spectral analysis
- harmonic distortion
- cavity modes
- pressure-field thinking
- Reynolds / flow-regime checks
- Strouhal vortex-shedding frequency
- aero-acoustic coupling
- geometry-vs-resonance optimization

The quantum-matter modules from that laboratory remain a separate research domain. They are **not** used as evidence that a combustion engine has a quantum-performance mechanism. For this V8, premium resonance claims must be backed by measurable classical structural dynamics, acoustics, fluid dynamics and test data.

See:

- `docs/nvh_resonance_architecture.md`
- `docs/research/archimedes_resonance_import.md`
- `docs/ADR-0002-resonance-first-class.md`
- `parameters/nvh_targets.yaml`
- `engineering/resonance.py`

## Current blueprint reference

The current blueprint is treated as **concept/reference geometry**, not manufacturing authority.

Initial visible values:

| Parameter | Reference |
|---|---:|
| Bore | 101.6 mm |
| Stroke | 88.9 mm |
| Nominal displacement label | 5.7 L |
| Overall width | 680 mm |
| Overall length | 810 mm |
| Overall height | 620 mm |
| Bank reference length | 530 mm |
| Bank reference height | 255 mm |
| Piston diameter reference | 101.6 mm |
| Piston height reference | 64.8 mm |

**Important:** 101.6 mm bore × 88.9 mm stroke × 8 cylinders derives to approximately **5.766 L**, so the 5.7 L label is currently treated as nominal rather than exact. The piston diameter equaling the bore is also flagged for semantic/clearance verification before locking.

## Repository map

```text
.
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── V8_ENGINE_TECHNICAL_CONTRACT.md
├── docs/
│   ├── ICD.md
│   ├── coordinate_system.md
│   ├── dimensional_model.md
│   ├── kinematics.md
│   ├── nvh_resonance_architecture.md
│   ├── validation.md
│   ├── ADR-0002-resonance-first-class.md
│   └── research/
│       └── archimedes_resonance_import.md
├── engineering/
│   ├── __init__.py
│   └── resonance.py
├── parameters/
│   ├── master_parameters.yaml
│   ├── derived_parameters.yaml
│   └── nvh_targets.yaml
├── scripts/
│   ├── validate_parameters.py
│   └── nvh_screen.py
├── tests/
│   └── test_resonance.py
└── .github/workflows/
    └── validate.yml
```

CAD and Blender source directories will be introduced only after the design-definition gates are passed.

## Modeling maturity

- **L0 — Envelope:** bounding volumes only
- **L1 — Functional skeleton:** axes, datums, interfaces, pivots
- **L2 — Mechanical geometry:** functional solids and moving relationships
- **L2-NVH — Dynamic screening:** dominant engine orders, modal separation, flow resonance and energy-path review
- **L3 — Production detail:** bosses, ribs, holes, passages, fasteners, fillets
- **L4 — Visual detail:** materials, finishes, logos, cosmetic detail

No L4 work is permitted before the relevant system passes L2 and its applicable NVH gate.

## First modeling target

The first 3D object will be `V8_MASTER_SKELETON`, not the engine block.

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

The second target will be the rotating assembly: crankshaft → connecting rods → pistons → wrist pins.

## Current gate

Before Fusion 360 or Blender work begins, the project must have:

- [x] conceptual blueprint
- [x] engineering source-of-truth policy
- [x] component hierarchy
- [x] coordinate convention
- [x] roadmap
- [x] technical contract
- [x] initial parameter registry
- [x] dimensional-audit framework
- [x] interface-control framework
- [x] kinematic framework
- [x] resonance/NVH architecture
- [x] initial resonance screening core
- [x] automated parameter validation
- [ ] missing dimensions resolved
- [ ] operating RPM envelope frozen
- [ ] dominant engine-order map frozen
- [ ] master skeleton specification frozen
- [ ] kinematic crank phasing frozen
- [ ] modal-analysis plan approved
- [ ] design baseline promoted to 1.0.0

## Rule

> **Geometry is the consequence of the system; premium behavior is the consequence of controlled energy flow.**

Until the dimensional model, skeleton and resonance baseline are approved: **do not model the engine by eye.**
