"""
Title : Finding the value of either Coulomb Force, one of the charges or distance
provided that the other three parameters are given.
Description : Coulomb's inverse-square law, or simply Coulomb's law, is an experimental law
of physics that quantifies the amount of force between two stationary, electrically charged particles.
The electric force between charged bodies at rest is conventionally called electrostatic force or Coulomb force
The equation for the Coulomb Force is as follows:
F = (K * |charge_1| * |charge_2|) / (distance)^2
Source :
- https://en.wikipedia.org/wiki/Coulomb%27s_law
"""


# Define the Coulombs Constant K and the function
Coulombs_CONSTANT = 8.988e9


def Coulombs_law(
    force: float, charge_1: float, charge_2: float, distance: float
) -> dict[str, float]:

    """
    Input Parameters
    ----------------
    force : magnitude in Newtons
    charge_1 : charge in Coulombs
    charge_2 : charge in Coulombs
    distance : distance in Meters
    Returns
    -------
    result : dict name, value pair of the parameter having Zero as it's value
    Returns the value of one of the parameters specified as 0, provided the values of
    other parameters are given.
    >>> Coulombs_law(force=0, charge_1=10, charge_2=1, distance=1)
    {'force': 8.988e10}
    >>> Coulombs_law(force=8.988e9, charge_1=0, charge_2=10, distance=0.1)
    {'charge_1': 0.0010000000000000002}
    >>> Coulombs_law(force=36337.283, charge_1=0, charge_2=0, distance=35584)
    Traceback (most recent call last):
        ...
    ValueError: One and only one argument must be 0
    >>> Coulombs_law(force=36337.283, charge_1=-674, charge_2=0, distance=35584)
    Traceback (most recent call last):
        ...
    ValueError: Magnitude of Coulombs force can not be negative
    >>> Coulombs_law(force=-847938e12, charge_1=674, charge_2=0, distance=9374)
    Traceback (most recent call last):
        ...
    ValueError: Magnitude of Coulombs force can not be negative
    """

    product_of_charge = charge_1 * charge_2

    if (force, charge_1, charge_2, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if force < 0:
        raise ValueError("Magnitude of Coulombs force can not be negative")
    if distance < 0:
        raise ValueError("Magnitude of Distance can not be negative")
    if charge_1 < 0 or charge_2 < 0:
        raise ValueError("Magnitude of charge can not be negative")
    if force == 0:
        force = Coulombs_CONSTANT * product_of_charge / (distance**2)
        return {"force": force}
    elif charge_1 == 0:
        charge_1 = (force) * (distance**2) / (Coulombs_CONSTANT * charge_2)
        return {"charge_1": charge_1}
    elif charge_2 == 0:
        charge_2 = (force) * (distance**2) / (Coulombs_CONSTANT * charge_1)
        return {"charge_2": charge_2}
    elif distance == 0:
        distance = (Coulombs_CONSTANT * product_of_charge / (force)) ** 0.5
        return {"distance": distance}
    raise ValueError("One and only one argument must be 0")


if __name__ == "__main__":
    print("Enter the magnitude of following  values and enter 0 in unknown value.")
    force = float(input("Enter the magnitude of force:"))
    charge_1 = float(input("Enter the magnitude of charge_1:"))
    charge_2 = float(input("Enter the magnitude of charge_2:"))
    distance = float(input("Enter the magnitude of distance:"))
    print(Coulombs_law(force, charge_1, charge_2, distance))
