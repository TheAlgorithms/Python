def nth_sgonal_num(n: int, s: int) -> int:
    """
    Returns the `n`th `s`-gonal number. It is assumed that `n` >= 0 and `s` >= 3
    (see for reference https://en.wikipedia.org/wiki/Polygonal_number).

    >>> nth_sgonal_num(0, 3)
    0
    >>> nth_sgonal_num(3, 3)
    6
    >>> nth_sgonal_num(5, 4)
    25
    >>> nth_sgonal_num(2, 5)
    5
    """
    return ((s - 2) * (n**2) - (s - 4) * n) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
