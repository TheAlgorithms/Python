import unittest
from .test_sort import TestSort
from ..heap_sort import heap_sort


class TestHeapSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(heap_sort)