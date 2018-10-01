import unittest
from .test_sort import TestSort
from ..insertion_sort import insertion_sort


class TestInsertionSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(insertion_sort)