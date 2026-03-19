"""
Given weights and values of n items, put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

Note that only the integer weights 0-1 knapsack problem is solvable
using dynamic programming.

This module provides multiple approaches:
- ``knapsack``: Bottom-up DP with O(n*W) space and solution reconstruction.
- ``knapsack_with_example_solution``: Wrapper that returns optimal value and subset.
- ``knapsack_optimized``: Space-optimized bottom-up DP using O(W) space (value only).
- ``mf_knapsack``: Top-down memoized approach (memory function) with no global state.
"""


def mf_knapsack(
    i: int,
    wt: list[int],
    val: list[int],
    j: int,
    memo: list[list[int]] | None = None,
) -> int:
    """
    Solve the 0-1 knapsack problem using top-down memoization (memory function).

    Unlike the previous implementation, this version does **not** rely on a global
    ``f`` table. The memoization table is passed explicitly or created on first call.

    :param i: Number of items to consider (1-indexed).
    :param wt: List of item weights.
    :param val: List of item values.
    :param j: Remaining knapsack capacity.
    :param memo: Optional pre-allocated memoization table of shape ``(i+1) x (j+1)``
        initialised with ``-1`` for unsolved sub-problems and ``0`` for base cases.
        When ``None`` a table is created automatically.
    :return: Maximum obtainable value considering items ``1..i`` with capacity ``j``.

    Examples:
    >>> mf_knapsack(4, [4, 3, 2, 3], [3, 2, 4, 4], 6)
    8
    >>> mf_knapsack(0, [1, 2], [10, 20], 5)
    0
    >>> mf_knapsack(3, [1, 3, 5], [10, 20, 100], 10)
    130
    >>> mf_knapsack(1, [5], [50], 3)
    0
    >>> mf_knapsack(1, [5], [50], 5)
    50
    """
    if memo is None:
        memo = [[0] * (j + 1)] + [[0] + [-1] * j for _ in range(i)]

    if i == 0 or j == 0:
        return 0

    if memo[i][j] >= 0:
        return memo[i][j]

    if j < wt[i - 1]:
        memo[i][j] = mf_knapsack(i - 1, wt, val, j, memo)
    else:
        memo[i][j] = max(
            mf_knapsack(i - 1, wt, val, j, memo),
            mf_knapsack(i - 1, wt, val, j - wt[i - 1], memo) + val[i - 1],
        )
    return memo[i][j]


def knapsack(
    w: int, wt: list[int], val: list[int], n: int
) -> tuple[int, list[list[int]]]:
    """
    Solve the 0-1 knapsack problem using bottom-up dynamic programming.

    :param w: Maximum knapsack capacity.
    :param wt: List of item weights.
    :param val: List of item values.
    :param n: Number of items.
    :return: A tuple ``(optimal_value, dp_table)`` where ``dp_table`` can be used
        for solution reconstruction via ``_construct_solution``.

    Examples:
    >>> knapsack(6, [4, 3, 2, 3], [3, 2, 4, 4], 4)[0]
    8
    >>> knapsack(10, [1, 3, 5, 2], [10, 20, 100, 22], 4)[0]
    142
    >>> knapsack(0, [1, 2], [10, 20], 2)[0]
    0
    >>> knapsack(5, [], [], 0)[0]
    0
    """
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w], dp


def knapsack_optimized(w: int, wt: list[int], val: list[int], n: int) -> int:
    """
    Solve the 0-1 knapsack problem using space-optimized bottom-up DP.

    Uses a single 1-D array of size ``w + 1`` instead of a 2-D ``(n+1) x (w+1)``
    table, reducing space complexity from O(n*W) to O(W).

    .. note::
        This variant returns only the optimal value; it does **not** support
        solution reconstruction (i.e. which items are included).

    :param w: Maximum knapsack capacity.
    :param wt: List of item weights.
    :param val: List of item values.
    :param n: Number of items.
    :return: Maximum obtainable value.

    Examples:
    >>> knapsack_optimized(6, [4, 3, 2, 3], [3, 2, 4, 4], 4)
    8
    >>> knapsack_optimized(10, [1, 3, 5, 2], [10, 20, 100, 22], 4)
    142
    >>> knapsack_optimized(0, [1, 2], [10, 20], 2)
    0
    >>> knapsack_optimized(5, [], [], 0)
    0
    >>> knapsack_optimized(50, [10, 20, 30], [60, 100, 120], 3)
    220
    """
    dp = [0] * (w + 1)

    for i in range(n):
        # Traverse capacity in reverse so each item is used at most once
        for capacity in range(w, wt[i] - 1, -1):
            dp[capacity] = max(dp[capacity], dp[capacity - wt[i]] + val[i])

    return dp[w]


def knapsack_with_example_solution(
    w: int, wt: list[int], val: list[int]
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
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError(
            "Both the weights and values vectors must be either lists or tuples"
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
    example_optional_set: set[int] = set()
    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(
    dp: list[list[int]], wt: list[int], i: int, j: int, optimal_set: set[int]
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
    import doctest

    doctest.testmod()

    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w))

    # Space-optimized knapsack
    print(f"Optimized: {knapsack_optimized(w, wt, val, n)}")

    # testing the dynamic programming problem with example
    # the optimal subset for the above example are items 3 and 4
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)
