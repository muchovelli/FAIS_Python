import unittest
from single_list import SingleList, Node


class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.list = SingleList()
        self.list.insert_head(Node(1))
        self.list.insert_head(Node(2))
        self.list.insert_head(Node(3))
        self.list.insert_head(Node(4))
        self.list.insert_head(Node(5))

    def test_is_empty(self):
        self.assertEqual(self.list.is_empty(), False)

    def test_count(self):
        self.assertEqual(self.list.count(), 5)

    def test_insert_head(self):
        self.assertEqual(self.list.insert_head(Node(6)), SingleList().insert_head(Node(6)))

    def test_insert_tail(self):
        self.assertEqual(self.list.insert_tail(Node(6)), SingleList().insert_tail(Node(6)))

    def test_remove_head(self):
        self.assertEqual(self.list.remove_head(), SingleList().remove_head())


if __name__ == '__main__':
    unittest.main()
