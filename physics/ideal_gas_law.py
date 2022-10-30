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

UNIVERSAL_GAS_CONSTANT = 8.314462  # Unit - J mol-1 K-1


def pressure_of_gas_system(moles: float, kelvin: float, volume: float) -> float:
    """
    >>> pressure_of_gas_system(2, 100, 5)
    332.57848
    >>> pressure_of_gas_system(0.5, 273, 0.004)
    283731.01575
    >>> pressure_of_gas_system(3, -0.46, 23.5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter positive value.
    """
    if moles < 0 or kelvin < 0 or volume < 0:
        raise ValueError("Invalid inputs. Enter positive value.")
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / volume


def volume_of_gas_system(moles: float, kelvin: float, pressure: float) -> float:
    """
    >>> volume_of_gas_system(2, 100, 5)
    332.57848
    >>> volume_of_gas_system(0.5, 273, 0.004)
    283731.01575
    >>> volume_of_gas_system(3, -0.46, 23.5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter positive value.
    """
    if moles < 0 or kelvin < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / pressure


if __name__ == "__main__":
    from doctest import testmod

    testmod()
