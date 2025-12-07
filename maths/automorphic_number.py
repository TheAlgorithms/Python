def is_automorphic(n: int) -> bool:
    """
    Check if a number is an Automorphic Number.

    A number is automorphic if its square ends with the number itself.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is automorphic, False otherwise.

    Examples:
    >>> is_automorphic(5)
    True
    >>> is_automorphic(6)
    True
    >>> is_automorphic(76)
    True
    >>> is_automorphic(7)
    False
    >>> is_automorphic(-5)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer

    Time Complexity:
        O(d) where d is the number of digits of n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    square = n * n
    return str(square).endswith(str(n))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
