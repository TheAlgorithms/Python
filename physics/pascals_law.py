"""
Description :
This law states that pressure exerted in some liquid which is at rest is the same in all the directions.
OR
Whenever an external pressure is applied on any part of a fluid contained in a vessel, it is transmitted undiminished and equally in all directions.

Source: https://www.vedantu.com/physics/pascal-law
Formulation: F = P * A
Where, P= Pressure, F=Force and A=Area of contact

Units:
1 Newton = 1 Newton/(meters^2) X (meters^2)
"""


def pascals_law(pressure: float, area: float) -> float:
    """
    >>> pascals_law(10, 10)
    100
    >>> pascals_law(2.0, 2)
    4.0
    """
    try:
        force = pressure * area
        return force
    except Exception:
        return -0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    pressure = 30.5
    area = 5.2
    force = pascals_law(pressure, area)
    print("The force is ", force, "N.")
