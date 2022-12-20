import unittest
from Stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)

    def test_push(self):
        self.assertEqual(self.stack.push(1), None)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)


if __name__ == '__main__':
    unittest.main()