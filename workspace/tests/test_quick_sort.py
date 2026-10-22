import unittest
from quick_sort import quick_sort, list1, list2, list3

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort(list1), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quick_sort(list2), [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14])
        self.assertEqual(quick_sort(list3), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
