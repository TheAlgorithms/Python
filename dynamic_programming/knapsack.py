"""
See: https://en.wikipedia.org/wiki/Knapsack_problem

Given weights and values of n items, put these items in a knapsack of
 capacity W to get the maximum total value in the knapsack.

Note that only the integer weights 0-1 knapsack problem is solvable
 using dynamic programming.
"""

from typing import Sequence

cache = None


def knapsack(max_weight: int, weights: Sequence[int], values: Sequence[int], n: int):
    """
    A solution to the classic knapsack problem, without the use of global variables.
    """
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight], dp


def knapsack_with_constructed_solution(max_weight: int, weights: Sequence[int], values: Sequence[int]):
    """
    Solves the integer weights knapsack problem returns one of
    the several possible optimal subsets.

    Parameters
    ---------

    max_weight: int, the total maximum weight for the given knapsack problem.
    weights: list, the vector of weights for all items where weights[i] is the weight
    of the i-th item.
    values: list, the vector of values for all items where values[i] is the value
    of the i-th item

    Returns
    -------
    optimal_val: float, the optimal value for the given knapsack problem
    example_optional_set: set, the indices of one of the optimal subsets
    which gave rise to the optimal value.

    Examples
    -------
    >>> knapsack_with_constructed_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
    >>> knapsack_with_constructed_solution(6, [4, 3, 2, 3], [3, 2, 4, 4])
    (8, {3, 4})
    >>> knapsack_with_constructed_solution(6, [4, 3, 2, 3], [3, 2, 4])
    Traceback (most recent call last):
        ...
    ValueError: The number of weights must be the same as the number of values.
    But got 4 weights and 3 values
    """
    num_items = len(weights)
    if num_items != len(values):
        raise ValueError(
            "The number of weights must be the "
            "same as the number of values.\nBut "
            f"got {num_items} weights and {len(values)} values"
        )
    for i in range(num_items):
        if not isinstance(weights[i], int):
            raise TypeError(
                "All weights must be integers but "
                f"got weight of type {type(weights[i])} at index {i}"
            )

    optimal_val, dp_table = knapsack(max_weight, weights, values, num_items)
    example_optional_set: set = set()
    _construct_solution(dp_table, weights, num_items, max_weight, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(dp: list[Sequence[int]], weights: Sequence[int], i: int, j: int, optimal_set: set[int]):
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights

    Parameters
    ---------

    dp: list of list, the table of a solved integer weight dynamic programming problem

    weights: a sequence of integers, the vector of weights of the items
    i: int, the index of the  item under consideration
    j: int, the current possible maximum weight
    optimal_set: set, the optimal subset so far. This gets modified by the function.

    Returns
    -------
    None

    """
    # for the current item i at a maximum weight j to be part of an optimal subset,
    # the optimal value at (i, j) must be greater than the optimal value at (i-1, j).
    # where i - 1 means considering only the previous items at the given maximum weight
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, weights, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, weights, i - 1, j - weights[i - 1], optimal_set)


def cached_knapsack(i: int, weights: list, values: list, j: int):
    """
    This code involves the concept of memory functions (cache).
    Here we solve the subproblems which are needed, unlike the below example.
    cache is a 2D array with -1s filled up.
    """
    global cache  # a global dynamic programming table for knapsack
    assert cache is not None

    if cache[i][j] < 0:
        if j < weights[i - 1]:
            optimal_value = cached_knapsack(i - 1, weights, values, j)
        else:
            optimal_value = max(
                cached_knapsack(i - 1, weights, values, j),
                cached_knapsack(i - 1, weights, values, j - weights[i - 1])
                + values[i - 1],
            )
        cache[i][j] = optimal_value
    return cache[i][j]


def test_algorithm_equivalence():
    """
    test that both knapsack algorithms return the optimal result.
    """
    values1 = [3, 2, 4, 4]
    weights1 = [4, 3, 2, 3]
    n = 4
    w = 6
    optimal_solution, optimal_subset = knapsack_with_constructed_solution(
        w, weights1, values1
    )
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}

    global cache
    cache = [[0] * (w + 1)] + [[0] + [-1 for _ in range(w + 1)] for _ in range(n + 1)]
    optimal_solution_again = cached_knapsack(n, weights1, values1, w)
    assert optimal_solution_again == 8


if __name__ == "__main__":
    """run tests."""
    import doctest

    doctest.testmod()
    test_algorithm_equivalence()
