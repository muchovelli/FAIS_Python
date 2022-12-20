import unittest
from random_queue import RandomQueue


class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue()

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.queue.is_full(), False)

    def test_insert(self):
        self.assertEqual(self.queue.insert(1), None)

    def test_remove(self):
        self.assertEqual(self.queue.remove(), None)

    def test_clear(self):
        self.assertEqual(self.queue.clear(), None)


if __name__ == '__main__':
    unittest.main()