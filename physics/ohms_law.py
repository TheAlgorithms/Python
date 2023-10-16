"""
Description :
Calculate one of the parameters (current, voltage, or resistance)
in an electrical circuit based on Ohm's law.
Ohm's law(Ω) states that the current through a
conductor between two points is directly
proportional to the voltage across the two points.
V is proportional to I.
V = I*R (where R is a proportionality constant)

    Input Parameters:
    - current: Current in Amperes (A)
    - voltage: Voltage in Volts (V)
    - resistance: Resistance in Ohms (Ω)

    Returns:
    A dictionary with the calculated parameter and its value.
Source :
- https://byjus.com/physics/ohms-law/
"""

from typing import Union


def ohms_law(
    voltage: float = None, current: float = None, resistance: float = None
) -> Union[float, None]:
    """
    Calculate one of the parameters (voltage, current, or resistance) in an electrical circuit
    based on Ohm's law.

    Input Parameters:
    - voltage: Voltage in Volts (V)
    - current: Current in Amperes (A)
    - resistance: Resistance in Ohms (Ω)

    Returns:
    The calculated parameter (voltage, current, or resistance) as a float.
    Returns None if all parameters are None.

    Example Usages:
    ohms_law(voltage=12, current=3)
    # Output: 4.0

    ohms_law(current=2, resistance=4)
    # Output: 8.0

    ohms_law(voltage=9, resistance=3)
    # Output: 3.0

    Note:
    - Only two out of the three parameters should be provided.
    - Negative values for current, voltage, and resistance are not allowed.
    - Providing all three parameters will return None.
    """
    # Check that exactly two parameters are provided
    if sum(param is not None for param in [voltage, current, resistance]) != 2:
        raise ValueError("Exactly two parameters (voltage, current, or resistance) must be provided.")

    # Check for negative values
    if current is not None and current < 0:
        raise ValueError("Current cannot be negative.")
    if voltage is not None and voltage < 0:
        raise ValueError("Voltage cannot be negative.")
    if resistance is not None and resistance < 0:
        raise ValueError("Resistance cannot be negative.")

    # Calculate the missing parameter
    if current is None:
        return voltage / resistance
    elif voltage is None:
        return current * resistance
    elif resistance is None:
        return voltage / current
    else:
        # All parameters are None, return None
        return None
# Run Doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
