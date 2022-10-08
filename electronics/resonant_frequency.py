# https://en.wikipedia.org/wiki/LC_circuit

from __future__ import annotations
from math import sqrt
from math import pi

def resonant_frequency(inductance: float, capacitance: float) -> tuple:

    """
    This function can calculate the resonant frequency of LC circuit,
    for the given value of inductance and capacitnace.

    Examples are given below:
    >>> resonant_frequency(inductance=0, capacitance=5)
    ValueError: Inductance cannot be 0 or negative
    >>> resonant_frequency(inductance=10, capacitance=0)
    ValueError: Capacitance cannot be 0 or negative
    >>> resonant_frequency(inductance=10, capacitance=5)
    0.022507907903927652
    """

    if inductance<=0:
        raise ValueError("Inductance cannot be 0 or negative")

    elif capacitance<=0:
        raise ValueError("Capacitance cannot be 0 or negative")

    else:
        return(float(1/(2*pi*(sqrt(inductance*capacitance)))))

if __name__ == "__main__":
    import doctest

    doctest.testmod()


