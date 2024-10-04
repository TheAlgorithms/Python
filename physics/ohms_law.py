def ohms_law(current: float, resistance: float) -> float:
    """
    Calculate the voltage when current and resistance data is given using Ohm's Law.

    Ohm's Law states that:
    V = I * R

    V = Voltage (Volts)
    I = Current (Amperes)
    R = Resistance (Ohms)

    >>> ohms_law(2,5)
    10.0

    >>> ohms_law(1,4)
    4.0

    >>> ohms_law(3,0.5)
    1.5

    >>> ohms_law(1.5,2)
    3.0

    # Test case for invalid input
    >>> ohms_law(2,0)
    Traceback (most recent call last):
        ...
    ValueError: Zero resistance

    >>> ohms_law(0,3)
    Traceback (most recent call last):
        ...
    ValueError: Zero current
    """
    if current or resistance ==0
        raise ValueError('Current or Resistance cannot be zero')

    voltage = current * resistance
    return voltage


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
