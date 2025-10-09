# https://byjus.com/equivalent-resistance-formula/

from __future__ import annotations


def resistor_parallel(resistors: list[float]) -> float:
    """
    Req = 1/ (1/R1 + 1/R2 + ... + 1/Rn)

    >>> resistor_parallel([3.21389, 2, 3])
    0.8737571620498019
    >>> resistor_parallel([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative or zero value!
    >>> resistor_parallel([3.21389, 2, 0.000])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative or zero value!
    """

    first_sum = 0.00
    for index, resistor in enumerate(resistors):
        if resistor <= 0:
            msg = f"Resistor at index {index} has a negative or zero value!"
            raise ValueError(msg)
        first_sum += 1 / float(resistor)
    return 1 / first_sum


def resistor_series(resistors: list[float]) -> float:
    """
    Req = R1 + R2 + ... + Rn

    Calculate the equivalent resistance for any number of resistors in parallel.

    >>> resistor_series([3.21389, 2, 3])
    8.21389
    >>> resistor_series([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative value!
    """
    sum_r = 0.00
    for index, resistor in enumerate(resistors):
        sum_r += resistor
        if resistor < 0:
            msg = f"Resistor at index {index} has a negative value!"
            raise ValueError(msg)
    return sum_r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
