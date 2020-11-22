# Importing doctest for testing our function
from doctest import testmod

# Defining function


def ohms_law(voltage: float, current: float, resistance: float) -> float:

    """
    This function calculates the any one
    of the three ohms_law values voltage,
    current, resistance, of electronics.
    >>> ohms_law(voltage=10, resistance=5,current=0 )
    2.0
    >>> ohms_law(current=1, resistance=10, voltage=0)
    10.0
    """
    if voltage == 0:
        result = float(current * resistance)
        return result
    elif current == 0:
        result = voltage / resistance
        return result
    elif resistance == 0:
        result = voltage / current
        return result
    else:
        return 0


if __name__ == "__main__":
    testmod(name="ohms_law", verbose=True)
