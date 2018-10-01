import unittest
from .test_sort import TestSort
from ..selection_sort import selection_sort


class TestSelectionSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(selection_sort)