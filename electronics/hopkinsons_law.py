# https://en.wikipedia.org/wiki/Magnetic_circuit#Hopkinson's_law
from __future__ import annotations


def hopkinsons_law(
    magnetomotiveforce: float, flux: float, reluctance: float
) -> dict[str, float]:
    """
    Hopkinson's Law can be applied, on any two given electrical values,
    which can be magnetomotive, force, flux, and reluctance,
    and then in a Python dict return name/value pair of the zero value.
    >>> hopkinsons_law(1,2,None)
    {'reluctance': 0.5}
    >>> hopkinsons_law(0.5,None,2)
    {'flux': 0.25}
    >>> hopkinsons_law(None,1,3)
    {'magnetomotiveforce': 3.0}
    >>> hopkinsons_law(None,None,None)
    Traceback (most recent call last):
    ...
    ValueError: All arguments cannot be None
    >>> hopkinsons_law(1,None,None)
    Traceback (most recent call last):
    ...
    ValueError: Exactly one argument must be None
    """
    if (magnetomotiveforce, flux, reluctance).count(None) == 3:
        raise ValueError("All arguments cannot be None")
    elif (magnetomotiveforce, flux, reluctance).count(None) != 1:
        raise ValueError("Exactly one argument must be None")
    elif magnetomotiveforce is None:
        return {"magnetomotiveforce": float(flux * reluctance)}
    elif flux is None:
        return {"flux": float(magnetomotiveforce / reluctance)}
    elif reluctance is None:
        return {"reluctance": float(magnetomotiveforce / flux)}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
