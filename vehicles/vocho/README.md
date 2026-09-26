# VOCHO — Reference Vehicle Program

The Vocho program is the first vehicle-scale reference implementation of the BlackMamba simulation-first modeling workflow inside GmGneralMotors.

## Objective

Build the vehicle as a hierarchy of independently specifiable, modelable, measurable, and certifiable systems rather than as one monolithic Blender scene.

```text
vehicle
├── SYSTEM_01_WHEEL
├── SYSTEM_02_BRAKE
├── SYSTEM_03_SUSPENSION
├── SYSTEM_04_STEERING
├── SYSTEM_05_CHASSIS
├── SYSTEM_06_BODY
├── SYSTEM_07_INTERIOR
├── SYSTEM_08_POWERTRAIN
└── SYSTEM_09_ELECTRICAL
```

Each system must be able to progress through:

```text
REFERENCE
→ DIMENSIONAL SPEC
→ BLUEPRINT
→ BLENDER MODEL
→ READ-BACK
→ VISUAL EVIDENCE
→ CERTIFICATE
```

## Modeling rule

A Blender file is not considered complete merely because geometry exists.

A system is complete only when its authoritative parameters, object hierarchy, evidence, and validation state agree.

## System 01

Current active system: [SYSTEM_01_WHEEL](SYSTEM_01_WHEEL/README.md).

This first system establishes the reusable contract for all later assemblies.

## Source-of-truth rule

Dimensions are classified as:

- `confirmed`: measured or supported by a trusted source.
- `derived`: mathematically derived from confirmed inputs.
- `provisional`: useful modeling target but not yet physically verified.
- `tbd`: unknown; must not be silently guessed.

The parameter file is authoritative. Blender is a generated/inspected artifact, not the source of dimensional truth.
