"""
HARMONIC MEAN : https://en.wikipedia.org/wiki/Harmonic_mean

"""


def harmonic_mean(series: list) -> float:
    """
    return the harmonic mean of series

    >>> harmonic_mean([1, 4, 4])
    2.0
    >>> harmonic_mean([3, 6, 9, 12])
    5.759999999999999
    >>> harmonic_mean(4)
    Traceback (most recent call last):
        ...
    ValueError: Input series is not valid, valid series - [2, 4, 6]
    >>> harmonic_mean([1, 2, 3])
    1.6363636363636365
    >>> harmonic_mean([])
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
        answer += 1 / val
    return len(series) / answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
