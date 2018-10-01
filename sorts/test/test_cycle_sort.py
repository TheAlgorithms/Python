import unittest
from .test_sort import TestSort
from ..cyclesort import cycle_sort


class TestCycleSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(cycle_sort, doesSortInPlace=True)