# Maclaurin series approximation of sine
from math import factorial


def maclaurin_sin(theta, accuracy=30):
    """
    Returns the maclaurin approximation of sine
    :param theta: the angle to which sin is found
    :param accuracy: the degree of accuracy wanted minimum ~ 1.5 theta
    :return: the value of sine in radians


    >>> maclaurin_sin(10)
    -0.54402111088927
    >>> maclaurin_sin(-10)
    0.54402111088927
    >>> maclaurin_sin(10, 15)
    -0.5429111519640644
    >>> maclaurin_sin(-10, 15)
    0.5429111519640644
    >>> maclaurin_sin("10")
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires an int or float value for theta and positive int for accuracy
    >>> maclaurin_sin(10, -30)
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires an int or float value for theta and positive int for accuracy
    >>> maclaurin_sin(10, 30.5)
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires an int or float value for theta and positive int for accuracy
    >>> maclaurin_sin(10, "30")
    Traceback (most recent call last):
    ...
    ValueError: maclaurin_sin() requires an int or float value for theta and positive int for accuracy
    """

    if (
        not isinstance(accuracy, int)
        or accuracy <= 0
        or type(theta) not in [int, float]
    ):
        raise ValueError(
            "maclaurin_sin() requires an int or float value for theta and positive int for accuracy"
        )

    theta = float(theta)

    _total = 0
    for r in range(accuracy):
        _total += ((-1) ** r) * ((theta ** (2 * r + 1)) / (factorial(2 * r + 1)))
    return _total


if __name__ == "__main__":
    print(maclaurin_sin(10))
    print(maclaurin_sin(-10))
    print(maclaurin_sin(10, 15))
    print(maclaurin_sin(-10, 15))
    print(maclaurin_sin("10"))
    print(maclaurin_sin(10, -30))
    print(maclaurin_sin(10, 30.5))
    print(maclaurin_sin(10, "30"))
