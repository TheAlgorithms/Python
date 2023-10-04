"""

Calculates the SumSet of two sets of numbers (A and B)

Source:
    https://en.wikipedia.org/wiki/Sumset

"""


def sumset(set_a: set, set_b: set) -> set:
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
    AssertionError: The input value of [set_b=3] is not a set
    """
    assert isinstance(set_a, set), f"The input value of [set_a={set_a}] is not a set"
    assert isinstance(set_b, set), f"The input value of [set_b={set_b}] is not a set"

    return {a + b for a in set_a for b in set_b}


if __name__ == "__main__":
    from doctest import testmod

    testmod()
