"""
The root-mean-square, average and most probable speeds of gas molecules are
derived from the Maxwell-Boltzmann distribution. The Maxwell-Boltzmann
distribution is a probability distribution that describes the distribution of
speeds of particles in an ideal gas.

The distribution is given by the following equation::

        -------------------------------------------------
        | f(v) = (M/2πRT)^(3/2) * 4πv^2 * e^(-Mv^2/2RT) |
        -------------------------------------------------

where:
    * ``f(v)`` is the fraction of molecules with a speed ``v``
    * ``M`` is the molar mass of the gas in kg/mol
    * ``R`` is the gas constant
    * ``T`` is the absolute temperature

More information about the Maxwell-Boltzmann distribution can be found here:
https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution

The average speed can be calculated by integrating the Maxwell-Boltzmann distribution
from 0 to infinity and dividing by the total number of molecules. The result is::

        ----------------------
        | v_avg = √(8RT/πM)  |
        ----------------------

The most probable speed is the speed at which the Maxwell-Boltzmann distribution
is at its maximum. This can be found by differentiating the Maxwell-Boltzmann
distribution with respect to ``v`` and setting the result equal to zero. The result is::

        ----------------------
        | v_mp = √(2RT/M)    |
        ----------------------

The root-mean-square speed is another measure of the average speed
of the molecules in a gas. It is calculated by taking the square root
of the average of the squares of the speeds of the molecules. The result is::

        ----------------------
        | v_rms = √(3RT/M)   |
        ----------------------

Here we have defined functions to calculate the average and
most probable speeds of molecules in a gas given the
temperature and molar mass of the gas.
"""

# import the constants R and pi from the scipy.constants library
from scipy.constants import R, pi


def avg_speed_of_molecule(temperature: float, molar_mass: float) -> float:
    """
    Takes the temperature (in K) and molar mass (in kg/mol) of a gas
    and returns the average speed of a molecule in the gas (in m/s).

    Examples:

    >>> avg_speed_of_molecule(273, 0.028) # nitrogen at 273 K
    454.3488755020387
    >>> avg_speed_of_molecule(300, 0.032) # oxygen at 300 K
    445.52572733919885
    >>> avg_speed_of_molecule(-273, 0.028) # invalid temperature
    Traceback (most recent call last):
        ...
    Exception: Absolute temperature cannot be less than 0 K
    >>> avg_speed_of_molecule(273, 0) # invalid molar mass
    Traceback (most recent call last):
        ...
    Exception: Molar mass should be greater than 0 kg/mol
    """

    if temperature < 0:
        raise Exception("Absolute temperature cannot be less than 0 K")
    if molar_mass <= 0:
        raise Exception("Molar mass should be greater than 0 kg/mol")
    return (8 * R * temperature / (pi * molar_mass)) ** 0.5


def mps_speed_of_molecule(temperature: float, molar_mass: float) -> float:
    """
    Takes the temperature (in K) and molar mass (in kg/mol) of a gas
    and returns the most probable speed of a molecule in the gas (in m/s).

    Examples:

    >>> mps_speed_of_molecule(273, 0.028) # nitrogen at 273 K
    402.65620701908966
    >>> mps_speed_of_molecule(300, 0.032) # oxygen at 300 K
    394.836895549922
    >>> mps_speed_of_molecule(-273, 0.028) # invalid temperature
    Traceback (most recent call last):
        ...
    Exception: Absolute temperature cannot be less than 0 K
    >>> mps_speed_of_molecule(273, 0) # invalid molar mass
    Traceback (most recent call last):
        ...
    Exception: Molar mass should be greater than 0 kg/mol
    """

    if temperature < 0:
        raise Exception("Absolute temperature cannot be less than 0 K")
    if molar_mass <= 0:
        raise Exception("Molar mass should be greater than 0 kg/mol")
    return (2 * R * temperature / molar_mass) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
