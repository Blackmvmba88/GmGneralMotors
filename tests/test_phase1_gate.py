import unittest

from engineering.phase1_gate import GateItem, evaluate_gate, require_provenance, unresolved_names


class Phase1GateTests(unittest.TestCase):
    def test_unknown_blocks_gate(self):
        report = evaluate_gate([
            GateItem("bore", "VERIFIED"),
            GateItem("deck_height", "UNKNOWN"),
        ])
        self.assertFalse(report.passed)
        self.assertEqual(unresolved_names(report.blockers), ("deck_height",))

    def test_all_resolved_passes(self):
        report = evaluate_gate([
            GateItem("bore", "VERIFIED"),
            GateItem("spacing", "CALCULATED"),
            GateItem("bridge", "DESIGN_TARGET"),
        ])
        self.assertTrue(report.passed)
        self.assertEqual(len(report.blockers), 0)

    def test_reference_does_not_pass_authoritative_gate(self):
        report = evaluate_gate([GateItem("envelope", "REFERENCE")])
        self.assertFalse(report.passed)

    def test_design_target_requires_rationale_for_provenance(self):
        self.assertFalse(require_provenance({"status": "DESIGN_TARGET", "value": 1.0}))
        self.assertTrue(require_provenance({
            "status": "DESIGN_TARGET",
            "value": 1.0,
            "rationale": "packaging target",
        }))

    def test_calculated_requires_relation(self):
        self.assertFalse(require_provenance({"status": "CALCULATED", "value": 2.0}))
        self.assertTrue(require_provenance({
            "status": "CALCULATED",
            "value": 2.0,
            "relation": "a + b",
        }))


if __name__ == "__main__":
    unittest.main()
