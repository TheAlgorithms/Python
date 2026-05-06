def is_alternate_harmonic_series(series: list) -> bool:
    """
    Web Biblography
    https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)

    checking whether the input series is alternate harmonic series or not
    >>> is_alternate_harmonic_series([1, -1/2, 1/3, -1/4, 1/5])
    True
    >>> is_alternate_harmonic_series([2/5, -2/10, 2/15, -2/20, 2/25])
    True
    >>> is_alternate_harmonic_series([1, 1/2, 1/3, 1/4])
    False
    >>> is_alternate_harmonic_series([1, -1/2, 1/4, -1/8])
    False
    >>> is_alternate_harmonic_series(4)
    Traceback (most recent call last):
        ...
    ValueError: Input series is not valid, valid series - [1, 2/3, 2]
    >>> is_alternate_harmonic_series([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must be a non empty list
    >>> is_alternate_harmonic_series([0])
    Traceback (most recent call last):
        ...
    ValueError: Input series cannot have 0 as an element
    >>> is_alternate_harmonic_series([1,2,0,6])
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
    receprocal= []
    series_len = len(series)
    for i in range(series_len):
        if series[i] == 0:
            raise ValueError("Input series cannot have 0 as an element")
        receprocal.append(1 / series[i])
    common_diff = abs(receprocal[1]) - abs(receprocal[0])
    for index in range(2, series_len):
        if abs(receprocal[index]) - abs(receprocal[index - 1]) != common_diff or receprocal[index]*receprocal[index-1] >= 0:
            return False
    return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()