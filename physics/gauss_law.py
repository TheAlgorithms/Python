# https://byjus.com/jee/gauss-law/

from __future__ import annotations

# Permittivity of free space -> units = C^2 / (N * m^2)
ε0 = 8.8541878128E-12 


def gauss_law(electric_field: float = 0, area: float = 0, charge: float = 0, res : str = "Flux") -> float:

    """
    Gauss law states that the flux through a closed surface (e.g. sphere)
    is equal to the electric charge within this shape divided by an electric constant (ε0).
    Formula: 
             q
    E * S = ---- 
             ε0

    Where E is an Electric Field flowing thorugh the surface S, and q is the total charge
    within the closed surface.

    References
    ----------
    https://byjus.com/jee/gauss-law/
    https://courses.lumenlearning.com/boundless-physics/chapter/electric-flux-and-gausss-law/


    Parameters
    ----------
    electric_field : float units N / C

    area : float units m^2

    charge : float with units in Coulombs

    res : str with options: Field, Flux, Charge. 

    Returns
    -------
    Returned value depends on the value of res:

    Flux --> flow of electric field through surface (units: N * m^2 * C^−1).

    Field --> Electric Field at a point in which the area was calculated.
              The area should be of an enclosed shape and could be virtual (no need for a physical object).
              The units of the electric field are: N / C

    Charge --> The total charge within an enclosed surface having flux that is equal to electric_field * area. 
               Units: C (Columb)

    >>> gauss_law(electric_field = 10, area = 3, res = "Charge")
    2.6562563438400003e-10

    >>> gauss_law(charge = 18e-9, res = "Flux")
    2032.9363212714343

    >>> gauss_law(area = 10, charge = 18e-9, res = "Field")
    203.2936321271434

    >>> gauss_law()
    Traceback (most recent call last):
      ...
    ValueError: One or more arguments are missing!

    >>> gauss_law(area = 10, res= "Field")
    Traceback (most recent call last):
      ...
    ValueError: One or more arguments are missing!
    """
    if res == "Flux":
        if abs(charge) > 0:
            return charge / ε0
        elif electric_field > 0 and area > 0:
            return electric_field * area
    elif res == "Field":
        if abs(charge) > 0 and area > 0:
            return charge / (ε0 * area)
    elif res == "Charge":
        if electric_field > 0 and area > 0:
            return electric_field * area * ε0

    raise ValueError("One or more arguments are missing!")



if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
