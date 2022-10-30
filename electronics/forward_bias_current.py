from math import e

from scipy.constants import Boltzmann, physical_constants

T = 300  # TEMPERATURE (unit = K)


def forward_bias_current(
    forward_voltage: float,
    reverse_saturation_current: float,
) -> float:
    """
    This function can calculate the Forward Bias Current of a pn junction diode.
    This is calculated from the given two values.
    Examples -
    >>> forward_bias_current(forward_voltage=0.7, reverse_saturation_current=1e-12)
    0.5747545691036846
    >>> forward_bias_current(forward_voltage=-5, reverse_saturation_current=1e-12)
    Traceback (most recent call last):
      ...
    ValueError: Forward voltage cannot be negative
    >>> forward_bias_current(forward_voltage=10, reverse_saturation_current=-2)
    Traceback (most recent call last):
      ...
    ValueError: Reverse saturation current should be positive
    >>> forward_bias_current(forward_voltage=10, reverse_saturation_current=1e17)
    Traceback (most recent call last):
      ...
    ValueError: Reverse saturation current cannot be greater than 1e-5
    """

    if voltage < 0:
        raise ValueError("Forward voltage cannot be negative")
    elif rev_sat_current <= 0:
        raise ValueError("Reverse saturation current should be positive")
    elif rev_sat_current > 1e-5:
        raise ValueError("Reverse saturation current cannot be greater than 1e-5")
    else:
        return reverse_saturation_current * (
            e
            ** (
                (forward_voltage * physical_constants["electron volt"][0])
                / (Boltzmann * T)
            )
            - 1
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
