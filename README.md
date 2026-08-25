# GmGneralMotors — Parametric V8 Engineering Project

> **Status:** DESIGN DEFINITION  
> **3D modeling:** LOCKED  
> **Blender:** LOCKED  
> **Baseline:** v0.1.0

This repository is the engineering source of truth for a modular, parametric V8 engine digital master. The immediate goal is **not** to make a pretty mesh. The goal is to define enough geometry, interfaces, parameters, kinematics, and validation rules that the final engine becomes a consequence of the system.

## Engineering chain of authority

```text
MASTER PARAMETERS
      ↓
MASTER SKELETON
      ↓
COMPONENT GEOMETRY
      ↓
ASSEMBLY
      ↓
VALIDATION
      ↓
VISUAL / BLENDER MODEL
```

If a component only fits after manual nudging, scaling, or arbitrary rotation, the error is upstream and must be fixed in the parameter, datum, constraint, or interface definition.

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
│   └── validation.md
├── parameters/
│   ├── master_parameters.yaml
│   └── derived_parameters.yaml
├── scripts/
│   └── validate_parameters.py
└── .github/workflows/
    └── validate.yml
```

CAD and Blender source directories will be introduced only after the design-definition gate is passed.

## Modeling maturity

- **L0 — Envelope:** bounding volumes only
- **L1 — Functional skeleton:** axes, datums, interfaces, pivots
- **L2 — Mechanical geometry:** functional solids and moving relationships
- **L3 — Production detail:** bosses, ribs, holes, passages, fasteners, fillets
- **L4 — Visual detail:** materials, finishes, logos, cosmetic detail

No L4 work is permitted before the relevant system passes L2 validation.

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
- [x] automated parameter validation
- [ ] missing dimensions resolved
- [ ] master skeleton specification frozen
- [ ] kinematic crank phasing frozen
- [ ] design baseline promoted to 1.0.0

## Rule

> **Geometry is the consequence of the system.**

Until the dimensional model and skeleton are approved: **do not model the engine by eye.**
