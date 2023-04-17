import math

def calculate_real_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate real power from apparent power and power factor.

    Args:
        apparent_power (float): Apparent power in volt-amperes (VA).
        power_factor (float): Power factor (cosine of the phase angle).

    Returns:
        float: Real power in watts.

    Examples:
    >>> calculate_real_power(100, 0.9)
    90.0
    >>> calculate_real_power(0, 0.8)
    0.0
    >>> calculate_real_power(100, -0.9)
    -90.0
    >>> calculate_real_power(100, 1.2)
    Traceback (most recent call last):
    ...
    ValueError: power_factor must be a valid float value between -1 and 1.
    """
    if not isinstance(power_factor, (int, float)) or power_factor < -1 or power_factor > 1:
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    real_power = apparent_power * power_factor
    return real_power


def calculate_reactive_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate reactive power from apparent power and power factor.

    Args:
        apparent_power (float): Apparent power in volt-amperes (VA).
        power_factor (float): Power factor (cosine of the phase angle).

    Returns:
        float: Reactive power in vars.

    Examples:
    >>> calculate_reactive_power(100, 0.9)
    43.58898943540674
    >>> calculate_reactive_power(0, 0.8)
    0.0
    >>> calculate_reactive_power(100, -0.9)
    -43.58898943540674
    >>> calculate_reactive_power(100, 1.2)
    Traceback (most recent call last):
    ...
    ValueError: power_factor must be a valid float value between -1 and 1.
    """
    if not isinstance(power_factor, (int, float)) or power_factor < -1 or power_factor > 1:
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    reactive_power = apparent_power * math.sqrt(1 - power_factor ** 2)
    return reactive_power


if __name__ == "__main__":
    import doctest

    doctest.testmod()
