# V8 ENGINE — Technical Contract

**Status:** Draft 0.1  
**Units:** millimeters / degrees  
**Primary target:** parametric mechanical V8 assembly

## 1. Mission

Build a modular, parameter-driven V8 digital master that can be verified before it is beautified.

The system must support independent component development, deterministic assembly, parameter revision, interference checks, future motion simulation, exploded views, cutaways, technical drawings and Blender visualization.

## 2. Fundamental rule

> No geometry is modeled until its function, references, coordinate system and interfaces are defined.

Do not start with cosmetic covers, textures, logos, hoses, wires, fasteners or render materials.

## 3. Authority order

When sources disagree, use this order:

1. locked master parameters
2. approved Interface Control Document
3. validated engineering drawings
4. component specifications
5. engineering assembly model
6. current blueprint reference
7. photographs/reference imagery
8. visual approximation

The current blueprint is `REFERENCE / CONCEPT GEOMETRY`, not manufacturing authority.

## 4. Baseline architecture

- 90° V8
- four cylinders per bank
- longitudinal crankshaft
- OHV/pushrod architecture baseline
- liquid cooling baseline
- wet-sump lubrication baseline
- central intake baseline
- front accessory drive

## 5. Global coordinates

```text
X = left / right
Y = front / rear
Z = down / up
```

Front: `Y-`  
Rear: `Y+`  
Left bank: `X-`  
Right bank: `X+`

Origin is the intersection of the crankshaft centerline, engine longitudinal center plane and primary front datum.

## 6. Primary datums

- `DATUM_A` — crankshaft centerline
- `DATUM_B` — engine longitudinal center plane
- `DATUM_C` — front reference plane
- `DATUM_D` — left deck plane
- `DATUM_E` — right deck plane
- `DATUM_F` — flywheel mounting plane

## 7. Parameter policy

Parameter states:

- `UNKNOWN`
- `ESTIMATED`
- `REFERENCE`
- `CALCULATED`
- `VERIFIED`
- `LOCKED`

A derived value must not be manually duplicated when it can be computed from upstream parameters.

Example: `crank_radius = stroke / 2`.

## 8. Component hierarchy

```text
V8_ENGINE
├── 00_REFERENCE
├── 01_ENGINE_BLOCK
├── 02_CRANKSHAFT
├── 03_CONNECTING_RODS
├── 04_PISTONS
├── 05_LEFT_CYLINDER_HEAD
├── 06_RIGHT_CYLINDER_HEAD
├── 07_CAMSHAFT
├── 08_VALVETRAIN
├── 09_TIMING_SYSTEM
├── 10_INTAKE
├── 11_EXHAUST
├── 12_LUBRICATION
├── 13_COOLING
├── 14_FRONT_ACCESSORIES
├── 15_FLYWHEEL
├── 16_FASTENERS
└── 99_COMPLETE_ASSEMBLY
```

## 9. Model maturity

- `L0` envelope
- `L1` functional skeleton
- `L2` mechanical geometry
- `L3` production detail
- `L4` visual detail

L4 cannot precede an approved L2 for the relevant system.

## 10. Top-down modeling

Required architecture:

`MASTER SKELETON → SUBASSEMBLIES → COMPONENTS`

The opposite pattern—modeling isolated components and forcing them together afterward—is prohibited for authoritative geometry.

## 11. Cylinder naming

Until a manufacturer-specific firing order is frozen:

- left bank: `L1 L2 L3 L4`
- right bank: `R1 R2 R3 R4`

A numeric 1–8 mapping is added only after crank phasing/firing order is approved.

## 12. Kinematic master

The complete four-stroke cycle uses one master variable:

`crank_angle`, domain `[0°, 720°)`.

Piston motion is derived from crank radius, connecting-rod length, cylinder-axis orientation and journal phase. No piston is hand-keyframed in the engineering model.

## 13. Interfaces

Each component must declare:

- input datums
- output datums
- mounting interfaces
- motion interface, if any
- clearance envelope
- parameter dependencies
- parent subsystem

## 14. Tolerance policy

Keep separate concepts separate:

- modeling tolerance
- assembly clearance
- manufacturing tolerance
- render tolerance

No manufacturing tolerance is inferred from a decorative blueprint note.

## 15. Naming

Components: `V8_<SYSTEM>_<COMPONENT>_<REV>`  
Sketches: `SK_<component>_<function>`  
Datums: `DT_<component>_<function>`  
Parameters: descriptive `snake_case` keys in the registry.

## 16. Versioning

Semantic versioning: `MAJOR.MINOR.PATCH`.

`0.x.x` means architecture/design definition is still evolving.  
`1.0.0` means the technical baseline has been approved.

## 17. Definition of Ready

A component can enter authoritative modeling only when function, datums, critical dimensions, interfaces, dependencies, parent system, target maturity and validation criteria are defined.

## 18. Definition of Done

A component is approved only when it matches the skeleton, preserves master parameters, satisfies interfaces, passes applicable interference/alignment tests, uses correct origin/units/naming and has a revision identity.

## 19. Golden rule

> If a part must be moved “until it looks right,” fix the upstream system instead.
