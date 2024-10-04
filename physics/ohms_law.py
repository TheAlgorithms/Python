def ohms_law(current: float, resistance: float, decimals: int = 1) -> float:
    """
    Calculate the voltage when current and resistance data is given using Ohm's Law.

    Ohm's Law states that:
    V = I * R
    
    Where:
    V = Voltage (Volts)
    I = Current (Amperes)
    R = Resistance (Ohms)
    
    Parameters:
    current (float): The current in Amperes (A).
    resistance (float): The resistance in Ohms (Ω).
    decimals (int): The number of decimal places to round the voltage. Default is 1.
    
    Returns:
    float: The calculated voltage in Volts (V).
    
    Examples:
    >>> ohms_law(2.0, 5.0)
    10.0
    
    >>> ohms_law(1.0, 4.0)
    4.0
    
    >>> ohms_law(3, 0.5)
    1.5
    
    >>> ohms_law(1.5, 2.0)
    3.0
    
    # Test case for invalid input (zero resistance)
    >>> ohms_law(2, 0)
    Traceback (most recent call last):
        ...
    ValueError: Zero resistance
    
    # Test case for invalid input (zero current)
    >>> ohms_law(0, 3)
    Traceback (most recent call last):
        ...
    ValueError: Zero current
    """
    if current == 0:
        raise ValueError('Zero current')
    if resistance == 0:
        raise ValueError('Zero resistance')

    voltage = current * resistance 
    return round(voltage, decimals)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
