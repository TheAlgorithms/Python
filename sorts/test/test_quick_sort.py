import unittest
from .test_sort import TestSort
from ..quick_sort import quick_sort
from ..quick_sort_3partition import quick_sort_3partition


class TestQuickSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(quick_sort)

    def test_sort_3partition(self):
        self.runSortingSuite(quick_sort_3partition, doesSortInPlace=True)

    # TODO: Random Normal Distribution Quick Sort