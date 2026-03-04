"""Sign Function."""


def sign(num: int | float) -> int:
    """
    Return the sign of a number: -1 for negative, 0 for zero, 1 for positive.

    >>> sign(-5)
    -1
    >>> sign(0)
    0
    >>> sign(10)
    1
    >>> sign(-0.5)
    -1
    """
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0


def test_sign():
    """
    >>> test_sign()
    """
    assert sign(-5) == -1
    assert sign(0) == 0
    assert sign(10) == 1
    assert sign(-0.001) == -1
    assert sign(0.001) == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_sign()
    print(sign(-5))  # --> -1
