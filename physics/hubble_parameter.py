"""
Title : Calculating the Hubble Parameter

Description : The Hubble parameter H is the Universe expansion rate in any time.
In cosmology is costumary to use the redshift z in place of time, because
the redshift is directily mensure in the light of galaxies moving away
from us.

So, the general relation that we obtain is

H = H_0*(Omg_r*(z+1)**4 + Omg_m*(z+1)**3 + Omg_k*(z+1)**2 + Omg_l)**(1/2)

where Omg_r,l,m are the relativity (the percentage) energy densities that exist
in the Universe today. Here, Omg_m is the sum of the barion density and the
dark matter. Omg_k is the curvature parameter and can be written in termm
of the densities by the completness

Omg_k = 1 - (Omg_m + Omg_r + Omg_l)

Source :
https://www.sciencedirect.com/topics/mathematics/hubble-parameter
"""


def hubble_parameter(H_0: float, Omg_r: float, Omg_m: float, Omg_l: float, z: float):
    """
    Input Parameters
    ----------------
    H_0: Hubble constante is the expansion rate today, usually given in km/(s*Mpc)
    but here can be used in any unit that will works just need to change
    the returned unit

    Omg_r: relative radiation density today

    Omg_m: relative mass density today

    Omg_l: relative dark energy density today

    z: redshift

    Returns
    -------
    result : Hubble parameter in and the unit km/s/Mpc (the unit can be changed
             if you want)

    >>> hubble_parameter(H_0=63.3, Omg_r=1e-4, Omg_m=-0.3, Omg_l=0.7, z=1)
    ...
    ValueError: Any input parameter can be negative

     >>> hubble_parameter(H_0=63.3, Omg_r=1e-4, Omg_m= 1.2, Omg_l=0.7, z=1)
     ...
     ValueError: Relative densities cannot be greater than one
    """

    if z < 0 or Omg_m < 0 or Omg_r < 0 or Omg_l < 0:
        raise ValueError("Any input parameter can be negative")
    if Omg_m > 1 or Omg_r > 1 or Omg_l > 1:
        raise ValueError("Relative densities cannot be greater than one")
    else:
        Omg_k = 1 - (Omg_m + Omg_r + Omg_l)
        E2 = Omg_r * (z + 1) ** 4 + Omg_m * (z + 1) ** 3 + Omg_k * (z + 1) ** 2 + Omg_l
        H = H_0 * E2 ** (1 / 2)
        return "Hubble parameter: " + str(H) + " km/s/Mpc"


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()

    # demo LCDM aproximation
    Omg_m = 0.3

    print(hubble_parameter(H_0=68.3, Omg_r=1e-4, Omg_m=Omg_m, Omg_l=1 - Omg_m, z=0))
