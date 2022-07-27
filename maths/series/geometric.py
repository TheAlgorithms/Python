"""
Geometric Mean
Reference :  https://en.wikipedia.org/wiki/Geometric_mean

Geometric series
Reference: https://en.wikipedia.org/wiki/Geometric_series
"""


def is_geometric_series(series: list) -> bool:
    """
    checking whether the input series is geometric series or not
    >>> is_geometric_series([2, 4, 8])
    True
    >>> is_geometric_series([3, 6, 12, 24])
    True
    >>> is_geometric_series([1, 2, 3])
    False
    >>> is_geometric_series([0, 0, 3])
    False
    >>> is_geometric_series([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must be a non empty list
    >>> is_geometric_series(4)
    Traceback (most recent call last):
        ...
    ValueError: Input series is not valid, valid series - [2, 4, 8]
    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 8]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1:
        return True
    try:
        common_ratio = series[1] / series[0]
        for index in range(len(series) - 1):
            if series[index + 1] / series[index] != common_ratio:
                return False
    except ZeroDivisionError:
        return False
    return True


def geometric_mean(series: list) -> float:
    """
    return the geometric mean of series

    >>> geometric_mean([2, 4, 8])
    3.9999999999999996
    >>> geometric_mean([3, 6, 12, 24])
    8.48528137423857
    >>> geometric_mean([4, 8, 16])
    7.999999999999999
    >>> geometric_mean(4)
    Traceback (most recent call last):
        ...
    ValueError: Input series is not valid, valid series - [2, 4, 8]
    >>> geometric_mean([1, 2, 3])
    1.8171205928321397
    >>> geometric_mean([0, 2, 3])
    0.0
    >>> geometric_mean([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must be a non empty list

    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 8]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    answer = 1
    for value in series:
        answer *= value
    return pow(answer, 1 / len(series))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
