def commutative_law_and(a, b):
    """
    Implement the commutative law for AND: A AND B = B AND A.

    Parameters:
    a (bool): The first boolean value.
    b (bool): The second boolean value.

    Returns:
    bool: Result of A AND B.

    >>> commutative_law_and(True, False)
    False
    >>> commutative_law_and(False, True)
    False
    >>> commutative_law_and(True, True)
    True
    >>> commutative_law_and(False, False)
    False
    """
    return a and b


def commutative_law_or(a, b):
    """
    Implement the commutative law for OR: A OR B = B OR A.

    Parameters:
    a (bool): The first boolean value.
    b (bool): The second boolean value.

    Returns:
    bool: Result of A OR B.

    >>> commutative_law_or(True, False)
    True
    >>> commutative_law_or(False, True)
    True
    >>> commutative_law_or(True, True)
    True
    >>> commutative_law_or(False, False)
    False
    """
    return a or b


# Implement other laws similarly

if __name__ == "__main__":
    import doctest

    doctest.testmod()
