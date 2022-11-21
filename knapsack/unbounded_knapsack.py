"""
    Unbounded Knapsack Problem :
    https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

    0-1 Knapsack Problem :
    https://en.wikipedia.org/wiki/Knapsack_problem
    https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

    The unbounded knapsack problem is an extension of the 0-1 knapsack problem.
    The main difference is that it is possible to utilize an infinite number of items
    in the unbounded knapsack problem.
    In other words, the problem statement is :

    Given a knapsack of capacity W
    and n types of items with certain values and weights,
    calculate the maximum total value of items the knapsack can carry.
    It is allowed to use unlimited number of instances of an item.
"""


def knapsack(capacity: int, items_weights: list[int], items_values: list[int]) -> int:
    """
    Returns the maximum value of items that can be put in a knapsack of a capacity c.
    Each type of item has a specific weight and value.
    It is possible to carry unlimited number of instances of an item.

    >>> c = 70
    >>> items_values = [40, 900, 120]
    >>> items_weights = [10, 20, 30]
    >>> knapsack(c, items_weights, items_values)
    2740

    The result is 2740 because it is possible to carry
    three items of value 900 and weight 20
    and one item of value 40 and weight 10.

    >>> c = 10
    >>> items_values = [10, 10]
    >>> items_weights = [1, 2]
    >>> knapsack(c, items_weights, items_values)
    100

    The result is 100 because it is possible to carry
    ten items of value 10 and weight 1.

    >>> c = 100
    >>> items_values = [999, 9999]
    >>> items_weights = [200, 400]
    >>> knapsack(c, items_weights, items_values)
    0

    The result is 0 because no items can be carried.
    """

    # n is the number of items
    n = len(items_weights)

    # dp stores the answer of the problem for a given capacity.
    # So dp[c] stores the maximum value of items that can be put in a knapsack
    # of a capacity c.
    # Initially, dp[c] starts with 0.
    dp = [0 for x in range(capacity + 1)]

    for i in range(n):

        # weight of the i-th item
        weight = items_weights[i]

        # value of the i-th item
        value = items_values[i]

        for c in range(weight, capacity + 1):
            dp[c] = max(dp[c], dp[c - weight] + value)

    return dp[capacity]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
