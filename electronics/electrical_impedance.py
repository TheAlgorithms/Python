"""Electrical impedance is the measure of the opposition that a
circuit presents to a current when a voltage is applied.
Impedance extends the concept of resistance to alternating current (AC) circuits.
Source: https://en.wikipedia.org/wiki/Electrical_impedance
"""

from __future__ import annotations

from math import pow, sqrt


def electrical_impedance(
    resistance: float, reactance: float, impedance: float
) -> dict[str, float]:
    """
    Apply Electrical Impedance formula, on any two given electrical values,
    which can be resistance, reactance, and impedance, and then in a Python dict
    return name/value pair of the zero value.

    >>> electrical_impedance(3,4,0)
    {'impedance': 5.0}
    >>> electrical_impedance(0,4,5)
    {'resistance': 3.0}
    >>> electrical_impedance(3,0,5)
    {'reactance': 4.0}
    >>> electrical_impedance(3,4,5)
    Traceback (most recent call last):
      ...
    ValueError: One and only one argument must be 0
    """
    if (resistance, reactance, impedance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if resistance == 0:
        return {"resistance": sqrt(pow(impedance, 2) - pow(reactance, 2))}
    elif reactance == 0:
        return {"reactance": sqrt(pow(impedance, 2) - pow(resistance, 2))}
    elif impedance == 0:
        return {"impedance": sqrt(pow(resistance, 2) + pow(reactance, 2))}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
