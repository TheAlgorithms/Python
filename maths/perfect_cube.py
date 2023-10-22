def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(4)
    False
    >>> perfect_cube(2)
    False
    >>> perfect_cube(0)
    True
    >>> perfect_cube(1)
    True
    >>> perfect_cube(-27)
    True
    >>> perfect_cube(-4)
    False
    >>> perfect_cube(-2)
    False

    """
    if n == 0:
        return True
    val = abs(n) ** (1 / 3)
    return abs(round(val) ** 3) == abs(n)


if __name__ == "__main__":
    print(perfect_cube(27))
    print(perfect_cube(4))
    print(perfect_cube(2))
    print(perfect_cube(0))
    print(perfect_cube(1))
    print(perfect_cube(-27))
    print(perfect_cube(-4))
    print(perfect_cube(-2))
