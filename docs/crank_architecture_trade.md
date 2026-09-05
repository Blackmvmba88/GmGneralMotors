# V8 Crank Architecture Trade Study

**Status:** DEVELOPMENT DIRECTION  
**Gate:** `NVH_BASELINE_READY` → `ROTATING_ASSEMBLY_PASS`

## Decision

The current premium V8 program will proceed with a **90° cross-plane crank as the development direction**.

This is not a production lock. It is a controlled choice that lets kinematic, torsional and NVH work advance while preserving a future flat-plane performance variant.

## Why cross-plane fits the current program

The project has already defined premium as controlled energy flow, low fatigue, low drone and deliberate acoustic character rather than maximum loudness or maximum RPM.

For that objective, cross-plane is the stronger first development path because it generally trades additional crank mass/counterweight complexity for a friendlier vibration character in a 90° V8.

## Trade matrix

| Criterion | Cross-plane | Flat-plane |
|---|---|---|
| Premium low/mid-frequency NVH direction | Strong | Higher burden |
| Second-order vibration burden | Lower | Higher |
| Crank inertia potential | Higher | Lower |
| Counterweight demand | Higher | Lower |
| High-RPM response potential | Moderate/strong | Strong |
| Exhaust pulse grouping | More complex by bank | More regular |
| Structural isolation burden | Lower directionally | Higher |
| Current project fit | **Preferred** | Future variant |

The table is a development-level engineering comparison, not a certification result. Actual behavior depends on crank mass distribution, rod/piston masses, firing sequence, block stiffness, mounts, exhaust geometry and operating range.

## Cross-plane geometry baseline

The development crank uses four throw phase families:

```text
T0   =   0°
T90  =  90°
T180 = 180°
T270 = 270°
```

This does **not** yet assign cylinders to throws.

## Combustion-event spacing

An evenly firing four-stroke V8 has eight combustion events over 720 crank degrees:

`720° / 8 = 90°`

Therefore the target event cadence is one combustion event every 90° of crank rotation.

That does not determine the firing order by itself.

## Cylinder identity policy

Continue using bank-local IDs:

- left bank: `L1 L2 L3 L4`
- right bank: `R1 R2 R3 R4`

Do not introduce numeric 1–8 numbering until the project owns a coherent numbering convention rather than inheriting a manufacturer convention accidentally.

## Still unresolved

Before crank phasing can be frozen:

- cylinder-to-throw mapping;
- numeric cylinder numbering, if numeric IDs are retained at all;
- firing order;
- rod journal pairing strategy;
- bank longitudinal stagger;
- crank station spacing;
- counterweight strategy;
- rotating and reciprocating masses;
- torsional damper strategy;
- authoritative RPM envelope.

## NVH implications

The cross-plane choice changes the next analysis priorities:

1. torsional order map;
2. crank counterweight / bearing load study;
3. bank-specific exhaust pulse sequence;
4. mount transfer paths;
5. block modal interaction near firing and harmonic orders.

## Variant policy

Flat-plane is explicitly retained as a future architecture candidate for a higher-RPM, lower-inertia derivative.

The premium family therefore does not need one crank philosophy forever; it needs a controlled architecture decision per engine variant.
