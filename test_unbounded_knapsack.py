"""
Created on Fri Oct 16 09:31:07 2020

@author: Dr. Tobias Schröder
@license: MIT-license

This file contains the test-suite for the unbounded_knapsack problem.
"""
import unittest

from unbounded_knapsack import unbounded_knapsack as k


class Test(unittest.TestCase):
    def test_base_case(self):
        """
        test for the base case
        """
        cap = 0
        val = [0]
        w = [0]
        c = len(val)
        self.assertEqual(k.unbounded_knapsack(cap, w, val, c), 0)

        val = [60]
        w = [10]
        c = len(val)
        self.assertEqual(k.unbounded_knapsack(cap, w, val, c), 0)

    def test_easy_case(self):
        """
        test for the base case
        """
        cap = 100
        val = [10, 30, 20]
        w = [5, 10, 15]
        c = len(val)
        self.assertEqual(k.unbounded_knapsack(cap, w, val, c), 300)

    def test_knapsack(self):
        """
        test for the knapsack
        """
        cap = 8
        val = [10, 40, 50, 70]
        w = [1, 3, 4, 5]
        c = len(val)
        self.assertEqual(k.unbounded_knapsack(cap, w, val, c), 110)


if __name__ == "__main__":
    unittest.main()
