"""A recursive implementation of 0-N Knapsack Problem
https://en.wikipedia.org/wiki/Knapsack_problem
"""

from __future__ import annotations

from functools import lru_cache


def knapsack(
    capacity: int,
    weights: list[int],
    values: list[int],
    counter: int,
    allow_repetition: bool = False,
) -> int:
    """
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val
    with option to allow repetitive selection of items

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack(cap, w, val, c)
    220

    Given the repetition is NOT allowed,
    the result is 220 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
    >>> knapsack(cap, w, val, c, True)
    300

    Given the repetition is allowed,
    the result is 300 cause the values of 60*5 (pick 5 times)
    got the weight of 10*5 which is the limit of the capacity.
    """

    @lru_cache
    def knapsack_recur(capacity: int, counter: int) -> int:
        # Base Case
        if counter == 0 or capacity == 0:
            return 0

        # If weight of the nth item is more than Knapsack of capacity,
        #   then this item cannot be included in the optimal solution,
        # else return the maximum of two cases:
        #   (1) nth item included only once (0-1), if allow_repetition is False
        #       nth item included one or more times (0-N), if allow_repetition is True
        #   (2) not included
        if weights[counter - 1] > capacity:
            return knapsack_recur(capacity, counter - 1)
        else:
            left_capacity = capacity - weights[counter - 1]
            new_value_included = values[counter - 1] + knapsack_recur(
                left_capacity, counter - 1 if not allow_repetition else counter
            )
            without_new_value = knapsack_recur(capacity, counter - 1)
            return max(new_value_included, without_new_value)

    return knapsack_recur(capacity, counter)


def knapsack_with_count(
    capacity: int,
    weights: list[int],
    values: list[int],
    counter: int,
    allow_repetition: bool = False,
) -> tuple[int, int]:
    """
    Return both the maximum knapsack value and the number of optimal subsets.

    The return value is ``(max_value, number_of_optimal_subsets)``.
    If multiple choices produce the same maximum value, their counts are added.

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack_with_count(cap, w, val, c)
    (220, 1)
    >>> knapsack_with_count(cap, w, val, c, True)
    (300, 1)
    >>> knapsack_with_count(3, [1, 2, 3], [1, 2, 3], 3)
    (3, 2)
    >>> knapsack_with_count(2, [1, 2], [1, 2], 2, True)
    (2, 2)
    """

    @lru_cache
    def knapsack_recur(remaining_capacity: int, item_count: int) -> tuple[int, int]:
        # Base Case: one empty subset yields value 0.
        if item_count == 0 or remaining_capacity == 0:
            return 0, 1

        if weights[item_count - 1] > remaining_capacity:
            return knapsack_recur(remaining_capacity, item_count - 1)

        left_capacity = remaining_capacity - weights[item_count - 1]
        included_value, included_count = knapsack_recur(
            left_capacity, item_count if allow_repetition else item_count - 1
        )
        included_value += values[item_count - 1]

        excluded_value, excluded_count = knapsack_recur(
            remaining_capacity, item_count - 1
        )

        if included_value > excluded_value:
            return included_value, included_count
        if excluded_value > included_value:
            return excluded_value, excluded_count
        return included_value, included_count + excluded_count

    return knapsack_recur(capacity, counter)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
