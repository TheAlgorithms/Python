import unittest
from .test_sort import TestSort
from ..bubble_sort import bubble_sort


class TestBubbleSort(TestSort):    
    def test_sort(self):
        self.runSortingSuite(bubble_sort)