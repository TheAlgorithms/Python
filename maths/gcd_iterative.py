def gcd_iterative(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two numbers iteratively.

    Examples:
    >>> gcd_iterative(48, 18)
    6
    >>> gcd_iterative(7, 5)
    1
    """
    while b != 0:
        a, b = b, a % b
    return a
