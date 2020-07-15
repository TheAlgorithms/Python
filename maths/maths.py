"""
package maths.py reimplements some trigonometric algorithms from math.py
"""

from math import pi


def _abs(value):
    """
    >>> _abs(-10)
    10
    >>> _abs(10)
    10
    >>> all(_abs(i) == abs(i) for i in range(-100, 100))  # test ints
    True
    >>> all(_abs(i / 10) == abs(i / 10) for i in range(-100, 100))  # test floats
    True
    """
    return -value if value < 0 else value


def _power(value, n):
    """
    >>> _power(-10, 2)
    100
    >>> _power(10, 2)
    100

    >>> all(_power(v, n) == v ** n for v in range(-100, 100) for n in range(-100, 100))
    True
    """
    result = 1

    if n == 0:
        result = 1
    else:
        for i in range(n):
            result *= value

    return result


def _sqrt(value):
    """
    newton iteration method:
    X(k+1) = 1/2 * (X(k) + vale/X(k))

    >>> _sqrt(9)
    3.0
    >>> _sqrt(25)
    5.0
    >>> from math import isclose, sqrt
    >>> all(isclose(_sqrt(i), sqrt(i)) for i in range(100))
    True
    """
    if value < 0:
        raise ValueError("Error: Value must be greater than or equal to 0")
    else:
        x = value
        t = 0
        while _abs(x - t) > 1e-15:
            t = x
            x = 0.5 * (x + (value / x))

    return x


# factorial
def _factor(value):
    """
    regulations 0! = 1

    >>> _factor(5)
    120
    >>> _factor(2)
    2
    """
    f = 1
    if value:
        for i in range(value):
            f = f * (i + 1)
    else:
        f = 1

    return f


# Another way to implement sin(x)
def __sin(value):
    """
    >>> __sin(90)
    1.0
    >>> __sin(0)
    0
    >>> from math import isclose, sin
    >>> all(isclose(__sin(i), sin(i), rel_tol=1e-07) for i in range(-720, 720))
    True
    """
    value *= pi / 180
    t = value
    x = 0
    n = 1

    while _abs(t) > 1e-15:
        x = x + t
        n = n + 1
        t = -t * value * value / (2 * n - 1) / (2 * n - 2)

    if x > 0 and x < 1e-15:
        x = 0

    return x


def _sin(value):
    """
    >>> _sin(90)
    1.0
    >>> _sin(0)
    0
    >>> from math import isclose, sin
    >>> all(isclose(_sin(i), sin(i), rel_tol=1e-07) for i in range(-720, 720))
    True
    """
    value *= pi / 180
    t = 1
    x = 0
    n = 1

    while _power(value, n) / _factor(n) > 1e-15:
        x += t * _power(value, n) / _factor(n)
        t *= -1
        n = n + 2

    return x


def _cos(value):
    """
    >>> _cos(90)
    6.428707379885143e-17
    >>> _cos(0)
    1.0
    >>> from math import isclose, cos
    >>> all(isclose(_cos(i), cos(i), rel_tol=1e-07) for i in range(-720, 720))
    True
    """
    value *= pi / 180
    n = 0
    t = 1
    x = 0

    while _power(value, n) / _factor(n) > 1e-15:
        x += t * _power(value, n) / _factor(n)
        t = -1 * t
        n = n + 2

    return x


def _tan(value):
    """
    >>> _tan(0)
    0.0
    >>> _tan(45)
    1.0
    >>> from math import isclose, tan
    >>> all(isclose(_tan(i), tan(i), rel_tol=1e-07) for i in range(-720, 720))
    True
    """
    return _sin(value) / _cos(value)
