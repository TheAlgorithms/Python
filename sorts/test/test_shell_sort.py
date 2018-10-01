import unittest
from .test_sort import TestSort
from ..shell_sort import shell_sort


class TestShellSort(TestSort):
    def test_sort(self):
        self.runSortingSuite(shell_sort)