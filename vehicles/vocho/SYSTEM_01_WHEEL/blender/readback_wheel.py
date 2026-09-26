"""Blender read-back inspector for BM-VOCHO-WHEEL-001.

Run with:
  blender --background LLANTA.blend --python readback_wheel.py -- --output wheel_readback.json

This script is read-only with respect to the .blend scene. It does not save the file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import bpy


SYSTEM_ID = "BM-VOCHO-WHEEL-001"

EXPECTED_OBJECTS = [
    "BMV_WHEEL_ROOT",
    "BMV_TIRE",
    "BMV_RIM",
    "BMV_HUB",
    "BMV_STUD_01",
    "BMV_STUD_02",
    "BMV_STUD_03",
    "BMV_STUD_04",
    "BMV_VALVE",
    "BMV_AXIS_ROTATION",
    "BMV_PLANE_MOUNT",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def vec3(v):
    return [float(v[0]), float(v[1]), float(v[2])]


def object_record(obj):
    data = {
        "name": obj.name,
        "type": obj.type,
        "parent": obj.parent.name if obj.parent else None,
        "location": vec3(obj.location),
        "rotation_euler": vec3(obj.rotation_euler),
        "scale": vec3(obj.scale),
        "dimensions": vec3(obj.dimensions),
        "visible_viewport": not obj.hide_viewport,
        "visible_render": not obj.hide_render,
    }

    if obj.type == "MESH" and obj.data:
        mesh = obj.data
        data["mesh"] = {
            "vertices": len(mesh.vertices),
            "edges": len(mesh.edges),
            "polygons": len(mesh.polygons),
            "materials": [m.name if m else None for m in mesh.materials],
        }

    return data


def parse_args():
    argv = sys.argv
    extra = argv[argv.index("--") + 1 :] if "--" in argv else []
    p = argparse.ArgumentParser()
    p.add_argument("--output", default="wheel_readback.json")
    return p.parse_args(extra)


def main():
    args = parse_args()

    blend_path = Path(bpy.data.filepath).resolve()
    if not blend_path.exists():
        raise SystemExit("Active Blender file is not a saved .blend file")

    objects = sorted((object_record(o) for o in bpy.data.objects), key=lambda x: x["name"])
    names = {o["name"] for o in objects}

    expected = {
        name: {"present": name in names}
        for name in EXPECTED_OBJECTS
    }

    payload = {
        "schema": "blackmamba.blender-readback.v1",
        "system_id": SYSTEM_ID,
        "blend": {
            "path": str(blend_path),
            "name": blend_path.name,
            "sha256": sha256_file(blend_path),
        },
        "scene": {
            "name": bpy.context.scene.name,
            "unit_system": bpy.context.scene.unit_settings.system,
            "scale_length": bpy.context.scene.unit_settings.scale_length,
            "object_count": len(objects),
        },
        "expected_object_contract": expected,
        "object_contract_complete": all(v["present"] for v in expected.values()),
        "objects": objects,
    }

    output = Path(args.output).resolve()
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "system_id": SYSTEM_ID,
        "blend_sha256": payload["blend"]["sha256"],
        "object_count": len(objects),
        "object_contract_complete": payload["object_contract_complete"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
