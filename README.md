# GmGneralMotors — Parametric V8 Engineering Project

> **Status:** PHASE 1 — DIMENSIONAL RECONSTRUCTION  
> **3D modeling:** LOCKED  
> **Blender:** LOCKED  
> **Baseline:** v0.6.0

This repository is the engineering source of truth for a modular, parametric premium V8 digital master. The goal is not to draw an engine by eye; it is to define enough geometry, interfaces, parameters, kinematics, resonance behavior and energy paths that the engine becomes a reproducible consequence of the system.

## Engineering chain of authority

```text
MASTER PARAMETERS
      ↓
DIMENSIONAL / SPATIAL RELATIONS
      ↓
PHASE 1 NUMERIC CLOSURE
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

If a component only fits after manual nudging, scaling or arbitrary rotation, the error is upstream.

If a structure survives static stress but lands on a harmful resonance in the operating envelope, it is **not** premium-ready.

## Current development architecture

- V8 / 90° bank
- 8 cylinders / 4 per bank
- bore `101.6 mm` / stroke `88.9 mm` as development dimensional authority
- calculated displacement `5.765925746 L / 351.858377 CID`
- OHV / pushrod baseline
- longitudinal crankshaft
- **90° cross-plane crank — development direction, not production lock**
- cross-plane throw phase families `0° / 90° / 180° / 270°`
- liquid cooling
- wet-sump lubrication baseline
- central intake / front accessory drive
- NVH, resonance and energy-path mapping are first-class design systems

## Phase 1 — Dimensional reconstruction

The visual blueprint is being converted into a governed dimensional model.

### Development dimensional authority

Explicit blueprint geometry governs Phase 1:

```text
bore   = 101.6 mm
stroke = 88.9 mm
```

Derived:

```text
crank radius       = 44.45 mm
bank half-angle    = 45°
displacement       = 5.765925746 L
displacement       = 351.858377 CID
swept volume/cyl   = 720.740718 cc
```

The visible `5.7 L / 350 CID` values remain nominal labels. Production bore/stroke remain unlocked for later durability, thermal, emissions, packaging, combustion and NVH evidence.

Piston operating OD remains unresolved until a real piston-to-wall clearance is defined.

## Governing dimensional relations

```text
crank_radius = stroke / 2
bank_half_angle = bank_angle / 2
piston_operating_OD = bore - diametral_piston_clearance
deck_height = crank_radius + rod_length + compression_height + deck_clearance
compression_ratio = (swept_volume + clearance_volume) / clearance_volume
```

A relation may be accepted before every numeric input is known.

## Crank architecture / kinematics

The first premium V8 baseline proceeds with a **90° cross-plane crank** as a development direction. This prioritizes controlled NVH and deliberate low/mid-frequency character while accepting additional counterweight/inertia burden. Flat-plane remains a future high-RPM derivative path.

The slider-crank relation is executable:

```text
x(θ) = r cos(θ) + sqrt(l² - r² sin²(θ))
travel_from_TDC = (r + l) - x(θ)
```

Tests verify TDC, BDC=stroke, 360° mechanical periodicity and throw-phase behavior without inventing an engine rod length.

Cylinder-to-throw mapping and firing order remain unresolved.

## Master-skeleton relation layer

The project separates **geometric relations** from **missing numeric dimensions**.

For bank angle `β`, with `α = β/2`:

```text
left cylinder axis  = (-sin α, 0, cos α)
right cylinder axis = (+sin α, 0, cos α)
deck normal         = corresponding cylinder axis
```

Cylinder spacing is governed by:

```text
center_spacing = bore + inter_cylinder_bridge
```

Longitudinal cylinder centers are governed by:

```text
Y_i = Y_front + i × center_spacing       i = 0..3
Y_front_right = Y_front_left + bank_offset
```

A deck reference point is governed by:

```text
P_deck = P_axis_base + deck_height × bank_axis
```

The caller owns `P_axis_base`; therefore the system does **not** silently assume zero bore-axis offset.

For the current coordinate convention:

```text
crank axis direction         = (0, 1, 0)
flywheel/pulley plane normal = (0, 1, 0)
engine center-plane normal   = (1, 0, 0)
cam axis direction           = (0, 1, 0)
```

Cylinder longitudinal centers are **not** crankpin station planes. Bank stagger and bore-axis offset remain explicit inputs.

## Phase 1 numeric closure ledger

The remaining work is now treated as a finite closure problem instead of an open-ended modeling exercise.

`parameters/phase1_closure.yaml` classifies the remaining blockers into:

- skeleton placement;
- piston/deck stack;
- crank/rotating system;
- NVH authority.

`scripts/phase1_gate_report.py` reports the unresolved set. Raw `REFERENCE`, `UNKNOWN`, `DECISION_PENDING` and `SCREENING_ONLY` states do not pass an authoritative geometry gate.

Accepted closure states are `DESIGN_TARGET`, `CALCULATED`, `VERIFIED`, and `LOCKED`, each with provenance requirements.

See:

- `parameters/phase1_closure.yaml`
- `engineering/phase1_gate.py`
- `scripts/phase1_gate_report.py`
- `docs/phase1_numeric_closure.md`

## Resonance / premium NVH

The project reuses the defensible classical engineering layer of `Blackmvmba88/archimedes-quantum-resonance-engine` for spectral/acoustic/flow reasoning. Quantum-system models remain a separate research domain and are not automotive performance evidence.

Current capabilities include:

- FFT / harmonic reasoning
- engine-order maps
- cavity modes
- quarter-wave and Helmholtz relations
- Reynolds / Strouhal screening
- source → path → receiver mapping
- inverse target-frequency → geometry screening
- modal coincidence / exclusion screening
- premium acoustic intent and anti-drone architecture

Resonance-derived geometry is only a candidate until package, CFD/acoustic, structural/modal, thermal, fatigue, manufacturing and physical validation pass.

## Material / FEA provenance

Authoritative simulation may not use anonymous `aluminum`, `steel`, `iron` or similar generic material labels.

Every numeric material property must carry source, revision, temperature and status; damping additionally requires confidence metadata. No material constants have been invented yet.

## Current gates

Completed:

- [x] conceptual blueprint and source-of-truth policy
- [x] dimensional dependency model and executable audit
- [x] development bore/stroke authority
- [x] cross-plane crank development direction
- [x] executable slider-crank kinematics
- [x] executable master-skeleton relation layer
- [x] explicit Phase 1 numeric closure ledger / gate reporter
- [x] interface-control framework
- [x] resonance/NVH architecture and engine-order screening
- [x] inverse resonance geometry screening
- [x] premium acoustic design intent
- [x] material provenance contract
- [x] automated engineering tests

Still blocking authoritative CAD:

- [ ] inter-cylinder bridge / cylinder center spacing
- [ ] front cylinder longitudinal datum
- [ ] bank longitudinal stagger
- [ ] bore-axis offset mode/value
- [ ] deck / piston / rod stack
- [ ] piston operating clearance
- [ ] cam axis X/Z
- [ ] crank station positions and journal geometry
- [ ] cylinder-to-throw mapping and firing order
- [ ] flywheel / pulley planes
- [ ] operating RPM envelope
- [ ] sourced modal material properties / boundary inputs
- [ ] numeric Phase 1 → Phase 2 handoff accepted
- [ ] master skeleton frozen
- [ ] design baseline promoted to 1.0.0

## Rule

> **Geometry is the consequence of the system; premium behavior is the consequence of controlled energy flow.**

Until the dimensional model, numeric skeleton handoff and applicable resonance gates are approved: **do not model the engine by eye.**
