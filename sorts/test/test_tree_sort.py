import unittest
from .test_sort import TestSort
from ..tree_sort import treesort


class TestTreeSort(TestSort):
    def test_sort(self):
        self.canSortDuplicateValues = False
        self.runSortingSuite(treesort)