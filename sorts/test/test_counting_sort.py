import unittest
from .test_sort import TestSort
from ..counting_sort import counting_sort


class TestCountingSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(counting_sort)