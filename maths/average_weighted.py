from __future__ import annotations


def weighted_mean(values: list[float], weights: list[float]) -> float:
    """
    Return the weighted mean of a list of values given their weights.
    Wiki: https://en.wikipedia.org/wiki/Weighted_arithmetic_mean

    >>> weighted_mean([10, 20, 30], [1, 2, 3])
    23.333333333333332
    >>> weighted_mean([5, 5, 5], [1, 1, 1])
    5.0
    >>> weighted_mean([], [])
    Traceback (most recent call last):
        ...
    ValueError: values and weights cannot be empty
    >>> weighted_mean([1, 2], [1])
    Traceback (most recent call last):
        ...
    ValueError: values and weights must have the same length
    >>> weighted_mean([1, 2], [0, 0])
    Traceback (most recent call last):
        ...
    ValueError: sum of weights cannot be zero
    """
    if len(values) == 0:
        raise ValueError("values and weights cannot be empty")
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if sum(weights) == 0:
        raise ValueError("sum of weights cannot be zero")
    return sum(x * w for x, w in zip(values, weights)) / sum(weights)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
