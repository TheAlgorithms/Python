def nth_sgonal_num(num: int, sides: int) -> int:
    """
    Returns the `num`th `sides`-gonal number. It is assumed that `num` >= 0 and
    `sides` >= 3 (see for reference https://en.wikipedia.org/wiki/Polygonal_number).

    >>> nth_sgonal_num(0, 3)
    0
    >>> nth_sgonal_num(3, 3)
    6
    >>> nth_sgonal_num(5, 4)
    25
    >>> nth_sgonal_num(2, 5)
    5
    """
    if num < 0 or sides < 3:
        raise ValueError("Invalid input: num must be >= 0 and sides must be >= 3.")

    return ((sides - 2) * (num**2) - (sides - 4) * num) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
