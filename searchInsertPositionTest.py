import unittest
from searchInsertPosition import searchInsertBinary

class TestSearchInsert(unittest.TestCase):
    def test_search(self):
        self.assertEqual(searchInsertBinary([1,3,5,6], 5), 2)
        self.assertEqual(searchInsertBinary([1,3,5,6], 2), 1)
        self.assertEqual(searchInsertBinary([1,3,5,6], 7), 4)
        self.assertEqual(searchInsertBinary([1,3,5,6], 0), 0)
        self.assertEqual(searchInsertBinary([1001], 5), 0)
        self.assertEqual(searchInsertBinary([1], 2), 1)