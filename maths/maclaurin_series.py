"""
https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
"""

from math import factorial, pi


def maclaurin_sin(theta: float, accuracy: int = 30) -> float:
    """
    Finds the maclaurin approximation of sin

    :param theta: the angle to which sin is found
    :param accuracy: the degree of accuracy wanted minimum
    :return: the value of sine in radians


    >>> from math import isclose, sin
    >>> all(isclose(maclaurin_sin(x, 50), sin(x)) for x in range(-25, 25))
    True
    >>> maclaurin_sin(10)
    -0.5440211108893691
    >>> maclaurin_sin(-10)
    0.5440211108893704
    >>> maclaurin_sin(10, 15)
    -0.544021110889369
    >>> maclaurin_sin(-10, 15)
    0.5440211108893704
    >>> maclaurin_sin("10")
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_sin() requires either an int or float for theta
    >>> maclaurin_sin(10, -30)
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_sin() requires a positive int for accuracy
    >>> maclaurin_sin(10, 30.5)
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_sin() requires a positive int for accuracy
    >>> maclaurin_sin(10, "30")
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_sin() requires a positive int for accuracy
    """

    if not isinstance(theta, (int, float)):
        raise ValueError("maclaurin_sin() requires either an int or float for theta")

    if not isinstance(accuracy, int) or accuracy <= 0:
        raise ValueError("maclaurin_sin() requires a positive int for accuracy")

    theta = float(theta)
    div = theta // (2 * pi)
    theta -= 2 * div * pi
    return sum(
        (-1) ** r * theta ** (2 * r + 1) / factorial(2 * r + 1) for r in range(accuracy)
    )


def maclaurin_cos(theta: float, accuracy: int = 30) -> float:
    """
    Finds the maclaurin approximation of cos

    :param theta: the angle to which cos is found
    :param accuracy: the degree of accuracy wanted
    :return: the value of cosine in radians


    >>> from math import isclose, cos
    >>> all(isclose(maclaurin_cos(x, 50), cos(x)) for x in range(-25, 25))
    True
    >>> maclaurin_cos(5)
    0.2836621854632268
    >>> maclaurin_cos(-5)
    0.2836621854632265
    >>> maclaurin_cos(10, 15)
    -0.8390715290764524
    >>> maclaurin_cos(-10, 15)
    -0.8390715290764521
    >>> maclaurin_cos("10")
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_cos() requires either an int or float for theta
    >>> maclaurin_cos(10, -30)
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_cos() requires a positive int for accuracy
    >>> maclaurin_cos(10, 30.5)
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_cos() requires a positive int for accuracy
    >>> maclaurin_cos(10, "30")
    Traceback (most recent call last):
        ...
    ValueError: maclaurin_cos() requires a positive int for accuracy
    """

    if not isinstance(theta, (int, float)):
        raise ValueError("maclaurin_cos() requires either an int or float for theta")

    if not isinstance(accuracy, int) or accuracy <= 0:
        raise ValueError("maclaurin_cos() requires a positive int for accuracy")

    theta = float(theta)
    div = theta // (2 * pi)
    theta -= 2 * div * pi
    return sum((-1) ** r * theta ** (2 * r) / factorial(2 * r) for r in range(accuracy))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(maclaurin_sin(10))
    print(maclaurin_sin(-10))
    print(maclaurin_sin(10, 15))
    print(maclaurin_sin(-10, 15))

    print(maclaurin_cos(5))
    print(maclaurin_cos(-5))
    print(maclaurin_cos(10, 15))
    print(maclaurin_cos(-10, 15))
