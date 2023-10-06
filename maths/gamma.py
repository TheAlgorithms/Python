"""
Gamma function is a very useful tool in math and physics.
It helps calculating complex integral in a convenient way.
for more info: https://en.wikipedia.org/wiki/Gamma_function
In mathematics, the gamma function is one commonly
used extension of the factorial function to complex numbers.
The gamma function is defined for all complex numbers except
the non-positive integers
Python's Standard Library math.gamma() function overflows around gamma(171.624).
"""
import math

from numpy import inf
from scipy.integrate import quad


def gamma_iterative(num: float) -> float:
    """
    Calculates the value of Gamma function of num
    where num is either an integer (1, 2, 3..) or a half-integer (0.5, 1.5, 2.5 ...).

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


def gamma_recursive(num: float) -> float:
    """
    Calculates the value of Gamma function of num
    where num is either an integer (1, 2, 3..) or a half-integer (0.5, 1.5, 2.5 ...).
    Implemented using recursion
    Examples:
    >>> from math import isclose, gamma as math_gamma
    >>> gamma_recursive(0.5)
    1.7724538509055159
    >>> gamma_recursive(1)
    1.0
    >>> gamma_recursive(2)
    1.0
    >>> gamma_recursive(3.5)
    3.3233509704478426
    >>> gamma_recursive(171.5)
    9.483367566824795e+307
    >>> all(isclose(gamma_recursive(num), math_gamma(num))
    ...     for num in (0.5, 2, 3.5, 171.5))
    True
    >>> gamma_recursive(0)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma_recursive(-1.1)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma_recursive(-4)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma_recursive(172)
    Traceback (most recent call last):
        ...
    OverflowError: math range error
    >>> gamma_recursive(1.1)
    Traceback (most recent call last):
        ...
    NotImplementedError: num must be an integer or a half-integer
    """
    if num <= 0:
        raise ValueError("math domain error")
    if num > 171.5:
        raise OverflowError("math range error")
    elif num - int(num) not in (0, 0.5):
        raise NotImplementedError("num must be an integer or a half-integer")
    elif num == 0.5:
        return math.sqrt(math.pi)
    else:
        return 1.0 if num == 1 else (num - 1) * gamma_recursive(num - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    num = 1.0
    while num:
        num = float(input("Gamma of: "))
        print(f"gamma_iterative({num}) = {gamma_iterative(num)}")
        print(f"gamma_recursive({num}) = {gamma_recursive(num)}")
        print("\nEnter 0 to exit...")
