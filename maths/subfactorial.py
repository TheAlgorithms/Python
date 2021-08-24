def subfactorial(n: int) -> int:
    """
    Returns the number of derangements of n elements aka the subfactorial of n (!n).
    A derangement is a permutation that maps no element to itself. More detailed
    information can be found at https://en.wikipedia.org/wiki/Derangement

    Time complexity: O(n)

    >>> subfactorial(2)
    1
    >>> subfactorial(5)
    44
    """

    if n < 0:
        raise Exception(
            "The subfactorial function is defined only for non-negative integers"
        )

    s0 = 1
    s1 = 0
    for i in range(1, n + 1):
        t = i * (s0 + s1)
        s0 = s1
        s1 = t
    return s0


if __name__ == "__main__":
    from doctest import testmod

    testmod()
