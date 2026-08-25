# Interface Control Document (ICD)

**Status:** Draft 0.1

This document controls subsystem boundaries. Dimensions are added as they become verified.

## Interface matrix

| Interface | Primary control | Current status |
|---|---|---|
| Block ↔ crankshaft | DATUM_A, main-bearing stations | OPEN |
| Crankshaft ↔ connecting rod | rod journal axis/width | OPEN |
| Connecting rod ↔ piston | wrist-pin axis | OPEN |
| Piston ↔ cylinder | cylinder axis, bore, running clearance | OPEN |
| Block ↔ cylinder head | deck plane, bore pattern, fastener pattern | OPEN |
| Camshaft ↔ block | cam axis, bearing stations | OPEN |
| Camshaft ↔ lifter | lobe/lifter contact geometry | OPEN |
| Lifter ↔ pushrod | cup/ball axis | OPEN |
| Pushrod ↔ rocker | ball/cup interface | OPEN |
| Rocker ↔ valve | pivot axis and tip contact | OPEN |
| Block ↔ oil pan | lower rail plane and bolt pattern | OPEN |
| Block ↔ timing cover | front plane and shaft exits | OPEN |
| Crankshaft ↔ flywheel | DATUM_F, pilot/bolt interface | OPEN |
| Crankshaft ↔ front pulley | front shaft interface | OPEN |
| Heads ↔ intake | intake mating planes/ports | OPEN |
| Heads ↔ exhaust | exhaust mating planes/ports | OPEN |

## Component interface template

Every authoritative component specification must include:

```text
COMPONENT
PARENT SYSTEM
INPUT DATUMS
OUTPUT DATUMS
MOUNTING INTERFACE
MOTION INTERFACE
CLEARANCE ENVELOPE
PARAMETER DEPENDENCIES
VALIDATION TEST
```

## Freeze rule

An interface may only become `LOCKED` when both sides are represented by compatible parameterized geometry and an applicable assembly test passes.
