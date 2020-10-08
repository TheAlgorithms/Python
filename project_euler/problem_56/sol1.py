def solution(a: int, b: int) -> int:
    """
    Considering natural numbers of the form, a**b, where a, b < 100,
    what is the maximum digital sum?
    :param a:
    :param b:
    :return:
    >>> solution(10,10)
    45

    >>> solution(100,100)
    972

    >>> solution(100,200)
    1872
    """

    # RETURN the MAXIMUM from the list of SUMs of the list of INT converted from STR of
    # BASE raised to the POWER
    return max(
        [
            sum([int(x) for x in str(base ** power)])
            for base in range(a)
            for power in range(b)
        ]
    )


# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
