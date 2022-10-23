"""
Convert International System of Units (SI) and Binary prefixes
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


def convert_si_prefix(
    known_amount: float,
    known_prefix: str | SIUnit,
    unknown_prefix: str | SIUnit,
) -> float:
    """
    Wikipedia reference: https://en.wikipedia.org/wiki/Binary_prefix
    Wikipedia reference: https://en.wikipedia.org/wiki/International_System_of_Units
    >>> convert_si_prefix(1, SIUnit.giga, SIUnit.mega)
    1000
    >>> convert_si_prefix(1, SIUnit.mega, SIUnit.giga)
    0.001
    >>> convert_si_prefix(1, SIUnit.kilo, SIUnit.kilo)
    1
    >>> convert_si_prefix(1, 'giga', 'mega')
    1000
    >>> convert_si_prefix(1, 'gIGa', 'mEGa')
    1000
    """
    if isinstance(known_prefix, str):
        known_prefix = SIUnit[known_prefix.lower()]
    if isinstance(unknown_prefix, str):
        unknown_prefix = SIUnit[unknown_prefix.lower()]
    unknown_amount: float = known_amount * (
        10 ** (known_prefix.value - unknown_prefix.value)
    )
    return unknown_amount


def convert_binary_prefix(
    known_amount: float,
    known_prefix: str | BinaryUnit,
    unknown_prefix: str | BinaryUnit,
) -> float:
    """
    Wikipedia reference: https://en.wikipedia.org/wiki/Metric_prefix
    >>> convert_binary_prefix(1, BinaryUnit.giga, BinaryUnit.mega)
    1024
    >>> convert_binary_prefix(1, BinaryUnit.mega, BinaryUnit.giga)
    0.0009765625
    >>> convert_binary_prefix(1, BinaryUnit.kilo, BinaryUnit.kilo)
    1
    >>> convert_binary_prefix(1, 'giga', 'mega')
    1024
    >>> convert_binary_prefix(1, 'gIGa', 'mEGa')
    1024
    """
    if isinstance(known_prefix, str):
        known_prefix = BinaryUnit[known_prefix.lower()]
    if isinstance(unknown_prefix, str):
        unknown_prefix = BinaryUnit[unknown_prefix.lower()]
    unknown_amount: float = known_amount * (
        2 ** ((known_prefix.value - unknown_prefix.value) * 10)
    )
    return unknown_amount


if __name__ == "__main__":
    import doctest

    doctest.testmod()
