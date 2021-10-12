"""
Arithmetic mean
Reference: https://en.wikipedia.org/wiki/Arithmetic_mean
"""


def arithmetic_mean(series: list) -> float:
    """
    return the arithmetic mean of series

    >>> arithmetic_mean([2, 4, 6])
    4.0
    >>> arithmetic_mean([3, 6, 9, 12])
    7.5
    >>> arithmetic_mean(4)
    Traceback (most recent call last):
        ...
    ValueError: Input series is not valid, valid series - [2, 4, 6]
    >>> arithmetic_mean([4, 8, 1])
    4.333333333333333
    >>> arithmetic_mean([1, 2, 3])
    2.0
    >>> arithmetic_mean([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must be a non empty list

    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 6]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    answer = 0
    for val in series:
        answer += val
    return answer / len(series)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
