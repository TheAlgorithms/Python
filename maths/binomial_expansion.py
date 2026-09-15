from maths.binomial_coefficient import binomial_coefficient


def binomial_expansion(a: float, b: float, n: int) -> int | float:
    """
    Compute the value of (a + b)^n using the Binomial Theorem.

    This function works for both positive and negative integer exponents.
    It raises a ZeroDivisionError if the base (a + b) is 0 and n is negative.

    Args:
        a: First term (int or float).
        b: Second term (int or float).
        n: Exponent (must be integer).

    Returns:
        The result of the binomial expansion (a + b)^n.

    Raises:
        ZeroDivisionError: If a + b == 0 and n < 0.

    See Also:
        https://en.wikipedia.org/wiki/Binomial_theorem

    Examples:
        >>> binomial_expansion(2, 3, 2)
        25
        >>> binomial_expansion(100, -4, 3)
        884736
        >>> binomial_expansion(2, 2, -2)
        0.0625
        >>> binomial_expansion(0, 0, 3)
        0
        >>> binomial_expansion(-2, 2, -1)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Cannot raise 0 to the negative power
    """
    total = a + b
    if total == 0 and n < 0:
        raise ZeroDivisionError("Cannot raise 0 to the negative power")

    abs_n = abs(n)
    value = sum(
        binomial_coefficient(abs_n, i) * (a ** (abs_n - i)) * (b**i)
        for i in range(abs_n + 1)
    )

    return value if n >= 0 else 1 / value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
