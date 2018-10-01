import unittest
from .test_sort import TestSort
from ..radix_sort import radixsort


class TestRadixSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(radixsort)