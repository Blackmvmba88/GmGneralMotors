# V8 NVH / Resonance Architecture

**Status:** Draft 0.2  
**Gate:** `NVH_BASELINE_READY`  
**Purpose:** Make resonance, acoustics and energy flow first-class design inputs before authoritative CAD geometry is frozen.

## 1. Premium definition

For this project, `premium` does not mean merely quiet and does not mean merely loud.

It means the engine has a deliberately controlled dynamic signature:

- harmful structural resonances are separated, damped or redirected;
- useful pressure-wave behavior may be intentionally tuned;
- unwanted drone and harshness are controlled;
- desired mechanical/exhaust character is preserved intentionally;
- energy paths are measurable and traceable;
- design decisions can be linked to simulation or test evidence.

## 2. Source → path → receiver model

Every NVH problem is described as:

```text
SOURCE
  ↓
TRANSFER PATH
  ↓
RECEIVER / RADIATOR
```

Examples:

```text
combustion pressure
  → piston / rod / crank
  → main bearings / block
  → mounts / chassis / cabin
```

```text
valve event
  → valvetrain / head
  → cover
  → airborne radiation
```

```text
intake pressure pulse
  → runner / plenum
  → throttle / airbox
  → cabin / exterior sound
```

## 3. Excitation map

For any engine order `N`:

`f = N × RPM / 60`

For an evenly firing four-stroke V8, aggregate combustion firing frequency is the fourth order:

`f_fire = 4 × RPM / 60`

Examples:

| RPM | 1X | 2X | 4X firing | 8X |
|---:|---:|---:|---:|---:|
| 1000 | 16.7 Hz | 33.3 Hz | 66.7 Hz | 133.3 Hz |
| 3000 | 50.0 Hz | 100.0 Hz | 200.0 Hz | 400.0 Hz |
| 6000 | 100.0 Hz | 200.0 Hz | 400.0 Hz | 800.0 Hz |

This table is only a starting order map. Actual amplitudes depend on crank phasing, combustion pressure, balance, firing order, reciprocating masses, stiffness, damping and accessories.

## 4. Structural resonance

A component is not accepted from static strength alone.

Required later evidence:

- modal frequencies;
- mode shapes;
- damping estimates/measurements;
- harmonic response;
- attachment stiffness;
- local antinode locations;
- stress response under dynamic loading.

Ribs, thickness changes and mass redistribution should be placed according to mode shape and load path, not visual symmetry alone.

## 5. Acoustic / pressure-wave families

The project tracks multiple resonance families separately.

### 5.1 Quarter-wave

`f ≈ c / (4L)`

Useful as a first estimate for runners, ducts, side branches and drone countermeasures.

### 5.2 Necked Helmholtz resonator

`f_H = c/(2π) × sqrt(A/(V L_eff))`

Useful for targeted attenuation or tuning when a cavity and neck are intentionally designed.

### 5.3 Rectangular cavity modes

`f = c/2 × sqrt((nx/Lx)^2 + (ny/Ly)^2 + (nz/Lz)^2)`

Useful as an idealized screening model for enclosed acoustic volumes. Real engine plenums and cavities require more realistic geometry/CFD/FEA or test.

## 6. Flow-generated tones

For vortex shedding:

`St = fD/U`

or

`f = St × U / D`

`St ≈ 0.2` can be used only as a coarse screening default for cylinder-like shedding conditions. It is not universal.

Flow-generated noise must be reviewed around:

- throttle edges;
- valve/port transitions;
- intake restrictions;
- accessory cooling flows;
- exposed bluff bodies;
- exhaust junctions.

## 7. Imported Archimedes research lineage

The source laboratory already contains engineering tools for:

- FFT spectra;
- THD and SPL;
- cavity modes and pressure-field visualization;
- Reynolds number;
- Strouhal frequency;
- Lighthill/Curle aero-acoustic scaling concepts;
- adaptive geometry-versus-resonance exploration.

Those classical tools are relevant to the V8 design philosophy and have been adapted into the local Python engineering layer.

The source laboratory also contains genuine quantum-system models (TLS/Bloch, Jaynes-Cummings, etc.). Those remain scientifically separate from combustion-engine NVH. We do not call a mechanical resonance `quantum` merely because the research lineage contains quantum physics.

## 8. Premium NVH gates

### `NVH_BASELINE_READY`

Requires:

- operating RPM envelope;
- tracked order set;
- source/path/receiver map;
- initial acoustic-resonance map;
- initial modal-analysis plan;
- provisional separation criteria.

### `NVH_INTEGRATED_PASS`

Requires evidence from:

- structural modal analysis;
- harmonic response;
- torsional analysis;
- mount transfer paths;
- intake/exhaust acoustic analysis;
- coincidence register between excitation lines and structural/acoustic modes.

## 9. Geometry optimization rule

We will not optimize geometry for one frequency in isolation.

A viable geometry must simultaneously respect:

- static strength;
- fatigue;
- thermal loads;
- manufacturability/casting;
- mass;
- fluid paths;
- modal behavior;
- acoustic radiation;
- serviceability.

A rib that fixes one mode but creates another, blocks coolant, adds a hot spot or prevents casting is not a successful design.

## 10. Current blockers

Before resonance can influence final geometry, we still need:

- authoritative RPM idle/redline envelope;
- crank phasing/firing order;
- rotating/reciprocating masses;
- candidate materials and elastic properties;
- wall thicknesses;
- mount locations and stiffness targets;
- intake/exhaust dimensions;
- first modal FEA results.

Until these exist, resonance calculations remain **screening**, not certification.
