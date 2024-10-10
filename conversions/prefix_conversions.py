"""
Uluslararası Ölçü Birimleri (SI) ve İkili ön ekleri dönüştürme
"""

from __future__ import annotations

from enum import Enum


class SIUnit(Enum):
    yotta = 24
    zetta = 21
    exa = 18
    peta = 15
    tera = 12
    giga = 9
    mega = 6
    kilo = 3
    hecto = 2
    deca = 1
    deci = -1
    centi = -2
    milli = -3
    micro = -6
    nano = -9
    pico = -12
    femto = -15
    atto = -18
    zepto = -21
    yocto = -24


class BinaryUnit(Enum):
    yotta = 8
    zetta = 7
    exa = 6
    peta = 5
    tera = 4
    giga = 3
    mega = 2
    kilo = 1


def si_on_ek_dönüştür(
    bilinen_miktar: float,
    bilinen_on_ek: str | SIUnit,
    bilinmeyen_on_ek: str | SIUnit,
) -> float:
    """
    Wikipedia referansı: https://en.wikipedia.org/wiki/Binary_prefix
    Wikipedia referansı: https://en.wikipedia.org/wiki/International_System_of_Units
    >>> si_on_ek_dönüştür(1, SIUnit.giga, SIUnit.mega)
    1000
    >>> si_on_ek_dönüştür(1, SIUnit.mega, SIUnit.giga)
    0.001
    >>> si_on_ek_dönüştür(1, SIUnit.kilo, SIUnit.kilo)
    1
    >>> si_on_ek_dönüştür(1, 'giga', 'mega')
    1000
    >>> si_on_ek_dönüştür(1, 'gIGa', 'mEGa')
    1000
    """
    if isinstance(bilinen_on_ek, str):
        bilinen_on_ek = SIUnit[bilinen_on_ek.lower()]
    if isinstance(bilinmeyen_on_ek, str):
        bilinmeyen_on_ek = SIUnit[bilinmeyen_on_ek.lower()]
    bilinmeyen_miktar: float = bilinen_miktar * (
        10 ** (bilinen_on_ek.value - bilinmeyen_on_ek.value)
    )
    return bilinmeyen_miktar


def ikili_on_ek_dönüştür(
    bilinen_miktar: float,
    bilinen_on_ek: str | BinaryUnit,
    bilinmeyen_on_ek: str | BinaryUnit,
) -> float:
    """
    Wikipedia referansı: https://en.wikipedia.org/wiki/Metric_prefix
    >>> ikili_on_ek_dönüştür(1, BinaryUnit.giga, BinaryUnit.mega)
    1024
    >>> ikili_on_ek_dönüştür(1, BinaryUnit.mega, BinaryUnit.giga)
    0.0009765625
    >>> ikili_on_ek_dönüştür(1, BinaryUnit.kilo, BinaryUnit.kilo)
    1
    >>> ikili_on_ek_dönüştür(1, 'giga', 'mega')
    1024
    >>> ikili_on_ek_dönüştür(1, 'gIGa', 'mEGa')
    1024
    """
    if isinstance(bilinen_on_ek, str):
        bilinen_on_ek = BinaryUnit[bilinen_on_ek.lower()]
    if isinstance(bilinmeyen_on_ek, str):
        bilinmeyen_on_ek = BinaryUnit[bilinmeyen_on_ek.lower()]
    bilinmeyen_miktar: float = bilinen_miktar * (
        2 ** ((bilinen_on_ek.value - bilinmeyen_on_ek.value) * 10)
    )
    return bilinmeyen_miktar


if __name__ == "__main__":
    import doctest

    doctest.testmod()
