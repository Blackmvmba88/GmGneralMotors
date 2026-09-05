# Resonance Geometry Synthesis — Screening Contract

**Status:** PRE-CAD SCREENING  
**Gate:** `NVH_BASELINE_READY`

## Purpose

Translate a target frequency into first-pass geometric relationships before authoritative CAD exists.

The output is not a final part. It is a controlled design candidate that must later survive packaging, flow, structural, thermal, fatigue, manufacturing and test evidence.

## Supported inverse relations

### Engine-order crossing

`RPM = 60 f / order`

This identifies where a structural/acoustic target intersects a selected engine order.

### Quarter-wave candidate

`L = c / (4 f)`

Useful as a first screening relation for ducts, runners and side branches.

### Helmholtz cavity volume

`V = A / (L_eff × (2πf/c)^2)`

Useful when neck area and effective neck length are selected as packaging candidates.

### Helmholtz neck area

`A = V × L_eff × (2πf/c)^2`

Useful when cavity volume is constrained by package space.

### Modal exclusion band

For screening margin `m`:

`[f_n(1-m), f_n(1+m)]`

This band is used only to flag order/mode coincidences for deeper analysis.

## Design rule

A frequency target never directly authorizes geometry.

The decision chain is:

```text
target frequency
      ↓
analytical geometry candidate
      ↓
package feasibility
      ↓
CFD / acoustic model
      ↓
structural / modal interaction
      ↓
thermal + fatigue + manufacturing
      ↓
prototype / measurement
      ↓
approved feature
```

## Example workflow

```bash
python scripts/resonance_geometry_design.py 400 --order 4
```

This computes:

- the RPM where 4X crosses 400 Hz;
- quarter-wave effective length for 400 Hz;
- a Helmholtz cavity volume using the explicitly supplied candidate neck geometry;
- the current modal screening exclusion band.

The default neck geometry is intentionally visible in the CLI output so it cannot be mistaken for a hidden authoritative dimension.

## Premium intent

The project is allowed to intentionally reinforce desirable pressure-wave behavior only when the same feature does not create unacceptable:

- structural stress amplification;
- fatigue concentration;
- cabin drone;
- thermal penalty;
- flow restriction;
- serviceability problems;
- manufacturing risk.

Premium behavior means **controlled energy flow**, not simply more resonance or less noise.
