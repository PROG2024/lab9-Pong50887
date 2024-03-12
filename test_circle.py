"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest

from circle import Circle

# TODO write 3 tests as described above

class Circletest(unittest.TestCase):

    def setUp(self):
        """Create a circle for other testcase."""
        self.circle = Circle(4)
        self.circle1 = Circle(3)
        self.circle2 = Circle(12)

    def test_add_area_typical_values(self):
        """add_area for typical values (4,3), (5,12)"""
        x = self.circle.add_area(self.circle1)
        self.assertEqual(x.get_radius(), Circle(5).get_radius())
        self.assertEqual(x.get_area(), Circle(5).get_area())
        y = self.circle2.add_area(x)
        self.assertEqual(y.get_radius(), Circle(13).get_radius())

    def test_add_area_edge_case_0(self):
        circle_0 = Circle(0)
        x = self.circle.add_area(circle_0)
        self.assertEqual(x.get_radius(), self.circle.get_radius())
        self.assertEqual(x.get_area(), self.circle.get_area())

    def test_circle_raised_error(self):
        with self.assertRaises(ValueError):
            circle_neg = Circle(-1)
        circle_0 = Circle(1)
