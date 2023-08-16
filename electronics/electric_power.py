# https://en.m.wikipedia.org/wiki/Electric_power
from __future__ import annotations

from typing import NamedTuple


class Result(NamedTuple):
    name: str
    value: float


def electric_power(voltage: float, current: float, power: float) -> tuple:
    """
    This function can calculate any one of the three (voltage, current, power),
    fundamental value of electrical system.
    examples are below:
    >>> electric_power(voltage=0, current=2, power=5)
    Result(name='voltage', value=2.5)
    >>> electric_power(voltage=2, current=2, power=0)
    Result(name='power', value=4.0)
    >>> electric_power(voltage=-2, current=3, power=0)
    Result(name='power', value=6.0)
    >>> electric_power(voltage=2, current=4, power=2)
    Traceback (most recent call last):
        ...
    ValueError: Only one argument must be 0
    >>> electric_power(voltage=0, current=0, power=2)
    Traceback (most recent call last):
        ...
    ValueError: Only one argument must be 0
    >>> electric_power(voltage=0, current=2, power=-4)
    Traceback (most recent call last):
        ...
    ValueError: Power cannot be negative in any electrical/electronics system
    >>> electric_power(voltage=2.2, current=2.2, power=0)
    Result(name='power', value=4.84)
    """
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Only one argument must be 0")
    elif power < 0:
        raise ValueError(
            "Power cannot be negative in any electrical/electronics system"
        )
    elif voltage == 0:
        return Result("voltage", power / current)
    elif current == 0:
        return Result("current", power / voltage)
    elif power == 0:
        return Result("power", float(round(abs(voltage * current), 2)))
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
