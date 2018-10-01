import unittest
from .test_sort import TestSort
from ..bogosort import bogosort


class TestBogoSort(TestSort):    
    def test_sort(self):
        self.runSortingSuite(bogosort)