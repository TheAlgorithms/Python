"""
Weighted Average (Weighted Mean)

A weighted average is an average in which each value has a specific weight
assigned to it. Values with higher weights contribute more to the final result.

Formula: weighted_avg = sum(value * weight) / sum(weights)

Reference: https://en.wikipedia.org/wiki/Weighted_arithmetic_mean
"""

from __future__ import annotations


def weighted_average(values: list[float], weights: list[float]) -> float:
    """
    Calculate the weighted average of a list of values with corresponding weights.

    :param values: List of numeric values.
    :param weights: List of weights corresponding to each value.
    :return: The weighted average as a float.

    >>> weighted_average([10, 20, 30], [1, 2, 3])
    23.333333333333332
    >>> weighted_average([100, 200], [0.5, 0.5])
    150.0
    >>> weighted_average([5], [2])
    5.0
    >>> weighted_average([], [])
    Traceback (most recent call last):
        ...
    ValueError: Values and weights lists must not be empty
    >>> weighted_average([1, 2], [1])
    Traceback (most recent call last):
        ...
    ValueError: Values and weights must have the same length
    >>> weighted_average([1, 2, 3], [-1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: All weights must be non-negative
    >>> weighted_average([1, 2, 3], [0, 0, 0])
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Sum of weights must not be zero
    """

    # ১. Error Handling
    if not values or not weights:
        raise ValueError("Values and weights lists must not be empty")

    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length")

    if any(w < 0 for w in weights):
        raise ValueError("All weights must be non-negative")

    total_weight = sum(weights)
    if total_weight == 0:
        raise ZeroDivisionError("Sum of weights must not be zero")

    # ২. Main Calculation
    return sum(value * weight for value, weight in zip(values, weights)) / total_weight


if __name__ == "__main__":
    import doctest

    doctest.testmod()
