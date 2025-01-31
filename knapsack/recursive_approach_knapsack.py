"""
A shopkeeper has bags of wheat that each have different weights and different profits.
Example:
no_of_items = 4
profit = [5, 4, 8, 6]
weight = [1, 2, 4, 5]
max_weight = 5

Constraints:
- max_weight > 0
- profit[i] >= 0
- weight[i] >= 0

Calculate the maximum profit the shopkeeper can make given the maximum weight that can be carried.
"""

from functools import lru_cache

def knapsack(weights: list, values: list, number_of_items: int, max_weight: int, index: int, memo=None) -> int:
    """
    Optimized Recursive Knapsack with Memoization.

    :param weights: List of item weights
    :param values: List of corresponding item profits
    :param number_of_items: Total number of available items
    :param max_weight: Maximum weight capacity of the knapsack
    :param index: Current item index being considered
    :param memo: Dictionary to store computed results for optimization
    :return: Maximum profit possible

    >>> knapsack([1, 2, 4, 5], [5, 4, 8, 6], 4, 5, 0)
    13
    >>> knapsack([3, 4, 5], [10, 9, 8], 3, 25, 0)
    27
    """
    if index == number_of_items:
        return 0

    if memo is None:
        memo = {}

    # If already computed, return stored value
    if (index, max_weight) in memo:
        return memo[(index, max_weight)]

    # Case 1: Skip the current item
    ans1 = knapsack(weights, values, number_of_items, max_weight, index + 1, memo)

    # Case 2: Include the current item (if weight allows)
    ans2 = 0
    if weights[index] <= max_weight:
        ans2 = values[index] + knapsack(weights, values, number_of_items, max_weight - weights[index], index + 1, memo)

    # Store and return the maximum value obtained
    memo[(index, max_weight)] = max(ans1, ans2)
    return memo[(index, max_weight)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
