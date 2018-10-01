import unittest
from .test_sort import TestSort
from ..gnome_sort import gnome_sort


class TestGnomeSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(gnome_sort, doesSortInPlace=True)