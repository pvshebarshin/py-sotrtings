import unittest

from python.sortings import bitonic_sort


class BitonicSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2]
        res = bitonic_sort(arr)
        self.assertEquals(res[0], 2)
        self.assertEquals(res[1], 3)
