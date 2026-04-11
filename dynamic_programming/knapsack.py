"""
Given weights and values of n items, put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

Note that only the integer weights 0-1 knapsack problem is solvable
using dynamic programming.
"""

from __future__ import annotations

from collections.abc import Sequence
from functools import lru_cache


def mf_knapsack(i: int, wt: Sequence[int], val: Sequence[int], j: int) -> int:
    """
    Return the optimal value for the 0/1 knapsack problem using memoization.

    This implementation caches subproblems with ``functools.lru_cache`` and avoids
    global mutable state.

    >>> mf_knapsack(4, [4, 3, 2, 3], [3, 2, 4, 4], 6)
    8
    >>> mf_knapsack(3, [10, 20, 30], [60, 100, 120], 50)
    220
    >>> mf_knapsack(0, [1], [10], 50)
    0
    """
    if i < 0:
        raise ValueError("The number of items to consider cannot be negative.")
    if j < 0:
        raise ValueError("The knapsack capacity cannot be negative.")
    if len(wt) != len(val):
        raise ValueError("The number of weights must match the number of values.")
    if i > len(wt):
        raise ValueError("The number of items to consider cannot exceed input length.")

    weights = tuple(wt)
    values = tuple(val)

    @lru_cache(maxsize=None)
    def solve(item_count: int, capacity: int) -> int:
        if item_count == 0 or capacity == 0:
            return 0
        if weights[item_count - 1] > capacity:
            return solve(item_count - 1, capacity)
        return max(
            solve(item_count - 1, capacity),
            solve(item_count - 1, capacity - weights[item_count - 1])
            + values[item_count - 1],
        )

    return solve(i, j)


def knapsack(
    w: int, wt: Sequence[int], val: Sequence[int], n: int
) -> tuple[int, list[list[int]]]:
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w], dp


def knapsack_with_example_solution(
    w: int, wt: Sequence[int], val: Sequence[int]
) -> tuple[int, set[int]]:
    """
    Solves the integer weights knapsack problem returns one of
    the several possible optimal subsets.

    Parameters
    ----------

    * `w`: int, the total maximum weight for the given knapsack problem.
    * `wt`: list, the vector of weights for all items where ``wt[i]`` is the weight
       of the ``i``-th item.
    * `val`: list, the vector of values for all items where ``val[i]`` is the value
      of the ``i``-th item

    Returns
    -------

    * `optimal_val`: float, the optimal value for the given knapsack problem
    * `example_optional_set`: set, the indices of one of the optimal subsets
      which gave rise to the optimal value.

    Examples
    --------

    >>> knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4, 4])
    (8, {3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4])
    Traceback (most recent call last):
        ...
    ValueError: The number of weights must be the same as the number of values.
    But got 4 weights and 3 values
    """
    if not (
        isinstance(wt, Sequence)
        and not isinstance(wt, (str, bytes))
        and isinstance(val, Sequence)
        and not isinstance(val, (str, bytes))
    ):
        raise ValueError(
            "Both the weights and values vectors must be non-string sequences"
        )

    num_items = len(wt)
    if num_items != len(val):
        msg = (
            "The number of weights must be the same as the number of values.\n"
            f"But got {num_items} weights and {len(val)} values"
        )
        raise ValueError(msg)
    for i in range(num_items):
        if not isinstance(wt[i], int):
            msg = (
                "All weights must be integers but got weight of "
                f"type {type(wt[i])} at index {i}"
            )
            raise TypeError(msg)

    optimal_val, dp_table = knapsack(w, wt, val, num_items)
    example_optional_set: set = set()
    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(
    dp: list[list[int]], wt: Sequence[int], i: int, j: int, optimal_set: set[int]
) -> None:
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights

    Parameters
    ----------

    * `dp`: list of list, the table of a solved integer weight dynamic programming
      problem
    * `wt`: list or tuple, the vector of weights of the items
    * `i`: int, the index of the item under consideration
    * `j`: int, the current possible maximum weight
    * `optimal_set`: set, the optimal subset so far. This gets modified by the function.

    Returns
    -------

    ``None``
    """
    # for the current item i at a maximum weight j to be part of an optimal subset,
    # the optimal value at (i, j) must be greater than the optimal value at (i-1, j).
    # where i - 1 means considering only the previous items at the given maximum weight
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w))

    # testing the dynamic programming problem with example
    # the optimal subset for the above example are items 3 and 4
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)
