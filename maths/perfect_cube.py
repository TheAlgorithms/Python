def perfect_cube(n: int) -> bool:
    """
      Check if a number is a perfect cube or not.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(4)
    False
    >>> perfect_cube(8)
    False
    >>> perfect_cube(125)
    True
    >>> perfect_cube(64)
    True
    >>> perfect_cube(0)
    True
    >>> perfect_cube(1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer
    >>> perfect_cube(3.375)
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer
    >>> perfect_cube("64")
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer
    >>> perfect_cube([27])
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer
    """
    val = n ** (1 / 3)
    return (val * val * val) == n


if __name__ == "__main__":
    print(perfect_cube(27))
    print(perfect_cube(4))
