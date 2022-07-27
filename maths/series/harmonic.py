"""
Harmonic mean
Reference: https://en.wikipedia.org/wiki/Harmonic_mean

Harmonic series
Reference: https://en.wikipedia.org/wiki/Harmonic_series(mathematics)
"""


def is_harmonic_series(series: list) -> bool:
    """
    checking whether the input series is arithmetic series or not
    >>> is_harmonic_series([ 1, 2/3, 1/2, 2/5, 1/3])
    True
    >>> is_harmonic_series([ 1, 2/3, 2/5, 1/3])
    False
    >>> is_harmonic_series([1, 2, 3])
    False
    >>> is_harmonic_series([1/2, 1/3, 1/4])
    True
    >>> is_harmonic_series([2/5, 2/10, 2/15, 2/20, 2/25])
    True
    >>> is_harmonic_series(4)
    Traceback (most recent call last):
        ...
    ValueError: Input series is not valid, valid series - [1, 2/3, 2]
    >>> is_harmonic_series([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must be a non empty list
    >>> is_harmonic_series([0])
    Traceback (most recent call last):
        ...
    ValueError: Input series cannot have 0 as an element
    >>> is_harmonic_series([1,2,0,6])
    Traceback (most recent call last):
        ...
    ValueError: Input series cannot have 0 as an element
    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [1, 2/3, 2]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1 and series[0] != 0:
        return True
    rec_series = []
    series_len = len(series)
    for i in range(0, series_len):
        if series[i] == 0:
            raise ValueError("Input series cannot have 0 as an element")
        rec_series.append(1 / series[i])
    common_diff = rec_series[1] - rec_series[0]
    for index in range(2, series_len):
        if rec_series[index] - rec_series[index - 1] != common_diff:
            return False
    return True


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
