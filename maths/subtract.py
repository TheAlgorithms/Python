def subtract(a: float, b: float) -> float:
    """
    >>> subtract(2, 2)
    0
    >>> subtract(2, -2)
    4
    """
    return a - b


if __name__ == "__main__":
    import doctest

    a = 10
    b = 4
    print(f"The sum of {a} + {b} is {subtract(a, b)}")

    doctest.testmod()
