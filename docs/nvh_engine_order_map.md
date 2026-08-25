# V8 Engine-Order / Resonance Baseline

**Status:** Screening baseline  
**Gate:** `NVH_BASELINE_READY`  
**Authority:** `SCREENING_ONLY` until operating RPM, crank phasing and firing order are frozen.

## Purpose

This document converts crank speed into a deterministic frequency map before CAD geometry is frozen. It is used to compare engine excitation lines against future structural, torsional and acoustic modes.

For engine order `N`:

`f = N × RPM / 60`

For an evenly firing four-stroke V8, aggregate combustion firing frequency is the **4th order**.

## Current screening envelope

The project has not yet frozen authoritative idle/redline values. Therefore all numbers below use the explicit screening envelope already registered in `parameters/nvh_targets.yaml`:

- minimum: 600 rpm
- maximum: 7000 rpm
- step: 100 rpm
- tracked core orders: 0.5X, 1X, 2X, 4X, 8X

## Reference order table

| RPM | 0.5X | 1X | 2X | 4X firing | 8X |
|---:|---:|---:|---:|---:|---:|
| 600 | 5.0 Hz | 10.0 Hz | 20.0 Hz | 40.0 Hz | 80.0 Hz |
| 1000 | 8.3 | 16.7 | 33.3 | 66.7 | 133.3 |
| 1500 | 12.5 | 25.0 | 50.0 | 100.0 | 200.0 |
| 2000 | 16.7 | 33.3 | 66.7 | 133.3 | 266.7 |
| 3000 | 25.0 | 50.0 | 100.0 | 200.0 | 400.0 |
| 4000 | 33.3 | 66.7 | 133.3 | 266.7 | 533.3 |
| 5000 | 41.7 | 83.3 | 166.7 | 333.3 | 666.7 |
| 6000 | 50.0 | 100.0 | 200.0 | 400.0 | 800.0 |
| 7000 | 58.3 | 116.7 | 233.3 | 466.7 | 933.3 |

The highest currently tracked screening line is therefore 8X at 7000 rpm = **933.3 Hz**.

With the provisional modal-band multiplier of 1.5, first-pass modal extraction should extend to approximately **1400 Hz**. This is a screening bandwidth, not a certification requirement.

## Excitation families

### Combustion

Primary aggregate line: `4X` for an evenly firing four-stroke V8.

Actual amplitude and sideband content depend on:

- firing order;
- cylinder-to-cylinder pressure variation;
- crank architecture;
- combustion phasing;
- load and transient state.

### Rotating assembly

Track at minimum:

- 1X rotational content;
- 2X components from imbalance / geometric effects where present;
- torsional orders produced by cylinder firing torque.

### Reciprocating assembly

Requires frozen reciprocating masses, rod ratio and crank phasing before authoritative force-order amplitudes can be calculated.

### Valvetrain

Valve-event and cam-related lines remain unresolved until cam timing and valvetrain architecture are frozen.

### Accessories

Pump, alternator, belt, gear, tooth-pass and blade-pass frequencies are added only after speed ratios and counts are defined.

## Source → path → receiver map

| Source | Transfer path | Main receivers / radiators |
|---|---|---|
| Combustion pressure | piston → rod → crank → main bearings → block → mounts | block surfaces, chassis, cabin |
| Valvetrain impacts | cam/lifter/pushrod/rocker → head/cover | head cover, airborne field |
| Intake pulses | runners → plenum → throttle → airbox | engine bay, cabin, exterior |
| Exhaust pulses | ports → headers → exhaust | underbody, cabin, exterior |
| Accessories | belt/gears/pumps → brackets/front cover/block | engine structure, chassis, airborne field |

## Coincidence rule

A future natural mode is flagged when an excitation line enters the current provisional separation margin around it.

Current preliminary margin: **10%**.

This margin exists only for early screening. Subsystem-specific margins must replace it after damping, boundary conditions, material properties and validation strategy are known.

## Required next inputs

To promote this document from screening to authoritative baseline, freeze:

1. operating idle / minimum rpm;
2. operating redline / maximum rpm;
3. crank phasing architecture;
4. firing order;
5. rotating and reciprocating masses;
6. valvetrain event frequencies;
7. accessory speed ratios.

Until those values exist, no missing excitation amplitude or frequency family is to be guessed.
