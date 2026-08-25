# Archimedes Resonance Research Import

**Source:** `Blackmvmba88/archimedes-quantum-resonance-engine`  
**Target:** `Blackmvmba88/GmGneralMotors`  
**Import date:** 2026-08-25

## Why this repository matters

The Archimedes laboratory is broader than automotive engineering. Its roadmap explicitly separates a classical Lorentz foundation, quantum-matter models, coherent control, cavity QED, condensed matter and error correction. It also contains auxiliary engineering modules for acoustics, aerodynamics, aero-acoustic coupling and adaptive design.

For the V8 project, the useful inheritance is the **classical engineering toolchain and philosophy that architecture follows physics**.

## Imported concepts

### Acoustic analysis

- spectral decomposition / FFT thinking;
- harmonic content / THD;
- SPL metrics;
- cavity eigenmodes;
- pressure-field visualization.

### Fluid / aero-acoustic analysis

- Reynolds number screening;
- vortex shedding via Strouhal frequency;
- Lighthill U^8 acoustic-power scaling concept;
- Curle dipole scaling concept;
- coupling between velocity field and radiated sound.

### Adaptive geometry

- geometry can be searched against a target resonance objective;
- resonance frequencies move when dimensions change;
- optimization should compare original and candidate geometries rather than rely on visual intuition.

## Corrections made during import

The source utility calls the rectangular-cavity eigenfrequency equation a `Helmholtz equation`. In this V8 repository we explicitly separate:

1. **rectangular cavity modes**
2. **necked Helmholtz resonator frequency**

because they are different physical models.

The source `St≈0.2` vortex-shedding default is preserved only as a coarse cylinder-like screening estimate, not as a universal constant for engine flows.

The source Lighthill/Curle functions use proportionality constants suitable for qualitative visualization. We therefore preserve those ideas in documentation but do not expose their current numerical power/SPL output as automotive certification evidence.

## Not imported as automotive evidence

The quantum portions of the source repository are not connected to V8 combustion, structural vibration or acoustic performance by any demonstrated mechanism in this project.

Therefore the following remain research-only:

- Two-Level System / Bloch equations;
- coherent quantum control;
- Jaynes-Cummings cavity QED;
- exciton-polariton models;
- quantum error-correction models.

They can remain part of the broader Archimedes research lineage without being used to make unsupported claims about the mechanical engine.

## Local implementation

Automotive-safe classical helpers now live in:

`engineering/resonance.py`

The current parameter contract lives in:

`parameters/nvh_targets.yaml`

The executable screening report is:

`python scripts/nvh_screen.py`

This import is intentionally small: bring the physics concepts we can defend, keep provenance, and revalidate everything in the automotive domain.
