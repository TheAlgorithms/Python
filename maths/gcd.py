def gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using
    the Euclidean algorithm.

    The GCD is the largest positive integer that divides both numbers
    without leaving a remainder.

    >>> gcd(48, 18)
    6
    >>> gcd(7, 5)
    1
    >>> gcd(0, 10)
    10
    >>> gcd(10, 0)
    10

    :param a: first integer
    :param b: second integer
    :return: greatest common divisor of a and b
    """
