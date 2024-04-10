"""
The van der Waals equation, named for its originator,
the Dutch physicist Johannes Diderik van der Waals,
is an equation of state that extends the ideal gas
law to include the non-zero size
of gas molecules and the interactions between them
(both of which depend on the specific substance).

As a result the equation is able to model the phase
change from liquid to gas, and vice versa.
It also produces simple analytic expressions for the
properties of real substances that shed light on their
behavior.

( Description was taken from https://en.wikipedia.org/wiki/Van_der_Waals_equation )

---------------------
| (p+a/V^2)(V-bv)=vRT |
---------------------
! p - Pressure (Pa)
! V - Volume (m^3)
! v - Amount of gas (mol)
! R - Universal gas constant
! T Absolute temperature (K)
! a, b - Parameters
"""

R = 8.314462618

# Taken from https://ru.wikipedia.org/wiki/Уравнение_Ван-дер-Ваальса
CONSTANTS = {
    "nitrogen": {"a": 0.1370, "b": 38.7e-6},
    "ammonia": {"a": 0.4225, "b": 37.1e-6},
    "argon": {"a": 0.1355, "b": 32.0e-6},
    "oxygen": {"a": 0.1382, "b": 31.9e-6},
}


def system_pressure(
    quantity: float, temperature: float, volume: float, a: float, b: float
) -> float:
    """
    Gets the system pressure from other 2 parameters
    ---------------------
    | p=(vRT)/(V-bv)-a/V^2 |
    ---------------------

    >>> system_pressure(1, 300, 1, 0.1382, 31.9e-6)
    2494.2801573455995
    >>> system_pressure(1, 100, 1, 0.1382, 31.9e-6)
    831.3345857818664
    >>> system_pressure(1, 300, -1, 0.1382, 31.9e-6)
    Traceback (most recent call last):
        ...
    ValueError: Please provide the positive values
    """

    if temperature < 0 or volume < 0:
        raise ValueError("Please provide the positive values")
    return (quantity * R * temperature) / (volume - quantity * b) - a / (volume**2)


def system_temperature(
    quantity: float, pressure: float, volume: float, a: float, b: float
) -> float:
    """
    Gets the system temperature from other 2 parameters
    ---------------------
    | T = 1/(vR)*(p+a/V^2)(V-bv) |
    ---------------------

    >>> system_temperature(1, 300, 1, 0.1382, 31.9e-6)
    36.09717661628195
    >>> system_temperature(1, 100, 1, 0.1382, 31.9e-6)
    12.04347294491859
    >>> system_temperature(1, 300, -1, 0.1382, 31.9e-6)
    Traceback (most recent call last):
        ...
    ValueError: Please provide the positive values
    """

    if pressure < 0 or volume < 0:
        raise ValueError("Please provide the positive values")
    return 1 / (quantity * R) * (pressure + a / volume**2) * (volume - quantity * b)


def critical_temperature(a: float, b: float) -> float:
    """
    Calculate the critical temperature from two parameters for each gas
    ---------------------
    | T_c=8a/(27bR) |
    ---------------------

    >>> critical_temperature(0.1382, 31.9e-6)
    154.3865270378366
    """

    return 8 * a / (27 * b * R)


def critical_volume(b: float) -> float:
    """
    Calculate the critical volume from one parameter for each gas
    ---------------------
    | V_c=3b |
    ---------------------

    >>> critical_volume(31.9e-6)
    9.570000000000001e-05
    """

    return 3 * b


def critical_pressure(a: float, b: float) -> float:
    """
    Calculate the critical pressure from two parameters for each gas
    ---------------------
    | p_c=a/(27b^2) |
    ---------------------

    >>> critical_pressure(0.1382, 31.9e-6)
    5029941.253052267
    """

    return a / (27 * b**2)


def critical_coefficient(a: float, b: float) -> float:
    """
    Calculate the critical coefficient from two parameters for each gas
    ---------------------
    | k_c=(R*T_c)/(p_c*V_c) |
    ---------------------

    >>> critical_coefficient(0.1382, 31.9e-6)
    2.6666666666666665
    """

    return (
        R * critical_temperature(a, b) / (critical_pressure(a, b) * critical_volume(b))
    )


def given_volume(volume: float, b: float) -> float:
    """
    Calculate the given volume from one parameter for each gas and volume
    ---------------------
    | φ = V / V_c |
    ---------------------

    >>> given_volume(1, 31.9e-6)
    10449.32079414838
    """

    return volume / critical_volume(b)


def given_pressure(pressure: float, a: float, b: float) -> float:
    """
    Calculate the given pressure from two parameters for each gas and pressure
    ---------------------
    | π = p / p_c |
    ---------------------

    >>> given_pressure(1, 0.1382, 31.9e-6)
    1.9880947901591899e-07
    """

    return pressure / critical_pressure(a, b)


def given_temperature(temperature: float, a: float, b: float) -> float:
    """
    Calculate the given temperature from two parameters for each gas and temperature
    ---------------------
    | τ = T / T_c |
    ---------------------

    >>> given_temperature(1, 0.1382, 31.9e-6)
    0.006477249143346057
    """

    return temperature / critical_temperature(a, b)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
