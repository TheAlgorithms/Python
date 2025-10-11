def reverse_factorial(n: int, divisor: int = 1) -> int:
    """
    Return x such that x! equals the given n, or -1 if no such integer exists.

    This function recursively divides the number `n` by successive integers 
    starting from 1 until it reaches 1. If the division completes exactly at 1,
    the last divisor - 1 is the factorial root. Otherwise, return -1.

    Parameters
    ----------
    n : int
        The number whose factorial root is to be found.
    divisor : int, optional
        The current divisor used in the recursion (default is 1).

    Returns
    -------
    int
        The factorial root if it exists, otherwise -1.

    Examples
    --------
    >>> reverse_factorial(120)
    5
    >>> reverse_factorial(24)
    4
    >>> reverse_factorial(150)
    -1
    >>> reverse_factorial(1)
    1
    >>> reverse_factorial(720)
    6
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return divisor
    if n % divisor != 0:
        return -1
    return reverse_factorial(n // divisor, divisor + 1)
