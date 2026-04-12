"""
0/1 Knapsack Problem using Dynamic Programming

Problem Statement:
Given weights and values of n items, select items to put in a knapsack of capacity W
to maximize the total value. In the 0/1 knapsack problem, you can either take an item
whole (1) or leave it (0) - fractional parts are not allowed.

Time Complexity: O(n × W) where n is the number of items and W is the knapsack capacity
Space Complexity: O(n × W) for the DP table

Note: This implementation solves the integer weights 0/1 knapsack problem using dynamic
programming. The problem exhibits optimal substructure and overlapping subproblems,
making it suitable for DP.

Key Insight:
For each item i and capacity w, we decide:
- Don't include item i: value = dp[i-1][w]
- Include item i (if weight allows): value = val[i-1] + dp[i-1][w-wt[i-1]]
We choose the maximum of these two options.

Example:
    >>> knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
"""


def mf_knapsack(i: int, wt: list[int], val: list[int], j: int) -> int:
    """
    Memory function approach for 0/1 knapsack problem (top-down with memoization).
    
    This approach only computes subproblems that are actually needed, unlike the
    bottom-up approach which fills the entire DP table. It uses a global DP table
    initialized with -1 to track which subproblems have been solved.
    
    Args:
        i (int): Current item index (1-indexed).
        wt (list[int]): List of item weights.
        val (list[int]): List of item values.
        j (int): Current knapsack capacity.
    
    Returns:
        int: Maximum value achievable with first i items and capacity j.
    
    Global Variables:
        f (list[list[int]]): Memoization table initialized with -1.
    
    Note:
        The global variable `f` must be initialized before calling this function.
        See the example in __main__ for proper initialization.
    """
    global f  # Memoization table
    if f[i][j] < 0:
        if j < wt[i - 1]:
            # Item too heavy, skip it
            f[i][j] = mf_knapsack(i - 1, wt, val, j)
        else:
            # Choose maximum of: excluding vs including current item
            f[i][j] = max(
                mf_knapsack(i - 1, wt, val, j),  # Exclude item i
                mf_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],  # Include item i
            )
    return f[i][j]


def knapsack(w: int, wt: list[int], val: list[int], n: int) -> tuple[int, list[list[int]]]:
    """
    Bottom-up dynamic programming solution for 0/1 knapsack problem.
    
    This iterative approach builds a DP table where dp[i][w_] represents the maximum
    value achievable using the first i items with a knapsack capacity of w_.
    
    Args:
        w (int): Maximum knapsack capacity.
        wt (list[int]): List of item weights (length n).
        val (list[int]): List of item values (length n).
        n (int): Number of items.
    
    Returns:
        tuple[int, list[list[int]]]: A tuple containing:
            - Maximum achievable value
            - The complete DP table for solution reconstruction
    
    Algorithm:
        For each item i and capacity w_:
        - If item fits (wt[i-1] <= w_): 
            dp[i][w_] = max(val[i-1] + dp[i-1][w_-wt[i-1]], dp[i-1][w_])
        - Otherwise:
            dp[i][w_] = dp[i-1][w_]
    
    Examples:
        >>> knapsack(6, [4, 3, 2, 3], [3, 2, 4, 4], 4)[0]
        8
        >>> knapsack(10, [1, 3, 5, 2], [10, 20, 100, 22], 4)[0]
        142
    """
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                # Max of: including item i vs excluding item i
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                # Item too heavy, can't include it
                dp[i][w_] = dp[i - 1][w_]
    
    return dp[n][w], dp


def knapsack_with_example_solution(w: int, wt: list, val: list):
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
    example_optional_set: set = set()
    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
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
    f = [[0] * (w + 1)] + [[0] + [-1] * (w + 1) for _ in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w))  # switched the n and w

    # testing the dynamic programming problem with example
    # the optimal subset for the above example are items 3 and 4
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)
