import unittest

from python.sortings import pancake_sort


class PancakeSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = pancake_sort(arr)
        self.assertEquals(res[0], 1)
        self.assertEquals(res[1], 2)
        self.assertEquals(res[2], 3)