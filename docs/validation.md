# Validation Plan

## Principle

A component is not correct because it looks correct. It is correct only when the applicable checks pass.

## Validation classes

### V-PARAM — Parameter integrity

- valid units
- legal parameter states
- positive bore/stroke/envelope values
- cylinder count consistency
- calculated displacement traceable to source values
- no unresolved `UNKNOWN` value promoted to `LOCKED`

### V-DIM — Dimensional

- master dimensions match registry
- derived dimensions match equations
- no duplicated contradictory source of truth

### V-ALIGN — Alignment

- journals share intended axes
- cylinder axes intersect intended crank geometry
- deck planes respect bank architecture
- paired interfaces share intended datums

### V-SYM — Symmetry

Where architecture calls for symmetry, left/right entities must be mathematically derived rather than visually mirrored by eye.

### V-INT — Interference

Detect unintended solid overlap and distinguish it from intentional fits/contact surfaces.

### V-KIN — Kinematic

Complete 0°–720° crank cycle and verify deterministic dependent motion.

### V-ENV — Envelope

Complete assembly must remain inside the approved package envelope unless an explicit change request revises it.

## Gate policy

| Gate | Minimum evidence |
|---|---|
| BASELINE_READY | parameter registry + unknown list + ICD + coordinate spec |
| DIMENSIONAL_MODEL_VALIDATED | critical dimensions resolved and equations pass |
| SKELETON_LOCKED | all primary axes/planes parameterized and reviewed |
| ROTATING_ASSEMBLY_PASS | 720° motion test |
| SHORT_BLOCK_STRUCTURAL_PASS | block/rotating assembly alignment + interference pass |
| HEAD_SYSTEM_PASS | head/block/valvetrain interface pass |
| V8_ASSEMBLY_ALPHA | complete structural assembly checks |
| V8_ASSEMBLY_BETA | engineering detail checks |
| BLENDER_ENTRY_GATE | stable engineering model + export convention |

## CI role

GitHub Actions currently validates the textual parameter baseline. CAD-specific geometry validation will be added when authoritative CAD artifacts exist.
