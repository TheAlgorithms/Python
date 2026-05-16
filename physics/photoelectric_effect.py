"""
The photoelectric effect is the emission of electrons when electromagnetic radiation ,
such as light, hits a material. Electrons emitted in this manner are called
photoelectrons.

In 1905, Einstein proposed a theory of the photoelectric effect using a concept that
light consists of tiny packets of energy known as photons or light quanta. Each packet
carries energy hv that is proportional to the frequency v of the corresponding
electromagnetic wave. The proportionality constant h has become known as the
Planck constant. In the range of kinetic energies of the electrons that are removed from
their varying atomic bindings by the absorption of a photon of energy hv, the highest
kinetic energy K_max is :

K_max = hv-W

Here, W is the minimum energy required to remove an electron from the surface of the
material. It is called the work function of the surface

Reference: https://en.wikipedia.org/wiki/Photoelectric_effect

"""

PLANCK_CONSTANT_JS = 6.6261 * pow(10, -34)  # in SI (Js)
PLANCK_CONSTANT_EVS = 4.1357 * pow(10, -15)  # in eVs


def maximum_kinetic_energy(
    frequency: float, work_function: float, in_ev: bool = False
) -> float:
    """
    Calculates the maximum kinetic energy of emitted electron from the surface.
    if the maximum kinetic energy is zero then no electron will be emitted
    or given electromagnetic wave frequency is small.

    frequency (float): Frequency of electromagnetic wave.
    work_function (float): Work function of the surface.
    in_ev (optional)(bool): Pass True if values are in eV.

    Usage example:
    >>> maximum_kinetic_energy(1000000,2)
    0
    >>> maximum_kinetic_energy(1000000,2,True)
    0
    >>> maximum_kinetic_energy(10000000000000000,2,True)
    39.357000000000006
    >>> maximum_kinetic_energy(-9,20)
    Traceback (most recent call last):
        ...
    ValueError: Frequency can't be negative.

    >>> maximum_kinetic_energy(1000,"a")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'float' and 'str'

    """
    if frequency < 0:
        raise ValueError("Frequency can't be negative.")
    if in_ev:
        return max(PLANCK_CONSTANT_EVS * frequency - work_function, 0)
    return max(PLANCK_CONSTANT_JS * frequency - work_function, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
