"""
The ideal gas law, also called the general gas equation, is the
equation of state of a hypothetical ideal gas. It is a good approximation
of the behavior of many gases under many conditions, although it has
several limitations. It was first stated by Benoît Paul Émile Clapeyron
in 1834 as a combination of the empirical Boyle's law, Charles's law,
Avogadro's law, and Gay-Lussac's law.[1] The ideal gas law is often written
in an empirical form:
 ------------
 | PV = nRT |
 ------------
P	=	Pressure (Pa)
V	=	Volume (m^3)
n	=	Amount of substance (mol)
R	=	Universal gas constant
T	=	Absolute temperature (Kelvin)

(Description adapted from https://en.wikipedia.org/wiki/Ideal_gas_law )
"""

UNIVERSAL_GAS_CONSTANT = 8.314462


def pressure_of_gas_system(moles: float, kelvin: float, volume: float) -> float:
    """
    >>> pressure_of_gas_system(2, 100, 5)
    332.57848
    >>> pressure_of_gas_system(0.5, 273, 0.004)
    283731.01575
    """
    if moles < 0 or kelvin < 0 or volume < 0:
        raise Exception("Invalid inputs. Enter positive value.")
    pressure: float = moles * kelvin * UNIVERSAL_GAS_CONSTANT / volume
    return pressure


def volume_of_gas_system(moles: float, kelvin: float, pressure: float) -> float:
    """
    >>> volume_of_gas_system(2, 100, 5)
    332.57848
    >>> volume_of_gas_system(0.5, 273, 0.004)
    283731.01575
    """
    if moles < 0 or kelvin < 0 or pressure < 0:
        raise Exception("Invalid inputs. Enter positive value.")
    volume: float = moles * kelvin * UNIVERSAL_GAS_CONSTANT / pressure
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / pressure


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Example 1
    example_1_volume = 5
    example_1_moles = 2
    example_1_kelvin = 100
    example_1_pressure = pressure_of_gas_system(
        example_1_moles, example_1_kelvin, example_1_volume
    )
    print(
        f"""Pressure(P) of a gas system with V = {example_1_volume} [m^3],
        n = {example_1_moles} [mol], T = {example_1_kelvin} [K]:"""
    )
    print(f"{example_1_pressure} [Pa]")

    print()

    # Example 2
    example_2_pressure = 0.004
    example_2_moles = 0.5
    example_2_kelvin = 273
    examle_2_volume = volume_of_gas_system(
        example_2_moles, example_2_kelvin, example_2_pressure
    )
    print(
        f"""Volume(V) of a gas system with P = {example_2_pressure} [Pa],
        n = {example_2_moles} [mol], T = {example_2_kelvin} [K]:"""
    )
    print(f"{examle_2_volume} [m^3]")
