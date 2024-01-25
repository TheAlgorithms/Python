from bisect import bisect
from itertools import accumulate

# Reference Link: https://en.wikipedia.org/wiki/Continuous_knapsack_problem


def frac_knapsack(
    values: list[int], weights: list[int], capacity: int, max_items: int
) -> float:
    """
    This function implements fractional knapsack problem.

    Args:
        values: List of values of items.
        weights: List of weights of items.
        capacity: Capacity of the knapsack.
        max_items: Number of items.

    Returns:
        Maximum value of items that can be put into the knapsack.

    >>> frac_knapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10, 4)
    105.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 4)
    95.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6], 8, 4)
    Traceback (most recent call last):
        ...
    ValueError: zip() argument 2 is shorter than argument 1
    >>> frac_knapsack([10, 40, 30], [5, 4, 6, 3], 8, 4)
    Traceback (most recent call last):
        ...
    ValueError: zip() argument 2 is longer than argument 1
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 0, 4)
    Traceback (most recent call last):
        ...
    ValueError: Capacity and max_items must be greater than 0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 0)
    Traceback (most recent call last):
        ...
    ValueError: Capacity and max_items must be greater than 0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], -8, 4)
    Traceback (most recent call last):
        ...
    ValueError: Capacity and max_items must be greater than 0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, -4)
    Traceback (most recent call last):
        ...
    ValueError: Capacity and max_items must be greater than 0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 800, 4)
    130
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 400)
    95.0
    >>> frac_knapsack("ABCD", [5, 4, 6, 3], 8, 400)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
    >>> frac_knapsack([500], [30], 10, 1)
    166.66666666666666
    """

    # Input validation
    if capacity <= 0 or max_items <= 0:
        raise ValueError("Capacity and max_items must be greater than 0")

    # sort in descending order of value/weight ratio
    r = sorted(
        zip(values, weights, strict=True), key=lambda x: x[0] / x[1], reverse=True
    )

    values, weights = [i[0] for i in r], [i[1] for i in r]  # unzip
    acc = list(accumulate(weights))  # cumulative sum of weights

    # find the index of the weight just greater than capacity
    k = bisect(acc, capacity)

    if k == 0:  # first item is greater than capacity
        fraction = capacity / weights[0]
        return fraction * values[0]
    elif k < max_items:  # fractional part of the kth item can be put into the knapsack
        fraction = (capacity - acc[k - 1]) / weights[k]
        return sum(values[:k]) + fraction * values[k]
    return sum(values[:k])  # all items can be put into the knapsack


if __name__ == "__main__":
    import doctest

    doctest.testmod()
