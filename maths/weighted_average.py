from __future__ import annotations


def weighted_average(values: list[float], weights: list[float]) -> float:
    """
    Return the weighted average of a list of values given their corresponding weights.

    https://en.wikipedia.org/wiki/Weighted_arithmetic_mean

    >>> weighted_average([1, 2, 3], [1, 1, 1])
    2.0
    >>> weighted_average([10, 20, 30], [1, 2, 3])
    23.333333333333332
    >>> weighted_average([5, 15], [1, 3])
    12.5
    >>> weighted_average([100], [0.5])
    100.0
    >>> weighted_average([], [])
    Traceback (most recent call last):
        ...
    ValueError: Inputs cannot be empty
    >>> weighted_average([1, 2], [1])
    Traceback (most recent call last):
        ...
    ValueError: Values and weights must have the same length
    >>> weighted_average([1, 2, 3], [0, 0, 0])
    Traceback (most recent call last):
        ...
    ValueError: Sum of weights cannot be zero
    """
    if not values and not weights:
        raise ValueError("Inputs cannot be empty")
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Sum of weights cannot be zero")
    return sum(value * weight for value, weight in zip(values, weights)) / total_weight


if __name__ == "__main__":
    import doctest

    doctest.testmod()
