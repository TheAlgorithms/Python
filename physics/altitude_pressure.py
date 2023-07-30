"""
Title : Calculate altitude using Pressure

Description :
    The below algorithm approximates the altitute using Barometric formula


"""


def get_altitude_at_pressure(pressure: float) -> float:
    """
    This method calculates the altitude from Pressure wrt to Sea level pressure as reference
    Pressure is in Pascals
    
    H = 44330 * [1 - (P/p0)^(1/5.255) ]
    
    Where :
    H = altitude (m)
    P = measured pressure
    p0 = reference pressure at sea level 101325 Pa

    Examples:

    >>> get_altitude_at_pressure(pressure=100000)
    105.47836610778828
    """

    if pressure > 101325:
        raise ValueError("Value Higer than Pressure at Sea Level !")

    return 44330 * (1-(pressure/101325)**(1/5.5255))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
