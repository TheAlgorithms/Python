"""
Created on Mon Oct 3 08:46:07 2022

@author: Parag Kumar Goyal
@license: MIT-license

This file contains the test-suite for the unbounded knapsack problem.
"""
import unittest

from knapsack import unbounded_knapsack as uk


class Test(unittest.TestCase):
    def test_base_case(self):
        """
        test for the base case
        """
        cap = 0
        val = [0]
        w = [0]
        c = len(val)
        self.assertEqual(uk.unbounded_knapsack(cap, w, val, c), 0)

        val = [60]
        w = [10]
        c = len(val)
        self.assertEqual(uk.unbounded_knapsack(cap, w, val, c), 0)

    def test_easy_case(self):
        """
        test for the base case
        """
        cap = 3
        val = [1, 2, 3]
        w = [3, 2, 1]
        c = len(val)
        self.assertEqual(uk.unbounded_knapsack(cap, w, val, c), 9)

    def test_unbounded_knapsack(self):
        """
        test for the unbounded knapsack
        """
        cap = 50
        val = [60, 100, 120]
        w = [10, 20, 30]
        c = len(val)
        self.assertEqual(uk.unbounded_knapsack(cap, w, val, c), 300)

        cap = 100
        val = [1, 30]
        w = [1, 50]
        c = len(val)
        self.assertEqual(uk.unbounded_knapsack(cap, w, val, c), 100)

        cap = 8
        val = [10, 40, 50, 70]
        w = [1, 3, 4, 5]
        c = len(val)
        self.assertEqual(uk.unbounded_knapsack(cap, w, val, c), 110)


if __name__ == "__main__":
    unittest.main()
