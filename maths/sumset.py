"""

Calculates the SumSet of two sets of numbers (A and B)

Source:
    https://en.wikipedia.org/wiki/Sumset

"""


def sumset(A: set, B: set) -> set:
    """
    :param first set: a set of numbers
    :param second set: a set of numbers
    :return: the nth number in Sylvester's sequence

    >>> sumset({1, 2, 3}, {4, 5, 6})
    {5, 6, 7, 8, 9}

    >>> sumset({1, 2, 3}, {4, 5, 6, 7})
    {5, 6, 7, 8, 9, 10}

    >>> sumset({1, 2, 3, 4}, 3)
    Traceback (most recent call last):
    ...
    AssertionError: The input value of [B=3] is not a set
    """
    assert isinstance(A, set), f"The input value of [A={A}] is not a set"
    assert isinstance(B, set), f"The input value of [B={B}] is not a set"

    return {a + b for a in A for b in B}


if __name__ == "__main__":
    from doctest import testmod

    testmod()
