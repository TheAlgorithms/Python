import math


def apparent_power(real_power: float, reactive_power: float) -> float:
    """
    Calculate apparent power from real power and reactive power.

    Examples:-
    >>> calculate_apparent_power(100, 50)
    111.80339887498948
    >>> calculate_apparent_power(100, -50)
    111.80339887498948
    >>> calculate_apparent_power(0, 0)
    0.0
    """
    return math.sqrt(real_power**2 + reactive_power**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
