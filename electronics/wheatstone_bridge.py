# https://en.wikipedia.org/wiki/Wheatstone_bridge
from __future__ import annotations


def wheatstone_solver(
    resistance_1: float, resistance_2: float, resistance_3: float
) -> float:
    """
    Calculate the unknown resistance (Rx) in a Wheatstone bridge circuit.

    A Wheatstone bridge is an electrical circuit used to precisely measure 
    an unknown resistance. This function calculates Rx when the three other 
    resistances in the bridge are known.

    Circuit Diagram:
    
         R1         R2
      +--/\/\/--+--/\/\/--+
      |         |         |
     Vin       Vg        Vout
      |         |         |
      +--/\/\/--+--/\/\/--+
         R3        Rx
    
    This solver uses the balanced bridge formula:
    Rx = (R2/R1) × R3
    
    Args:
        resistance_1 (R1): First known resistance
        resistance_2 (R2): Second known resistance
        resistance_3 (R3): Third known resistance
    
    Returns:
        float: The calculated unknown resistance (Rx)

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
