def commutative_law_and(a: bool, b: bool) -> bool:
    """
    Implement the commutative law for AND: A AND B = B AND A.

    Parameters:
    a (bool): The first boolean operand.
    b (bool): The second boolean operand.

    Returns:
    bool: Result of the commutative law (A AND B).

    Examples:
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

def commutative_law_or(a: bool, b: bool) -> bool:
    """
    Implement the commutative law for OR: A OR B = B OR A.

    Parameters:
    a (bool): The first boolean operand.
    b (bool): The second boolean operand.

    Returns:
    bool: Result of the commutative law (A OR B).

    Examples:
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
