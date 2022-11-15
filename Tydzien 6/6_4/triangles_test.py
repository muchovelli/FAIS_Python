# Kod testujący moduł.

import unittest
import triangles as tri

class TestPolynomials(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(tri.Triangle(1, 2, 3, 4, 5, 6)), "[(1, 2), (3, 4), (5, 6)]")
        self.assertEqual(repr(tri.Triangle(1, 2, 3, 4, 5, 6)), "Triangle(1, 2, 3, 4, 5, 6)")

    def test_eq(self):
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6) == tri.Triangle(1, 2, 3, 4, 5, 6), True)
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6) == tri.Triangle(1, 2, 5, 6, 3, 4), True)
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6) == tri.Triangle(1, 2, 3, 4, 5, 7), False)

    def test_ne(self):
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6) != tri.Triangle(1, 2, 3, 4, 5, 6), False)
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6) != tri.Triangle(1, 2, 5, 6, 3, 4), False)
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6) != tri.Triangle(1, 2, 3, 4, 5, 7), True)

    def test_center(self):
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6).center(), tri.Point(3, 4))
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6).center(), tri.Point(3, 4))
        self.assertEqual(tri.Triangle(1, 2, 3, 4, 5, 6).center(), tri.Point(3, 4))

    def test_move(self):
        self.assertEqual((tri.Triangle(1, 2, 3, 4, 5, 6).move(1, 1)), tri.Triangle(2, 3, 4, 5, 6, 7))

    def test_area(self):
        self.assertEqual(tri.Triangle(-1, 1, 2, 1, -2, -1).area(), 3.0)
