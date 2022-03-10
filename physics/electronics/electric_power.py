# https://en.m.wikipedia.org/wiki/Electric_power
from __future__ import annotations

from collections import namedtuple


def electric_power(voltage: float, current: float, power: float) -> tuple:
    """
    This function can calculate any one of the three (voltage, current, power),
    fundamental value of electrical system.
    examples are below:
    >>> electric_power(voltage=0, current=2, power=5)
    result(name='voltage', value=2.5)
    >>> electric_power(voltage=2, current=2, power=0)
    result(name='power', value=4.0)
    >>> electric_power(voltage=-2, current=3, power=0)
    result(name='power', value=6.0)
    >>> electric_power(voltage=2, current=4, power=2)
    Traceback (most recent call last):
        File "<stdin>", line 15, in <module>
    ValueError: Only one argument must be 0
    >>> electric_power(voltage=0, current=0, power=2)
    Traceback (most recent call last):
        File "<stdin>", line 19, in <module>
    ValueError: Only one argument must be 0
    >>> electric_power(voltage=0, current=2, power=-4)
    Traceback (most recent call last):
        File "<stdin>", line 23, in <modulei
    ValueError: Power cannot be negative in any electrical/electronics system
    >>> electric_power(voltage=2.2, current=2.2, power=0)
    result(name='power', value=4.84)
    """
    result = namedtuple("result", "name value")
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Only one argument must be 0")
    elif power < 0:
        raise ValueError(
            "Power cannot be negative in any electrical/electronics system"
        )
    elif voltage == 0:
        return result("voltage", power / current)
    elif current == 0:
        return result("current", power / voltage)
    elif power == 0:
        return result("power", float(round(abs(voltage * current), 2)))
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
