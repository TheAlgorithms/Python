import math

from numpy import inf
from scipy.integrate import quad


def gamma_iterative(num: float) -> float:
    """
    https://en.wikipedia.org/wiki/Gamma_function
    In mathematics, the gamma_iterative function is one commonly
    used extension of the factorial function to complex numbers.
    The gamma_iterative function is defined for all complex numbers except the non-positive
    integers
    >>> gamma_iterative(-1)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma_iterative(0)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma_iterative(9)
    40320.0
    >>> from math import gamma as math_gamma
    >>> all(.99999999 < gamma_iterative(i) / math_gamma(i) <= 1.000000001
    ...     for i in range(1, 50))
    True
    >>> gamma_iterative(-1)/math_gamma(-1) <= 1.000000001
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma_iterative(3.3) - math_gamma(3.3) <= 0.00000001
    True
    """
    if num <= 0:
        raise ValueError("math domain error")

    return quad(integrand, 0, inf, args=(num))[0]


def integrand(x: float, z: float) -> float:
    return math.pow(x, z - 1) * math.exp(-x)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
