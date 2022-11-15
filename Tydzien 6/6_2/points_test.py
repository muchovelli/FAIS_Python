# Kod testujący moduł.

import unittest
import points as p

class TestPolynomials(unittest.TestCase):

    # Testy dla klasy Point
    def test_print(self):
        self.assertEqual(str(p.Point(1, 2)), "(1, 2)")
        self.assertEqual(repr(p.Point(1, 2)), "Point(1, 2)")

    def test_eq(self):
        self.assertEqual(p.Point(1, 2) == p.Point(1, 2), True)
        self.assertEqual(p.Point(1, 2) == p.Point(2, 1), False)

    def test_ne(self):
        self.assertEqual(p.Point(1, 2) != p.Point(1, 2), False)
        self.assertEqual(p.Point(1, 2) != p.Point(2, 1), True)

    def test_add(self):
        self.assertEqual(p.Point(1, 2) + p.Point(2, 1), p.Point(3, 3))
        self.assertEqual(p.Point(1, 2) + p.Point(2, 1), p.Point(3, 3))

    def test_sub(self):
        self.assertEqual(p.Point(1, 2) - p.Point(2, 1), p.Point(-1, 1))
        self.assertEqual(p.Point(1, 2) - p.Point(2, 1), p.Point(-1, 1))

    def test_mul(self):
        self.assertEqual(p.Point(1, 2) * p.Point(2, 1), 4)
        self.assertEqual(p.Point(1, 2) * p.Point(2, 1), 4)

    def test_cross(self):
        self.assertEqual(p.Point(1, 2).cross(p.Point(2, 1)), -3)
        self.assertEqual(p.Point(1, 2).cross(p.Point(2, 1)), -3)

    def test_length(self):
        self.assertEqual(p.Point(1, 2).length(), 2.23606797749979)
        self.assertEqual(p.Point(1, 2).length(), 2.23606797749979)

    def test_hash(self):
        self.assertEqual(hash(p.Point(1, 2)), hash(p.Point(1, 2)))
        self.assertEqual(hash(p.Point(1, 2)), hash(p.Point(1, 2)))

