# Blender Read-Back — BM-VOCHO-WHEEL-001

This directory contains the read-back layer that binds a real Blender artifact to the wheel-system contract.

## Why this exists

The Blender viewport is not authoritative by itself. The system needs a reproducible machine-readable snapshot of what is actually inside the source `.blend`.

The inspector records:

- exact source file SHA-256,
- Blender scene unit configuration,
- object count,
- object names and hierarchy,
- transforms,
- object dimensions,
- mesh vertex/edge/polygon counts,
- material names,
- presence/absence of the required `BMV_*` contract objects.

It does **not** save or mutate the source scene.

## Run

```bash
blender --background /path/to/LLANTA.blend \
  --python vehicles/vocho/SYSTEM_01_WHEEL/blender/readback_wheel.py \
  -- --output /tmp/wheel_readback.json
```

## First pass on an existing scene

An existing `.blend` is not expected to already use the `BMV_*` names.

The first read-back therefore answers:

1. what objects actually exist,
2. which ones are candidate tire/rim/hub/studs,
3. what dimensions Blender reports,
4. whether unit scale is sane,
5. whether the object hierarchy is usable.

Only after that evidence should objects be renamed or reorganized.

## Mapping workflow

```text
LLANTA.blend
   ↓
readback_wheel.py
   ↓
wheel_readback.json
   ↓
human/AI mapping review
   ↓
object_mapping.json
   ↓
controlled rename/reparent transaction
   ↓
read-back again
   ↓
contract pass
```

## Certification boundary

A read-back is evidence, not certification.

Certification additionally requires:

- exact source artifact identity,
- dimensional source agreement,
- blueprint agreement,
- WARPBLACK visual/read-back evidence,
- certificate hash.
