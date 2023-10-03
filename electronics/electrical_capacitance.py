# http://labman.phys.utk.edu/phys222core/modules/m2/capacitors.html

"""
Description:- The capacitance tells us how much charge the electronic device
stores for a given voltage.
"""


from __future__ import annotations


def electrical_capacitance(voltage: float, charge: float, capacitance: float) -> dict[str, float]:
    """
    Apply Capacitance formula , on any two given electrical values, which can be voltage, charge,
    or capacitance, and then in a Python dict return name/value pair of the zero value.

    >>> electrical_capacitance(voltage=10, capacitance=5, charge=0)
    {'charge': 50.0}
    >>> electrical_capacitance(voltage=0, capacitance=0, charge=10)
    Traceback (most recent call last):
      ...
    ValueError: One and only one argument must be 0
    >>> electrical_capacitance(voltage=0, capacitance=-1, charge=-2)
    Traceback (most recent call last):
      ...
    ValueError: Capacitance cannot be negative
    >>> electrical_capacitance(capacitance=0, voltage=-10, charge=-1)
    {'capacitance': 0.1}
    >>> electrical_capacitance(voltage=0, charge=-1.5, capacitance=2)
    {'voltage': -0.75}
    """
    if (voltage, charge, capacitance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if capacitance < 0:
        raise ValueError("Capacitance cannot be negative")
    if voltage == 0:
        return {"voltage": charge / capacitance}
    elif charge == 0:
        return {"charge": float(capacitance * voltage)}
    elif capacitance == 0:
        return {"capacitance": charge / voltage}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
