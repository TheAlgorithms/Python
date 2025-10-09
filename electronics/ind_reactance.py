# https://en.wikipedia.org/wiki/Electrical_reactance#Inductive_reactance
from __future__ import annotations

from math import pi


def ind_reactance(
    inductance: float, frequency: float, reactance: float
) -> dict[str, float]:
    """
    Calculate inductive reactance, frequency or inductance from two given electrical
    properties then return name/value pair of the zero value in a Python dict.

    Parameters
    ----------
    inductance : float with units in Henries

    frequency : float with units in Hertz

    reactance : float with units in Ohms

    >>> ind_reactance(-35e-6, 1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Inductance cannot be negative

    >>> ind_reactance(35e-6, -1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Frequency cannot be negative

    >>> ind_reactance(35e-6, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Inductive reactance cannot be negative

    >>> ind_reactance(0, 10e3, 50)
    {'inductance': 0.0007957747154594767}

    >>> ind_reactance(35e-3, 0, 50)
    {'frequency': 227.36420441699332}

    >>> ind_reactance(35e-6, 1e3, 0)
    {'reactance': 0.2199114857512855}

    """

    if (inductance, frequency, reactance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if inductance < 0:
        raise ValueError("Inductance cannot be negative")
    if frequency < 0:
        raise ValueError("Frequency cannot be negative")
    if reactance < 0:
        raise ValueError("Inductive reactance cannot be negative")
    if inductance == 0:
        return {"inductance": reactance / (2 * pi * frequency)}
    elif frequency == 0:
        return {"frequency": reactance / (2 * pi * inductance)}
    elif reactance == 0:
        return {"reactance": 2 * pi * frequency * inductance}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
