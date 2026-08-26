# Phase 1 Validation Matrix

| Check | Evidence | Current state |
|---|---|---|
| Bore/stroke arithmetic | `engineering/dimensional.py` + tests | PASS |
| Crank radius relation | `stroke / 2` | PASS |
| Bank half-angle relation | `bank_angle / 2` | PASS |
| Blueprint displacement | calculated from visible geometry | PASS |
| Exact 350 CID alternative | solved at fixed bore | PASS |
| Exact 5.700 L alternative | solved at fixed bore | PASS |
| Piston OD relation | bore minus diametral clearance | RELATION PASS / INPUT UNKNOWN |
| Deck-stack relation | crank radius + rod + compression height + deck clearance | RELATION PASS / INPUTS UNKNOWN |
| Compression-ratio relation | swept + clearance volume | RELATION PASS / VOLUMES UNKNOWN |
| Cylinder spacing | provenance required | BLOCKED |
| Bank stagger | provenance required | BLOCKED |
| Crank stations | provenance/design target required | BLOCKED |
| Cam axis | provenance/design target required | BLOCKED |
| Flywheel/pulley planes | provenance/design target required | BLOCKED |
| `DIMENSIONAL_MODEL_VALIDATED` | all critical inputs resolved | NOT READY |

The distinction between a passed **relation** and an unresolved **input** is intentional. It allows the system architecture to advance without fabricating missing geometry.
