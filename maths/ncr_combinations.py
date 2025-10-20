"""
Generalized nCr (combinations) calculator for real numbers n and integer r.
Wikipedia URL: https://en.wikipedia.org/wiki/Binomial_coefficient
"""

from math import factorial as math_factorial


def nCr(n: float, r: int) -> float:
    """
    Compute the number of combinations (n choose r) for real n and integer r
    using the formula:

        nCr = n * (n-1) * (n-2) * ... * (n-r+1) / r!

    Parameters
    ----------
    n : float
        Total number of items. Can be any real number.
    r : int
        Number of items to choose. Must be a non-negative integer.

    Returns
    -------
    float
        The number of combinations.

    Raises
    ------
    ValueError
        If r is not an integer or r < 0

    Examples
    --------
    >>> nCr(5, 2)
    10.0
    >>> nCr(5.5, 2)
    12.375
    >>> nCr(10, 0)
    1.0
    >>> nCr(0, 0)
    1.0
    >>> nCr(5, -1)
    Traceback (most recent call last):
        ...
    ValueError: r must be a non-negative integer
    >>> nCr(5, 2.5)
    Traceback (most recent call last):
        ...
    ValueError: r must be a non-negative integer
    """
    if not isinstance(r, int) or r < 0:
        raise ValueError("r must be a non-negative integer")

    if r == 0:
        return 1.0

    numerator = 1.0
    for i in range(r):
        numerator *= n - i

    denominator = math_factorial(r)
    return numerator / denominator


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    n = float(input("Enter n (real number): ").strip() or 0)
    r = int(input("Enter r (integer): ").strip() or 0)
    print(f"nCr({n}, {r}) = {nCr(n, r)}")
