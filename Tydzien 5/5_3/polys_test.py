import unittest
import polys as pol


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]  # W(x) = x
        self.p2 = [0, 0, 1]  # W(x) = x^2
        self.p3 = [0, -4, 3]  # W(x) = 3x^2 -4x +0
        self.p4 = [0, -3, 5, -9, -2, 2]  # W(x) = 2x^5 -2x^4 -9x^3 +5x^2 -3x
        self.p5 = [3]  # W(x) = 3
        self.p6 = [0, 0, 0]  # W(x) = 0
        self.p7 = [0]  # W(x) = 0
        self.p8 = [-1, 4, -5, 2]  # W(x) = 2 +4x -5x^2 +2x^3

    def test_add_poly(self):
        self.assertEqual(pol.add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(pol.sub_poly(self.p4, self.p1), [0, -4, 5, -9, -2, 2])

    def test_mul_poly(self):
        self.assertEqual(pol.mul_poly(self.p1, self.p6), [0])

    def test_is_zero(self):
        self.assertFalse(pol.is_zero(self.p1))
        self.assertTrue(pol.is_zero(self.p6))

    def test_eq_poly(self):
        self.assertTrue(pol.eq_poly(self.p6, self.p7))
        self.assertTrue(pol.eq_poly(self.p5, [3]))
        self.assertFalse(pol.eq_poly(self.p1, self.p5))

    def test_eval_poly(self):
        self.assertEqual(pol.eval_poly(self.p8, 2), 3)

    def test_pow_poly(self):
        self.assertEqual(pol.pow_poly(self.p1, 2), [0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(pol.diff_poly(self.p1), [1])
        self.assertEqual(pol.diff_poly(self.p2), [0, 2])


if __name__ == '__main__':
    unittest.main()
