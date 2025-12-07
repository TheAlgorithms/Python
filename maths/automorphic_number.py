def is_automorphic(n: int) -> bool:
    """
    Check if a number is an Automorphic Number.
    A number is automorphic if its square ends with the number itself.

    Examples:
    >>> is_automorphic(5)
    True
    >>> is_automorphic(6)
    True
    >>> is_automorphic(76)
    True
    >>> is_automorphic(7)
    False

    Time Complexity: O(d) where d is number of digits
    """
    square = n * n
    return str(square).endswith(str(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
