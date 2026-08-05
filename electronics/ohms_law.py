# https://en.wikipedia.org/wiki/Ohm%27s_law
from __future__ import annotations


def ohms_law(voltage: float, current: float, resistance: float) -> dict[str, float]:
    """
    Apply Ohm's Law to calculate the missing electrical value.

    Ohm's Law: V = I × R, where V=voltage, I=current, R=resistance

    Args:
        voltage: Electrical potential difference in volts (0 if unknown)
        current: Electrical current in amperes (0 if unknown)
        resistance: Electrical resistance in ohms (0 if unknown)

    Returns:
        Dictionary with the calculated value: {'voltage': V}, {'current': I}, or {'resistance': R}

    Raises:
        ValueError: If not exactly one value is 0, or if resistance is negative

    Examples:
        >>> ohms_law(voltage=10, resistance=5, current=0)
        {'current': 2.0}
        >>> ohms_law(voltage=0, current=2, resistance=5)
        {'voltage': 10.0}
        >>> ohms_law(voltage=10, current=2, resistance=0)
        {'resistance': 5.0}
        >>> ohms_law(voltage=0, current=0, resistance=10)
        Traceback (most recent call last):
          ...
        ValueError: One and only one argument must be 0
        >>> ohms_law(voltage=0, current=1, resistance=-2)
        Traceback (most recent call last):
          ...
        ValueError: Resistance cannot be negative
        >>> ohms_law(resistance=0, voltage=-10, current=1)
        {'resistance': -10.0}
        >>> ohms_law(voltage=0, current=-1.5, resistance=2)
        {'voltage': -3.0}
        >>> ohms_law(voltage=12, current=3, resistance=0)
        {'resistance': 4.0}
        >>> ohms_law(voltage=-9, current=3, resistance=0)
        {'resistance': -3.0}
        >>> ohms_law(voltage=0, current=2.5, resistance=4)
        {'voltage': 10.0}
        >>> ohms_law(voltage=7.5, current=0, resistance=3)
        {'current': 2.5}
    """
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if resistance < 0:
        raise ValueError("Resistance cannot be negative")
    if voltage == 0:
        return {"voltage": float(current * resistance)}
    elif current == 0:
        return {"current": voltage / resistance}
    elif resistance == 0:
        return {"resistance": voltage / current}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
