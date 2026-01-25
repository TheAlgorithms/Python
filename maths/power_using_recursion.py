"""
== Raise base to the power of exponent using recursion ==
    Input -->
        Enter the base: 3
        Enter the exponent: 4
    Output  -->
        3 to the power of 4 is 81
    Input -->
        Enter the base: 2
        Enter the exponent: 0
    Output -->
        2 to the power of 0 is 1
"""


def power(base: float, exponent: int) -> float:
    """
    Calculate the power of a base raised to an exponent using recursion.

    Args:
        base (int): The base number.
        exponent (int): The exponent number.

    Returns:
        the calculated value of base^exponent || base**exponent

    cases:
    >>> power(3, 4)
    81
    >>> power(2, 0)
    1
    >>> power(5, 1)
    5
    >>> power(2, -1)
    0.5
    >>> power(-2, 3)
    -8
    >>> power(-2, 2)
    4
    >>> power(0, 5)
    0
    >>> power (0,0)
    1
    """
    if not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")

    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Raise base to the power of exponent using recursion...")
    try:
        base = float(input("Enter the base: ").strip())
        exponent = int(input("Enter the exponent: ").strip())
        result = power(base, exponent)
        print(f"{base} to the power of {exponent} is {result}")
    except ValueError as e:
        print(f"Invalid input: {e} ")
    except TypeError as e:
        print(f"error: {e}")
    except RecursionError:
        print(
            """error: Maximum recursive depth exceeded.
            The exponent you might have given as input might have been very large"""
        )
