import unittest

from python.sortings import cycle_sort


class CycleSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = cycle_sort(arr)
        self.assertEquals(res[0], 1)
        self.assertEquals(res[1], 2)
        self.assertEquals(res[2], 3)