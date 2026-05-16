from math import log

from scipy.constants import Boltzmann, physical_constants

T = 300  # TEMPERATURE (unit = K)


def builtin_voltage(
    donor_conc: float,  # donor concentration
    acceptor_conc: float,  # acceptor concentration
    intrinsic_conc: float,  # intrinsic concentration
) -> float:
    """
    This function can calculate the Builtin Voltage of a pn junction diode.
    This is calculated from the given three values.
    Examples -
    >>> builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=1e10)
    0.833370010652644
    >>> builtin_voltage(donor_conc=0, acceptor_conc=1600, intrinsic_conc=200)
    Traceback (most recent call last):
      ...
    ValueError: Donor concentration should be positive
    >>> builtin_voltage(donor_conc=1000, acceptor_conc=0, intrinsic_conc=1200)
    Traceback (most recent call last):
      ...
    ValueError: Acceptor concentration should be positive
    >>> builtin_voltage(donor_conc=1000, acceptor_conc=1000, intrinsic_conc=0)
    Traceback (most recent call last):
      ...
    ValueError: Intrinsic concentration should be positive
    >>> builtin_voltage(donor_conc=1000, acceptor_conc=3000, intrinsic_conc=2000)
    Traceback (most recent call last):
      ...
    ValueError: Donor concentration should be greater than intrinsic concentration
    >>> builtin_voltage(donor_conc=3000, acceptor_conc=1000, intrinsic_conc=2000)
    Traceback (most recent call last):
      ...
    ValueError: Acceptor concentration should be greater than intrinsic concentration
    """

    if donor_conc <= 0:
        raise ValueError("Donor concentration should be positive")
    elif acceptor_conc <= 0:
        raise ValueError("Acceptor concentration should be positive")
    elif intrinsic_conc <= 0:
        raise ValueError("Intrinsic concentration should be positive")
    elif donor_conc <= intrinsic_conc:
        raise ValueError(
            "Donor concentration should be greater than intrinsic concentration"
        )
    elif acceptor_conc <= intrinsic_conc:
        raise ValueError(
            "Acceptor concentration should be greater than intrinsic concentration"
        )
    else:
        return (
            Boltzmann
            * T
            * log((donor_conc * acceptor_conc) / intrinsic_conc**2)
            / physical_constants["electron volt"][0]
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
