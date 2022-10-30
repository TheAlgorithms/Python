def calculate_resistence_in_parallel(resistors_in_parallel: list) -> float:
    """
    Calculate total resistance of resistors used in parallel
    >>> calculate_resistence_in_parallel([200, 470, 220])
    85.67
    """
    total = sum(1 / val for val in resistors_in_parallel)
    return round(1 / total, 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
