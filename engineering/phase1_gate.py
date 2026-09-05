"""Phase 1 numeric-closure and handoff readiness helpers.

This module is intentionally conservative: UNKNOWN and DECISION_PENDING values
remain blockers unless a requirement is explicitly marked not applicable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


BLOCKING_STATUSES = {"UNKNOWN", "DECISION_PENDING", "SCREENING_ONLY", "REFERENCE"}
ACCEPTED_STATUSES = {"CALCULATED", "VERIFIED", "LOCKED", "DESIGN_TARGET"}


@dataclass(frozen=True)
class GateItem:
    name: str
    status: str
    rationale: str = ""

    @property
    def is_resolved(self) -> bool:
        return self.status in ACCEPTED_STATUSES


@dataclass(frozen=True)
class GateReport:
    gate: str
    passed: bool
    resolved: tuple[GateItem, ...]
    blockers: tuple[GateItem, ...]


def evaluate_gate(items: Sequence[GateItem], gate: str = "DIMENSIONAL_MODEL_VALIDATED") -> GateReport:
    """Evaluate a gate from explicit status-bearing items."""
    resolved = tuple(item for item in items if item.is_resolved)
    blockers = tuple(item for item in items if not item.is_resolved)
    return GateReport(gate=gate, passed=not blockers, resolved=resolved, blockers=blockers)


def status_map_to_items(values: Mapping[str, Mapping[str, object]]) -> list[GateItem]:
    """Convert a parameter/status mapping into gate items.

    Each entry must contain a string ``status``. Missing status is treated as
    UNKNOWN so absence cannot accidentally pass the gate.
    """
    items: list[GateItem] = []
    for name, payload in values.items():
        status = str(payload.get("status", "UNKNOWN"))
        rationale = str(payload.get("source_requirement", payload.get("relation", "")))
        items.append(GateItem(name=name, status=status, rationale=rationale))
    return items


def unresolved_names(items: Sequence[GateItem]) -> tuple[str, ...]:
    return tuple(item.name for item in items if not item.is_resolved)


def require_provenance(parameter: Mapping[str, object]) -> bool:
    """Return True only if an accepted numeric parameter carries provenance.

    DESIGN_TARGET values may use ``rationale`` in lieu of an external source;
    CALCULATED values may use ``relation``. VERIFIED/LOCKED values require a
    source or explicit relation.
    """
    status = str(parameter.get("status", "UNKNOWN"))
    if status not in ACCEPTED_STATUSES:
        return False
    if status == "DESIGN_TARGET":
        return bool(parameter.get("rationale"))
    if status == "CALCULATED":
        return bool(parameter.get("relation"))
    return bool(parameter.get("source") or parameter.get("relation"))
