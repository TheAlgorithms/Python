"""
Title : Calculate altitude using Pressure

Description :
    The below algorithm approximates the altitude using Barometric formula


"""


def get_altitude_at_pressure(pressure: float) -> float:
    """
    This method calculates the altitude from Pressure wrt to
    Sea level pressure as reference .Pressure is in Pascals
    https://en.wikipedia.org/wiki/Pressure_altitude
    https://community.bosch-sensortec.com/t5/Question-and-answers/How-to-calculate-the-altitude-from-the-pressure-sensor-data/qaq-p/5702

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
        raise ValueError("Value Higher than Pressure at Sea Level !")

    return 44_330 * (1 - (pressure / 101_325) ** (1 / 5.5255))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
