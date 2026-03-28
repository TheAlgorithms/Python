def add(a: int, b: int) -> int:
    """
    Return sum of two integers

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    return a + b
