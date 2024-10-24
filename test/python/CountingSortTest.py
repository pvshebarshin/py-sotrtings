import unittest

from python.countingSort import counting_sort


class CountingSortTest(unittest.TestCase):

    def test_simple(self):
        arr = [3, 2, 1]
        res = counting_sort(arr)
        self.assertEquals(res[0], 1)
        self.assertEquals(res[1], 2)
        self.assertEquals(res[2], 3)
