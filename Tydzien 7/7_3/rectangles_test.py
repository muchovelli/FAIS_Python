import unittest
import rectangles as rec
import points as p


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = rec.Rectangle(1, 2, 3, 4)
        self.r2 = rec.Rectangle(1, 2, 3, 4)
        self.r3 = rec.Rectangle(1, 2, 3, 5)

    def test_print(self):
        self.assertEqual(str(self.r1), "[(1, 2), (3, 4)]")
        self.assertEqual(repr(self.r1), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertEqual(self.r1 == self.r2, True)
        self.assertEqual(self.r1 == self.r3, False)

    def test_ne(self):
        self.assertEqual(self.r1 != self.r2, False)
        self.assertEqual(self.r1 != self.r3, True)

    def test_center(self):
        self.assertEqual(rec.Rectangle(1, 2, 3, 4).center(), p.Point(2, 3))

    def test_area(self):
        self.assertEqual(self.r1.area(), 4)

    def test_move(self):
        self.assertEqual(self.r1.move(1, 1), rec.Rectangle(2, 3, 4, 5))

    def test_intersection(self):
        self.assertEqual(self.r1.intersection(self.r2), rec.Rectangle(1, 2, 3, 4))
        self.assertEqual(self.r1.intersection(self.r3), rec.Rectangle(1, 2, 3, 4))
        self.assertEqual(self.r1.intersection(rec.Rectangle(2, 3, 4, 17)), rec.Rectangle(2, 3, 3, 4))

    def test_make4(self):
        self.assertEqual(self.r1.make4(), (
        rec.Rectangle(1, 2, 2, 3), rec.Rectangle(2, 2, 3, 3), rec.Rectangle(1, 3, 2, 4), rec.Rectangle(2, 3, 3, 4)))


if __name__ == '__main__':
    unittest.main()
