# Premium Acoustic Signature Specification

**Status:** Design intent  
**Gate:** `NVH_BASELINE_READY` → `NVH_INTEGRATED_PASS`

## Principle

Premium means **controlled character**, not silence and not maximum loudness.

The engine must distinguish:

- intended signature;
- benign mechanical texture;
- unwanted drone;
- structural resonance;
- flow-generated tonal noise;
- transient ringing.

A tone may be intentionally reinforced only when fatigue, thermal, flow, emissions, serviceability and cabin-comfort requirements remain acceptable.

## Design-intent regions

The following regions are qualitative until the authoritative RPM envelope is frozen.

### Idle

Target character: `DEEP_STABLE_MECHANICAL`

Desired behavior:

- stable low-order presence;
- no intermittent boom;
- no unstable panel ringing;
- no accessory tone dominating engine character.

### Cruise

Target character: `LOW_FATIGUE_LOW_DRONE`

Desired behavior:

- sustained narrowband tones should not dominate the cabin;
- mount transmissibility should suppress objectionable structural paths;
- intake/exhaust character remains present but subordinate to comfort.

### Load / acceleration

Target character: `PROGRESSIVE_INTAKE_EXHAUST_PRESENCE`

Desired behavior:

- sound level and harmonic richness rise progressively with load;
- no sudden tonal peak caused by an accidental resonance;
- structural harshness must not masquerade as performance sound.

### High RPM

Target character: `CLEAN_HARMONIC_RISE_WITHOUT_HARSHNESS`

Desired behavior:

- higher-order content may become more audible;
- no uncontrolled cover, sump, bracket or mount radiation;
- no single narrowband resonance should dominate the spectrum.

## Anti-drone definition

`DRONE_CANDIDATE` is any sustained narrowband feature that:

1. persists across a meaningful steady-state RPM/load window;
2. couples efficiently into the cabin or a major radiating surface;
3. is not intentionally part of the approved signature;
4. shows high coherence with an engine order or acoustic mode.

The project will not invent a universal Hz or dB threshold before vehicle/package measurements exist.

## Measurement architecture

### Structural

Minimum accelerometer locations:

- block near main-bearing region;
- left cylinder head;
- right cylinder head;
- front cover;
- oil pan;
- engine side of each mount;
- chassis side of each mount.

Preferred sensor type: tri-axial acceleration where packaging allows.

### Acoustic

Minimum microphone locations:

- intake near-field reference;
- exhaust near-field reference;
- engine-bay reference;
- driver-ear / cabin reference once a vehicle package exists.

## Minimum metrics

- narrowband FFT spectrum;
- engine-order spectrum;
- order amplitude versus RPM;
- acceleration RMS;
- mount transmissibility;
- SPL;
- coherence when a transfer path is being diagnosed;
- ring-down decay for suspected resonators;
- transient spectrogram during tip-in and lift-off.

## Source / path / receiver evidence

Every unwanted feature must be documented with:

```text
SOURCE
  ↓
TRANSFER PATH
  ↓
RECEIVER / RADIATOR
```

Corrective action must target the correct layer.

Examples:

- source reduction: firing/combustion balance, accessory excitation;
- path modification: stiffness, damping, mount properties, bracket geometry;
- receiver modification: panel ribs, curvature, thickness distribution;
- acoustic tuning: runner length, plenum volume, side branch, Helmholtz resonator, muffler volume.

## Geometry rule

No rib, cavity, resonator or mass feature is approved because it "looks tuned".

It must be tied to at least one measurable or calculable target:

- shifted modal frequency;
- reduced response amplitude;
- improved modal separation;
- reduced transfer-path gain;
- desired acoustic-mode placement;
- reduced ring-down time;
- improved flow/acoustic compromise.

## Evidence required for `NVH_INTEGRATED_PASS`

1. engine-order map over the frozen operating envelope;
2. structural modal results with mode shapes;
3. harmonic-response screening at dominant orders;
4. crank torsional screening;
5. mount input/output transfer review;
6. intake/exhaust acoustic analysis;
7. resonance coincidence register;
8. final signature-vs-drone classification;
9. documented corrective actions for critical coincidences.

## Open decisions

Still intentionally unknown:

- cabin SPL targets;
- exterior SPL targets;
- exact desired signature bands;
- exact unwanted drone bands;
- mount-isolation numeric targets;
- final intake/exhaust harmonic emphasis.

These values should be frozen from a combination of simulation, benchmark measurements and prototype data—not guessed from branding language.
