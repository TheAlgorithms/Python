import unittest
from .test_sort import TestSort
from ..merge_sort import merge_sort
from ..merge_sort_fastest import merge_sort as merge_sort_fastest


class TestMergeSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(merge_sort)

    def test_sort_fastest(self):
        self.runSortingSuite(merge_sort_fastest)