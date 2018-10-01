import unittest
from .test_sort import TestSort
from ..cocktail_shaker_sort import cocktail_shaker_sort


class TestCocktailShakerSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(cocktail_shaker_sort, doesSortInPlace=True)