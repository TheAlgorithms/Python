# https://en.wikipedia.org/wiki/Magnetic_circuit#Hopkinson's_law
from __future__ import annotations


def hopkinsons_law(
    magnetomotiveforce: float, flux: float, reluctance: float
) -> dict[str, float]:
    """
    Hopkinson's Law can be applied,on any two given electrical values,
    which can be magnetomotive,force, flux, and reluctance,
    and then in a Python dict return name/value pair of the zero value.

    >>> hopkinsons_law(magnetomotiveforce=10, flux=5, reluctance=0)
    {'reluctance': 2.0}
    >>> hopkinsons_law(magnetomotiveforce=0, flux=0, reluctance=10)
    Traceback (most recent call last):
      ...
    ValueError: One and only one argument must be 0
    >>> hopkinsons_law(magnetomotiveforce=0, flux=1, reluctance=-2)
    Traceback (most recent call last):
      ...
    ValueError: Reluctance cannot be negative
    >>> hopkinsons_law(reluctance=0, magnetomotiveforce=-10, flux=1)
    {'reluctance': -10.0}
    >>> hopkinsons_law(magnetomotiveforce=0, flux=-1.5, reluctance=2)
    {'magnetomotiveforce': -3.0}
    """
    if (magnetomotiveforce, flux, reluctance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if reluctance < 0:
        raise ValueError("Reluctance cannot be negative")
    if magnetomotiveforce == 0:
        return {"magnetomotiveforce": float(flux * reluctance)}
    elif flux == 0:
        return {"flux": magnetomotiveforce / reluctance}
    elif reluctance == 0:
        return {"reluctance": magnetomotiveforce / flux}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
