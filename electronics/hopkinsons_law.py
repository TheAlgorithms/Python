# https://en.wikipedia.org/wiki/Magnetic_circuit#Hopkinson's_law
from __future__ import annotations


def hopkinsons_law(
    magnetomotive_force: float, flux: float, reluctance: float
) -> dict[str, float]:
    """
    Apply Hopkinson's Law, on any two given electrical values, which can be magnetomotive force, flux,
    and reluctance, and then in a Python dict return name/value pair of the zero value.

    >>> hopkinsons_law(magnetomotive_force=10, reluctance=5, flux=0)
    {'flux': 2.0}
    >>> hopkinsons_law(magnetomotive_force=0, flux=0, reluctance=10)
    Traceback (most recent call last):
      ...
    ValueError: One and only one argument must be 0
    >>> hopkinsons_law(magnetomotive_force=0, flux=1, reluctance=-2)
    Traceback (most recent call last):
      ...
    ValueError: Reluctance cannot be negative
    >>> hopkinsons_law(reluctance=0, magnetomotive_force=-10, flux=1)
    {'reluctance': -10.0}
    >>> hopkinsons_law(magnetomotive_force=0, flux=-1.5, reluctance=2)
    {'magnetomotive_force': -3.0}
    """
    if (magnetomotive_force, flux, reluctance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if reluctance < 0:
        raise ValueError("Reluctance cannot be negative")
    if magnetomotive_force == 0:
        return {"magnetomotive_force": float(flux * reluctance)}
    elif flux == 0:
        return {"flux": magnetomotive_force / reluctance}
    elif reluctance == 0:
        return {"reluctance": magnetomotive_force / flux}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
