import unittest

from python.sortings import insertion_sort


class InsertionSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = insertion_sort(arr)
        self.assertEquals(res[0], 1)
        self.assertEquals(res[1], 2)
        self.assertEquals(res[2], 3)
