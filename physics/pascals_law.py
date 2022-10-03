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

How to use?
Inputs:
    ___________________________________________________
   |Name         | Units                   | Type      |
   |-------------|-------------------------|-----------|
   |pressure     | (in Newton/(meters^2))  | float     |
   |-------------|-------------------------|-----------|
   |area         | (in (meters^2))         | float     |
   |_____________|_________________________|___________|

Output:
    ___________________________________________________
   |Name         | Units                   | Type      |
   |-------------|-------------------------|-----------|
   |force        | (in Newtons)            | float     |
   |_____________|_________________________|___________|

"""


def pascals_law(pressure: float, area: float) -> float:
    """
    >>> pascals_law(10, 10)
    100
    >>> pascals_law(2.0, 2)
    2.0
    """
    force = float()
    try:
        force = pressure * area
    except Exception:
        return -0.0
    return force


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()

    # demo
    pressure = 30.5
    area = 5.2
    force = pascals_law(pressure, area)
    print("The force is ", force, "N.")
