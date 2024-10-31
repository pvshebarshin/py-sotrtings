import unittest

from python.sortings import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = bubble_sort(arr)
        self.assertEquals(res[0], 1)
        self.assertEquals(res[1], 2)
        self.assertEquals(res[2], 3)
