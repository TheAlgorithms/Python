import unittest
from .test_sort import TestSort
from ..pancake_sort import pancakesort


class TestPancakeSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(pancakesort)