"""
Title : Implementation of Boyle's law.

Description :
    Boyle's law, also referred to as the Boyle-Mariotte law, or Mariotte's law
    (especially in France), is a gas law which states that the pressure exerted
    by a gas of a fixed mass and temperature is inversely proportional to the
    volume occupied by it.

    For a gas, the relationship between volume and pressure (at constant mass and
    temperature) can be expressed mathematically as follows.

    P ∝ (1/V)

    Where P is the pressure exerted by the gas and V is the volume occupied by it. This
    proportionality can be converted into an equation by adding a constant, k.

    P = k*(1/V) ⇒ PV = k

    Boyle's law states that when the temperature of a given mass of confined gas is
    constant,the product of its pressure and volume is also constant. When comparing the
    same substance under two different sets of conditions, the law can be expressed as:

    P1V1 = P2V2

    Where,

    P1 is the initial pressure exerted by the gas in Pascals (P)
    V1 is the initial volume occupied by the gas Litres (L)
    P2 is the final pressure exerted by the gas Pascals (P)
    V2 is the final volume occupied by the gas Litres (L)

    This equation can be used to predict the increase in the pressure exerted by a gas
    on the walls of its container when the volume of its container is decreased
    (and its quantity and absolute temperature remain unchanged).

Sources :
    https://en.wikipedia.org/wiki/Boyle%27s_law
    https://byjus.com/chemistry/boyles-law/
"""

valid_variables: list[str] = ["v1", "v2", "p1", "p2"]


def check_validity(values: dict[str, float]) -> None:
    """

    Function takes dictionary as an input and returns nothing if the input
    is valid

    >>> check_validity({})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input expected 3 items, got 0

    >>> check_validity({'v1':2,'v2':4,'k':6})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input k is not a valid variable

    >>> check_validity({'v1':2,'v2':4,'p1':-6})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input p1 must be greater than 0

    >>> check_validity({'v1':2,'v2':4,'p1':6})

    """
    if len(values) != 3:
        msg = f"Invalid input expected {3} items, got {len(values)}"
        raise ValueError(msg)
    else:
        for value in values:
            if value not in valid_variables:
                msg = f"Invalid input {value} is not a valid variable"
                raise ValueError(msg)
            if values[value] <= 0:
                msg = f"Invalid input {value} must be greater than 0"
                raise ValueError(msg)
        return


def find_target_variable(values: dict[str, float]) -> str:
    """

    Function is used to get the valid target variable whose value needs to be found
    using Boyle's Law.
    Function takes a dictionary as an input and returns a string

    >>> find_target_variable({})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input expected 3 items, got 0

    >>> find_target_variable({'v1':1,'v2':2,'p2':4})
    'p1'

    >>> find_target_variable({'v1':1,'v2':2,'k':4})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input k is not a valid variable

    >>> find_target_variable({'v1':1,'v2':-2,'p2':4})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input v2 must be greater than 0

    """
    check_validity(values)
    for variable in valid_variables:
        if variable not in values:
            return variable
    raise ValueError("Input is invalid")


def boyles_law(values: dict[str, float]) -> dict[str, str]:
    """

    Function calculates the the unknown pressure or volume using Boyle's law.
    Function takes a dictionary as an input. It contains values for respective
    pressure and volumes and computes the required value and returns it as
    output

    >>> boyles_law({'p1':2,'v2':1})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input expected 3 items, got 2

    >>> boyles_law({})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input expected 3 items, got 0

    >>> boyles_law({'p1':2,'v2':1, 'k':6})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input k is not a valid variable

    >>> boyles_law({'p1':2,'v2':1, 'v1':-6})
    Traceback (most recent call last):
        ...
    ValueError: Invalid input v1 must be greater than 0

    >>> boyles_law({'p1':100,'v2':150, 'v1':120})
    {'p2': '80.0 Pa'}

    >>> boyles_law({'p1':10,'v1':20, 'p2':20})
    {'v2': '10.0 L'}

    >>> boyles_law({'v1':13,'p2':17, 'v2':19})
    {'p1': '24.846 Pa'}

    >>> boyles_law({'v2':27,'p1':25, 'p2':29})
    {'v1': '31.32 L'}

    """
    check_validity(values)
    target = find_target_variable(values)
    float_precision = ".3f"
    if target == "p1":
        p1 = float(
            format((values["p2"] * values["v2"]) / values["v1"], float_precision)
        )
        return {"p1": f"{p1} Pa"}
    elif target == "v1":
        v1 = float(
            format((values["p2"] * values["v2"]) / values["p1"], float_precision)
        )
        return {"v1": f"{v1} L"}
    elif target == "p2":
        p2 = float(
            format((values["p1"] * values["v1"]) / values["v2"], float_precision)
        )
        return {"p2": f"{p2} Pa"}
    else:
        v2 = float(
            format((values["p1"] * values["v1"]) / values["p2"], float_precision)
        )
        return {"v2": f"{v2} L"}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
