# https://en.wikipedia.org/wiki/LC_circuit

"""An LC circuit, also called a resonant circuit, tank circuit, or tuned circuit,
is an electric circuit consisting of an inductor, represented by the letter L,
and a capacitor, represented by the letter C, connected together.
The circuit can act as an electrical resonator, an electrical analogue of a
tuning fork, storing energy oscillating at the circuit's resonant frequency.
Source: https://en.wikipedia.org/wiki/LC_circuit
"""

from __future__ import annotations

from math import pi, sqrt


def resonant_frequency(inductance: float, capacitance: float) -> tuple:
    """
    This function can calculate the resonant frequency of LC circuit,
    for the given value of inductance and capacitnace.

    Examples are given below:
    >>> resonant_frequency(inductance=10, capacitance=5)
    ('Resonant frequency', 0.022507907903927652)
    >>> resonant_frequency(inductance=0, capacitance=5)
    Traceback (most recent call last):
      ...
    ValueError: Inductance cannot be 0 or negative
    >>> resonant_frequency(inductance=10, capacitance=0)
    Traceback (most recent call last):
      ...
    ValueError: Capacitance cannot be 0 or negative
    """

    if inductance <= 0:
        raise ValueError("Inductance cannot be 0 or negative")

    elif capacitance <= 0:
        raise ValueError("Capacitance cannot be 0 or negative")

    else:
        return (
            "Resonant frequency",
            float(1 / (2 * pi * (sqrt(inductance * capacitance)))),
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
