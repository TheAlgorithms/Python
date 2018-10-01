import unittest
from .test_sort import TestSort
from ..timsort import timsort


class TestTimSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(timsort)