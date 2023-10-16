"""
Description :
Calculate one of the parameters (current, voltage, or resistance) in an electrical circuit based on Ohm's law.
Ohm's law(Ω) states that the current through a conductor between two points is directly proportional to the voltage across the two points.
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
def ohms_law(voltage=None, current=None, resistance=None) -> float:
    """
    Example Usages:
    ohms_law(current=2, resistance=4)
    # Output: {'voltage': 8.0}

    ohms_law(voltage=12, current=3)
    # Output: {'resistance': 4.0}

    ohms_law(voltage=9, resistance=3)
    # Output: {'current': 3.0}

    Note:
    - Only two out of the three parameters should be provided.
    - Negative values for current, voltage, and resistance are not allowed.
    - Providing all three parameters will raise an error.
    """
    # Check that exactly two parameters are provided
    if sum(param is not None for param in [current, voltage, resistance]) != 2:
        raise ValueError(
            "Exactly two parameters (current, voltage, or resistance) must be provided."
        )

    # Check for negative values
    if current is not None and current < 0:
        raise ValueError("Current cannot be negative.")
    if voltage is not None and voltage < 0:
        raise ValueError("Voltage cannot be negative.")
    if resistance is not None and resistance < 0:
        raise ValueError("Resistance cannot be negative.")

    # Calculate the missing parameter
    if current is None:
        current = voltage / resistance
        return {"current": current}
    elif voltage is None:
        voltage = current * resistance
        return {"voltage": voltage}
    elif resistance is None:
        resistance = voltage / current
        return {'resistance': resistance}

#Run Doctest
if __name__ == "__main__":
    import doctest

    doctest.testmod()
