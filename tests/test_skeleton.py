import math
import unittest

from engineering.skeleton import (
    assert_unit_vectors,
    bank_axis_unit_vectors,
    bridge_width_from_spacing_mm,
    center_spacing_from_bore_and_bridge_mm,
    engine_center_plane_normal,
    longitudinal_cylinder_centers_mm,
    paired_bank_cylinder_centers_mm,
    plane_normal_for_crank_normal_plane,
    point_along_axis_mm,
    side_by_side_rod_center_separation_mm,
)


class SkeletonRelationTests(unittest.TestCase):
    def test_90_degree_bank_axes_are_plus_minus_45_degrees(self):
        axes = bank_axis_unit_vectors(90.0)
        expected = math.sqrt(0.5)
        self.assertAlmostEqual(axes.left[0], -expected)
        self.assertAlmostEqual(axes.left[2], expected)
        self.assertAlmostEqual(axes.right[0], expected)
        self.assertAlmostEqual(axes.right[2], expected)
        assert_unit_vectors((axes.left, axes.right))

    def test_spacing_and_bridge_are_inverse_relations(self):
        spacing = center_spacing_from_bore_and_bridge_mm(101.6, 8.0)
        self.assertAlmostEqual(spacing, 109.6)
        self.assertAlmostEqual(bridge_width_from_spacing_mm(spacing, 101.6), 8.0)

    def test_longitudinal_centers_are_uniform(self):
        centers = longitudinal_cylinder_centers_mm(50.0, 110.0, count=4)
        self.assertEqual(centers, (50.0, 160.0, 270.0, 380.0))

    def test_bank_stagger_is_explicit(self):
        left, right = paired_bank_cylinder_centers_mm(50.0, 110.0, 20.0)
        self.assertEqual(left, (50.0, 160.0, 270.0, 380.0))
        self.assertEqual(right, (70.0, 180.0, 290.0, 400.0))

    def test_point_along_bank_axis(self):
        axis = bank_axis_unit_vectors(90.0).right
        point = point_along_axis_mm((0.0, 100.0, 0.0), axis, 200.0)
        self.assertAlmostEqual(point[0], math.sqrt(0.5) * 200.0)
        self.assertAlmostEqual(point[1], 100.0)
        self.assertAlmostEqual(point[2], math.sqrt(0.5) * 200.0)

    def test_side_by_side_rod_center_separation(self):
        self.assertAlmostEqual(side_by_side_rod_center_separation_mm(24.0, 22.0, 0.4), 23.4)

    def test_global_plane_normals(self):
        self.assertEqual(plane_normal_for_crank_normal_plane(), (0.0, 1.0, 0.0))
        self.assertEqual(engine_center_plane_normal(), (1.0, 0.0, 0.0))

    def test_spacing_smaller_than_bore_rejected(self):
        with self.assertRaises(ValueError):
            bridge_width_from_spacing_mm(100.0, 101.6)


if __name__ == "__main__":
    unittest.main()
