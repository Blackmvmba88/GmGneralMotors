# Structural Modal / Harmonic Analysis Plan

**Status:** Pre-CAD planning  
**Purpose:** Define how resonance will influence geometry before component detail is frozen.

## 1. Analysis sequence

### A. Component free-free modal studies

Use for:

- block casting concept;
- heads;
- front cover;
- oil pan;
- intake plenum;
- exhaust manifolds / headers;
- accessory brackets.

Goal: identify intrinsic mode families and radiator-like surfaces before mount constraints hide them.

### B. Constrained subassembly studies

Apply realistic interfaces for:

- block + main caps / bedplate;
- block + heads;
- front-drive assembly;
- intake assembly;
- exhaust assembly.

Goal: understand mode migration when joints and attachments are introduced.

### C. Complete powertrain modal study

Include:

- engine mounts;
- transmission / rear support when available;
- accessory masses;
- intake/exhaust attachment stiffness;
- fluid-added-mass effects when they become material to the result.

### D. Harmonic response

Excite the model using engine-order lines and subsystem-specific forces once amplitudes are available.

## 2. Frequency bandwidth

The current screening envelope tracks up to 8X at 7000 rpm:

`8 × 7000 / 60 = 933.3 Hz`

With the provisional 1.5 analysis-band multiplier:

`933.3 × 1.5 ≈ 1400 Hz`

Therefore the first modal studies should extract modes through approximately **1.4 kHz** while the screening envelope remains active.

When authoritative RPM and order sets are frozen, this limit must be recalculated automatically.

## 3. Required model properties

No modal result is considered engineering evidence until the model identifies:

- material elastic modulus;
- Poisson ratio;
- density;
- joint / contact assumptions;
- bolt or preload simplifications;
- mount stiffness assumptions;
- boundary conditions;
- mesh size and element type;
- convergence evidence for critical modes.

Unknown properties must remain explicitly UNKNOWN rather than replaced by decorative defaults.

## 4. Mode-shape review

For each critical mode record:

- natural frequency;
- dominant moving component / surface;
- nodal regions;
- antinodal regions;
- likely acoustic radiator area;
- strain-energy concentration;
- nearby engine-order crossings;
- proposed corrective action.

## 5. Geometry intervention hierarchy

When a harmful coincidence is detected, investigate in this order:

1. source amplitude reduction where practical;
2. load-path or joint-stiffness change;
3. local stiffness redistribution;
4. curvature / rib placement at high-response regions;
5. thickness redistribution;
6. damping treatment where compatible;
7. mass addition only when justified.

The default response is **not** to make the whole part thicker.

## 6. Premium acceptance logic

A structure is not premium-ready merely because it survives stress analysis.

It must also demonstrate that critical operating excitations do not create unacceptable:

- resonance amplification;
- fatigue hot spots;
- mount transfer;
- panel radiation;
- cabin drone;
- tonal harshness.

## 7. Deliverable schema

Each future simulation report should contain:

```text
MODEL_REVISION
PARAMETER_BASELINE
BOUNDARY_CONDITIONS
MATERIAL_SET
MESH_EVIDENCE
MODE_TABLE
MODE_SHAPE_IMAGES
ORDER_CROSSING_TABLE
HARMONIC_RESPONSE
CORRECTIVE_ACTIONS
PASS_FAIL_GATE
```

## 8. Current blocker

Actual FEA remains blocked until authoritative CAD geometry, candidate materials, wall thicknesses, joints and mount interfaces exist.

This document defines the analysis contract now so geometry can be created with the dynamic requirements already known.
