def array_complement(a: list, b: list) -> list:
    """
    removes all values from list a which
    are also present in list b [ while keeping
    the initial order of the elements ]

    https://en.wikipedia.org/wiki/Complement_(set_theory)

    >>> array_complement([1, 6, 2, 8], [1, 4])
    [6, 2, 8]
    >>> array_complement([146], [146, 25])
    []
    >>> array_complement([35], [36])
    [35]
    """

    return [c for c in a if c not in b]

if __name__ == "__main__":
    __import__("doctest").testmod()