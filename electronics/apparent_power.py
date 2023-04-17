import math


def apparent_power(real_power: float, reactive_power: float) -> float:
    """
    Calculate apparent power from real power and reactive power.

    Args:
        real_power (float): Real power in watts.
        reactive_power (float): Reactive power in vars.

    Returns:
        float: Apparent power in volt-amperes (VA).

    Examples:-
    >>> calculate_apparent_power(100, 50)
    111.80339887498948
    >>> calculate_apparent_power(100, -50)
    111.80339887498948
    >>> calculate_apparent_power(0, 0)
    0.0
    """
    apparent_power = math.sqrt(real_power**2 + reactive_power**2)
    return apparent_power


if __name__ == "__main__":
    import doctest

    doctest.testmod()
