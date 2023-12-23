# https://en.wikipedia.org/wiki/Friis_transmission_equation
from __future__ import annotations
import math


def friis_transmission(
    Pt: float, Pr: float, Gr: float, Gt: float, d: float, wavelength: float
) -> dict[str, float]:
    """
    Apply Friis Transmission Formula on any six given values.These can be Power Transmitted, Power Received,
    DistanceWavelength ,Gain of the Receiving Antenna and Gain of the Transmitting Antenna
    and then in a Python dict return name/value pair of the zero value.

    Friis Transmission Formula states that the power received by an antenna is proportional to the
    power density of the signal and the effective area of the receiving antenna, and inversely
    proportional to the square of the distance from the transmitter.

    Reference
    ----------
    Friis, H. T. (1946). "A Note on a Simple Transmission Formula". Proceedings of the IRE. 34 (5): 254–256.

    Parameters
    ----------
    Pt : float with units in Watts
    Pr: float with units in Watts
    Gr: float with units in dB
    Gt: float with units in dB
    d: float with units in meters
    wavelength: float with units in meters

    Returns
    -------
    result : dict name/value pair of the zero value

    >>> friis_transmission(Pt=0, Pr=0, Gr=0, Gt=0, d=0, wavelength=0)
    Traceback (most recent call last):
        ...
    ValueError: One and only one argument must be 0

    >>> friis_tranmission(Pt=3, Pr=0.0645, Gr=12, Gt=30, d=-100, wavelength=0.1)
    Traceback (most recent call last):
        ...
    ValueEroor: Distance cannot be negative
    >>> friis_transmission(Pt=3,Pr=0,Gt=15,Gr=25,d=10,wavelegth=0.1)
    {'Pr': 0.0189}

    >>> friss_transmission(Pt=0,Pr=0.000001,Gt=40,Gr=40,d=48000,wavelength=0.075)
    {'Pt': 0.64}

    >>> friss_trainmission(Pt=0.64,Pr=0.0189,Gt=40,Gr=10,d=10,wavelength=0)
    {'wavelength': 0.02697}

    >>> friss_transmission{Pt=0.64,Pr=0.0189,Gt=40,Gr=10,d=10,wavelength=0.026}
    {'d': 1045.32}

    >>> friss_transmission(Pt=0.64,Pr=0.0189,Gt=0,Gr=10,d=10,wavelength=0.02697)
    {'Gt':-27.43}

    >>> friis_transmission(Pt=0.64,Pr=0.0189,Gt=27.43,Gr=10,d=10,wavelength=0.02697)
    {'Gr': -27.43}

    """
    if (Pt, Pr, Gr, Gt, d, wavelength).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if d < 0:
        raise ValueError("Distance cannot be negative")
    if Pr == 0:
        Gt_lin = 10 ** (Gt / 10)
        Gr_lin = 10 ** (Gr / 10)
        Pr = Pt * (Gt_lin * Gr_lin * (wavelength / (4 * math.pi * d)) ** 2)
        return {"Pr": Pr}
    elif Pt == 0:
        Gt_lin = 10 ** (Gt / 10)
        Gr_lin = 10 ** (Gr / 10)
        Pt = Pr / (Gt_lin * Gr_lin * (wavelength / (4 * math.pi * d)) ** 2)
        return {"Pt": Pt}
    elif Gt == 0:
        Gr_lin = 10 ** (Gr / 10)
        Gt_lin = (Pr / Pt) * (wavelength**2 * d**2) / Gr_lin
        Gt = 10 * math.log10(Gt_lin)
        return {"Gt": Gt}
    elif Gr == 0:
        Gt_lin = 10 ** (Gt / 10)
        Gr_lin = (Pr / Pt) * (wavelength**2 * d**2) / Gt_lin
        Gr = 10 * math.log10(Gr_lin)
        return {"Gr": Gr}
    elif d == 0:
        Gt_lin = 10 ** (Gt / 10)
        Gr_lin = 10 ** (Gr / 10)
        d = math.sqrt((Gr_lin * Gt_lin) / ((Pt / Pr) * wavelength**2))
        return {"d": d}
    elif wavelength == 0:
        Gt_lin = 10 ** (Gt / 10)
        Gr_lin = 10 ** (Gr / 10)
        wavelength = math.sqrt((Gr_lin * Gt_lin) / ((Pt / Pr) * d**2))
        return {"wavelength": wavelength}
    raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
