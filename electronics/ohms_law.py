# https://en.wikipedia.org/wiki/Ohm%27s_law
from typing import Dict


def ohms_law(voltage: float, current: float, resistance: float) -> Dict[str, float]:
    """
    Apply Ohm's Law, on any two given electrical values, which can be voltage, current,
    and resistance, and then in a Python dict return name/value pair of the zero value.

    >>> ohms_law(voltage=10, resistance=5, current=0)
    {'current': 2.0}
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
