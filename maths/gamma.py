import math

from numpy import inf
from scipy.integrate import quad


def gamma(num: float) -> float:
    """
    https://en.wikipedia.org/wiki/Gamma_function
    In mathematics, the gamma function is one commonly
    used extension of the factorial function to complex numbers.
    The gamma function is defined for all complex numbers except the non-positive
    integers
    >>> gamma(-1)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma(0)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma(9)
    40320.0
    >>> from math import gamma as math_gamma
    >>> all(.99999999 < gamma(i) / math_gamma(i) <= 1.000000001
    ...     for i in range(1, 50))
    True
    >>> gamma(-1)/math_gamma(-1) <= 1.000000001
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma(3.3) - math_gamma(3.3) <= 0.00000001
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
