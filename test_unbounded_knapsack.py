"""
Created on Tue Aug 31 16:31:07 2022

This file contains the test-suite for the unbounded_knapsack problem.
"""
import unittest

from unbounded_knapsack import unbounded_knapsack as k


class Test(unittest.TestCase):
    def test_base_case(self):
        """
        test for the base case
        """
        capacity = 0
        value = [0]
        weight = [0]
        length = len(val)
        self.assertEqual(k.unbounded_knapsack(capacity, weight, value, length), 0)

        value = [60]
        weight = [10]
        length = len(val)
        self.assertEqual(k.unbounded_knapsack(capacity, weight, value, length), 0)

    def test_easy_case(self):
        """
        test for the base case
        """
        capacity = 100
        value = [10, 30, 20]
        weight = [5, 10, 15]
        length = len(val)
        self.assertEqual(k.unbounded_knapsack(capacity, weight, value, length), 300)

    def test_knapsack(self):
        """
        test for the knapsack
        """
        capacity = 8
        value = [10, 40, 50, 70]
        weight = [1, 3, 4, 5]
        length = len(val)
        self.assertEqual(k.unbounded_knapsack(capacity, weight, value, length), 110)


if __name__ == "__main__":
    unittest.main()
