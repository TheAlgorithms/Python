def array_complement(initial_lst: list, diff_lst: list) -> list:
    """
    removes all values from list initial_lst which
    are also present in list diff_lst [ while keeping
    the initial order of the elements ]

    https://en.wikipedia.org/wiki/Complement_(set_theory)

    >>> array_complement([1, 6, 2, 8], [1, 4])
    [6, 2, 8]
    >>> array_complement([146], [146, 25])
    []
    >>> array_complement([35], [36])
    [35]
    
    
    """

    return [c for c in initial_lst if c not in diff_lst]


if __name__ == "__main__":
    __import__("doctest").testmod()
