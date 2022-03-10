# https://en.wikipedia.org/wiki/Charge_carrier_density
# https://www.pveducation.org/pvcdrom/pn-junctions/equilibrium-carrier-concentration
# http://www.ece.utep.edu/courses/ee3329/ee3329/Studyguide/ToC/Fundamentals/Carriers/concentrations.html

from __future__ import annotations


def carrier_concentration(
    electron_conc: float,
    hole_conc: float,
    intrinsic_conc: float,
) -> tuple:
    """
    This function can calculate any one of the three -
    1. Electron Concentration
    2, Hole Concentration
    3. Intrinsic Concentration
    given the other two.
    Examples -
    >>> carrier_concentration(electron_conc=25, hole_conc=100, intrinsic_conc=0)
    ('intrinsic_conc', 50.0)
    >>> carrier_concentration(electron_conc=0, hole_conc=1600, intrinsic_conc=200)
    ('electron_conc', 25.0)
    >>> carrier_concentration(electron_conc=1000, hole_conc=0, intrinsic_conc=1200)
    ('hole_conc', 1440.0)
    >>> carrier_concentration(electron_conc=1000, hole_conc=400, intrinsic_conc=1200)
    Traceback (most recent call last):
        File "<stdin>", line 37, in <module>
    ValueError: You cannot supply more or less than 2 values
    >>> carrier_concentration(electron_conc=-1000, hole_conc=0, intrinsic_conc=1200)
    Traceback (most recent call last):
        File "<stdin>", line 40, in <module>
    ValueError: Electron concentration cannot be negative in a semiconductor
    >>> carrier_concentration(electron_conc=0, hole_conc=-400, intrinsic_conc=1200)
    Traceback (most recent call last):
        File "<stdin>", line 44, in <module>
    ValueError: Hole concentration cannot be negative in a semiconductor
    >>> carrier_concentration(electron_conc=0, hole_conc=400, intrinsic_conc=-1200)
    Traceback (most recent call last):
        File "<stdin>", line 48, in <module>
    ValueError: Intrinsic concentration cannot be negative in a semiconductor
    """
    if (electron_conc, hole_conc, intrinsic_conc).count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")
    elif electron_conc < 0:
        raise ValueError("Electron concentration cannot be negative in a semiconductor")
    elif hole_conc < 0:
        raise ValueError("Hole concentration cannot be negative in a semiconductor")
    elif intrinsic_conc < 0:
        raise ValueError(
            "Intrinsic concentration cannot be negative in a semiconductor"
        )
    elif electron_conc == 0:
        return (
            "electron_conc",
            intrinsic_conc**2 / hole_conc,
        )
    elif hole_conc == 0:
        return (
            "hole_conc",
            intrinsic_conc**2 / electron_conc,
        )
    elif intrinsic_conc == 0:
        return (
            "intrinsic_conc",
            (electron_conc * hole_conc) ** 0.5,
        )
    else:
        return (-1, -1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
