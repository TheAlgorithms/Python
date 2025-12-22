# https://en.wikipedia.org/wiki/Wheatstone_bridge
from __future__ import annotations


def wheatstone_solver(
    resistance_1: float, resistance_2: float, resistance_3: float
) -> float:
    """
     Wheatstone Bridge is an electrical circuit used to accurately measure
    an unknown resistance by balancing two legs of a bridge circuit.

    The bridge is said to be balanced when no current flows 
    through the galvanometer connected between the midpoints 
     of the two voltage dividers.
      Balance condition:
       R1 / R2 = R3 / R4

      Applications:
      - Measurement of unknown resistance
      - Strain gauge circuits
      - Sensor calibration
    This function can calculate the unknown resistance in an wheatstone
    network, given that the three other resistances 
    in the network are known.

    Usage examples:
    >>> wheatstone_solver(resistance_1=2, resistance_2=4, resistance_3=5)
    10.0
    >>> wheatstone_solver(resistance_1=356, resistance_2=234, resistance_3=976)
    641.5280898876405
    >>> wheatstone_solver(resistance_1=2, resistance_2=-1, resistance_3=2)
    Traceback (most recent call last):
        ...
    ValueError: All resistance values must be positive
    >>> wheatstone_solver(resistance_1=0, resistance_2=0, resistance_3=2)
    Traceback (most recent call last):
        ...
    ValueError: All resistance values must be positive
    """

    if resistance_1 <= 0 or resistance_2 <= 0 or resistance_3 <= 0:
        raise ValueError("All resistance values must be positive")
    else:
        return float((resistance_2 / resistance_1) * resistance_3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
