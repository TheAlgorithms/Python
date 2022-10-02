#https://en.wikipedia.org/wiki/Magnetic_circuit#Hopkinson's_law
from __future__ import annotations
def hopkinsons_law(magnetomotive_force:float, current:float, reluctance:float) -> dict[str, float]:
    """
    Apply Hopkinson's Law, on any two given electrical values, which can be magnetomotive force, current,
    and reluctance, and then in a Python dict return name/value pair of the zero value.

    >>> hopkinsons_law(magnetomotive_force=10, reluctance=5, current=0)
    {'current': 2.0}
    >>> hopkinsons_law(magnetomotive_force=0, current=0, reluctance=10)
    Traceback (most recent call last):
      ...
    ValueError: One and only one argument must be 0
    >>> hopkinsons_law(magnetomotive_force=0, current=1, reluctance=-2)
    Traceback (most recent call last):
      ...
    ValueError: Reluctance cannot be negative
    >>> hopkinsons_law(reluctance=0, magnetomotive_force=-10, current=1)
    {'reluctance': -10.0}
    >>> hopkinsons_law(magnetomotive_force=0, current=-1.5, reluctance=2)
    {'magnetomotive_force': -3.0}
    """
    if (magnetomotive_force, current, reluctance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if reluctance < 0:
        raise ValueError("Reluctance cannot be negative")
    if magnetomotive_force == 0:
        return {"magnetomotive_force": float(current * reluctance)}
    elif current == 0:
        return {"current": magnetomotive_force / reluctance}
    elif reluctance == 0:
        return {"reluctance": magnetomotive_force / current}
    else:
        raise ValueError("Exactly one argument must be 0")

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()        