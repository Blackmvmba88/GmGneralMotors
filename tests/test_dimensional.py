import math
import unittest

from engineering.dimensional import (
    bank_half_angle_deg,
    compression_ratio,
    crank_radius_mm,
    deck_height_mm,
    displacement_cid,
    displacement_l,
    displacement_per_cylinder_cc,
    piston_operating_od_mm,
    stroke_for_target_cid,
    stroke_for_target_l,
)


class DimensionalRelationsTests(unittest.TestCase):
    def test_blueprint_displacement(self):
        self.assertAlmostEqual(displacement_l(101.6, 88.9, 8), 5.765925746146245, places=12)
        self.assertAlmostEqual(displacement_cid(101.6, 88.9, 8), 351.8583772020569, places=9)

    def test_per_cylinder_volume(self):
        self.assertAlmostEqual(displacement_per_cylinder_cc(101.6, 88.9), 720.7407182682807, places=9)

    def test_crank_radius_and_bank_half_angle(self):
        self.assertAlmostEqual(crank_radius_mm(88.9), 44.45)
        self.assertAlmostEqual(bank_half_angle_deg(90.0), 45.0)

    def test_exact_350_cid_stroke_at_fixed_bore(self):
        stroke = stroke_for_target_cid(350.0, 101.6, 8)
        self.assertAlmostEqual(stroke, 88.43046525543434, places=9)
        self.assertAlmostEqual(displacement_cid(101.6, stroke, 8), 350.0, places=9)

    def test_exact_5_7_l_stroke_at_fixed_bore(self):
        stroke = stroke_for_target_l(5.7, 101.6, 8)
        self.assertAlmostEqual(stroke, 87.88354590564778, places=9)
        self.assertAlmostEqual(displacement_l(101.6, stroke, 8), 5.7, places=12)

    def test_piston_clearance_relation(self):
        self.assertAlmostEqual(piston_operating_od_mm(101.6, 0.10), 101.5)

    def test_deck_stack_relation(self):
        # Synthetic values test the relation only; they are not V8 design inputs.
        result = deck_height_mm(88.9, 150.0, 30.0, 0.2)
        self.assertAlmostEqual(result, 224.65)

    def test_compression_ratio_relation(self):
        self.assertAlmostEqual(compression_ratio(900.0, 100.0), 10.0)

    def test_invalid_geometry_rejected(self):
        with self.assertRaises(ValueError):
            displacement_l(0.0, 88.9, 8)
        with self.assertRaises(ValueError):
            piston_operating_od_mm(101.6, 200.0)


if __name__ == "__main__":
    unittest.main()
