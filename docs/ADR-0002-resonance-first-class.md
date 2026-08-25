# ADR-0002 — Resonance and Energy Flow Are First-Class Design Inputs

**Status:** Accepted  
**Date:** 2026-08-25

## Context

The V8 project originally treated geometry, kinematics and interfaces as the primary pre-CAD authority. Structural resonance, airborne acoustics, intake/exhaust pressure waves and flow-generated tones can invalidate an otherwise strong and geometrically correct design.

A premium engine also needs an intentional acoustic and vibration signature rather than an accidental one discovered after prototype fabrication.

## Decision

The project will treat NVH/resonance as a first-class cross-cutting subsystem before structural geometry is frozen.

The engineering chain becomes:

```text
parameters → skeleton → geometry → structural/flow/NVH models → validated assembly
```

A component can fail its engineering gate even if static geometry and strength are acceptable when dynamic response creates an unacceptable resonance, transfer path or acoustic radiator.

## Imported research

We will reuse the classical acoustic/aero-acoustic foundations from `Blackmvmba88/archimedes-quantum-resonance-engine` where they are physically applicable.

Quantum-system models in that repository remain research-isolated unless a future automotive application is supported by a specific, testable physical mechanism and evidence.

## Consequences

### Positive

- resonance is considered before expensive geometry freeze;
- ribs and wall thickness can be placed by dynamic evidence;
- intake and exhaust can be tuned as wave systems;
- sound character can become a design target;
- digital-twin data can include modal/NVH state;
- premium claims can be backed by measurements.

### Cost

- additional FEA/CFD/test work;
- more parameters and evidence gates;
- structural and acoustic optimization may conflict with mass, thermal and manufacturing goals.

## Rejected alternative

Treat NVH as a late-stage exhaust/mount tuning exercise after the complete engine is modeled.

Reason for rejection: late discovery of resonance can force expensive redesign of core structural geometry.
