import unittest

from python.sortings import merge_sort


class MergeSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = merge_sort(arr)
        self.assertEquals(arr[0], 1)
        self.assertEquals(arr[1], 2)
        self.assertEquals(arr[2], 3)