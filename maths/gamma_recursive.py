"""
Gamma function is a very useful tool in math and physics.
It helps calculating complex integral in a convenient way.
for more info: https://en.wikipedia.org/wiki/Gamma_function

Python's Standard Library math.gamma() function overflows around gamma(171.624).
"""
from math import pi, sqrt


def gamma(num: float) -> float:
    """
    Calculates the value of Gamma function of num
    where num is either an integer (1, 2, 3..) or a half-integer (0.5, 1.5, 2.5 ...).
    Implemented using recursion
    Examples:
    >>> from math import isclose, gamma as math_gamma
    >>> gamma(0.5)
    1.7724538509055159
    >>> gamma(2)
    1.0
    >>> gamma(3.5)
    3.3233509704478426
    >>> gamma(171.5)
    9.483367566824795e+307
    >>> all(isclose(gamma(num), math_gamma(num)) for num in (0.5, 2, 3.5, 171.5))
    True
    >>> gamma(0)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma(-1.1)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma(-4)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> gamma(172)
    Traceback (most recent call last):
        ...
    OverflowError: math range error
    >>> gamma(1.1)
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
        return sqrt(pi)
    else:
        return 1.0 if num == 1 else (num - 1) * gamma(num - 1)


def test_gamma() -> None:
    """
    >>> test_gamma()
    """
    assert gamma(0.5) == sqrt(pi)
    assert gamma(1) == 1.0
    assert gamma(2) == 1.0


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    num = 1
    while num:
        num = float(input("Gamma of: "))
        print(f"gamma({num}) = {gamma(num)}")
        print("\nEnter 0 to exit...")
