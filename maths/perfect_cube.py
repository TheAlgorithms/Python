def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(4)
    False
    >>> perfect_cube(125)
    True
    >>> perfect_cube(1024)
    False
    """
    val = n ** (1 / 3)
    return (val * val * val) == n


if __name__ == "__main__":
    print(perfect_cube(27))
    print(perfect_cube(4))
    print(perfect_cube(125))
    print(perfect_cube(1024))
