import unittest

from python.sortings import odd_even_sort


class OddEvenSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = odd_even_sort(arr)
        self.assertEquals(res[0], 1)
        self.assertEquals(res[1], 2)
        self.assertEquals(res[2], 3)