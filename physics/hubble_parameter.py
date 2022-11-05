"""
Title : Calculating the Hubble Parameter

Description : The Hubble parameter H is the Universe expansion rate
in any time. In cosmology is customary to use the redshift redshift
in place of time, becausethe redshift is directily mensure
in the light of galaxies moving away from us.

So, the general relation that we obtain is

H = hubble_constant*(radiation_density*(redshift+1)**4
                     + matter_density*(redshift+1)**3
                     + curvature*(redshift+1)**2 + dark_energy)**(1/2)

where radiation_density, matter_density, dark_energy are the relativity
(the percentage) energy densities that exist
in the Universe today. Here, matter_density is the
sum of the barion density and the
dark matter. Curvature is the curvature parameter and can be written in term
of the densities by the completeness


curvature = 1 - (matter_density + radiation_density + dark_energy)

Source :
https://www.sciencedirect.com/topics/mathematics/hubble-parameter
"""


def hubble_parameter(
    hubble_constant: float,
    radiation_density: float,
    matter_density: float,
    dark_energy: float,
    redshift: float,
) -> float:

    """
    Input Parameters
    ----------------
    hubble_constant: Hubble constante is the expansion rate today usually
    given in km/(s*Mpc)

    radiation_density: relative radiation density today

    matter_density: relative mass density today

    dark_energy: relative dark energy density today

    redshift: the light redshift

    Returns
    -------
    result : Hubble parameter in and the unit km/s/Mpc (the unit can be
    changed if you want, just need to change the unit of the Hubble constant)

    >>> hubble_parameter(hubble_constant=68.3, radiation_density=1e-4,
    ... matter_density=-0.3, dark_energy=0.7, redshift=1)
    Traceback (most recent call last):
    ...
    ValueError: All input parameters must be positive

    >>> hubble_parameter(hubble_constant=68.3, radiation_density=1e-4,
    ... matter_density= 1.2, dark_energy=0.7, redshift=1)
    Traceback (most recent call last):
    ...
    ValueError: Relative densities cannot be greater than one

    >>> hubble_parameter(hubble_constant=68.3, radiation_density=1e-4,
    ... matter_density= 0.3, dark_energy=0.7, redshift=0)
    68.3
    """
    parameters = [redshift, radiation_density, matter_density, dark_energy]
    if any(0 > p for p in parameters):
        raise ValueError("All input parameters must be positive")

    if any(1 < p for p in parameters[1:4]):
        raise ValueError("Relative densities cannot be greater than one")
    else:
        curvature = 1 - (matter_density + radiation_density + dark_energy)

        e_2 = (
            radiation_density * (redshift + 1) ** 4
            + matter_density * (redshift + 1) ** 3
            + curvature * (redshift + 1) ** 2
            + dark_energy
        )

        hubble = hubble_constant * e_2 ** (1 / 2)
        return hubble


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()

    # demo LCDM approximation
    matter_density = 0.3

    print(
        hubble_parameter(
            hubble_constant=68.3,
            radiation_density=1e-4,
            matter_density=matter_density,
            dark_energy=1 - matter_density,
            redshift=0,
        )
    )
