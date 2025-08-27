"""
The root-mean-square speed is essential in measuring the average speed of particles
contained in a gas, defined as,
 -----------------
 | Vrms = √3RT/M |
 -----------------

In Kinetic Molecular Theory, gasified particles are in a condition of constant random
motion; each particle moves at a completely different pace, perpetually clashing and
changing directions consistently velocity is used to describe the movement of gas
particles, thereby taking into account both speed and direction. Although the velocity
of gaseous particles is constantly changing, the distribution of velocities does not
change.
We cannot gauge the velocity of every individual particle, thus we frequently reason
in terms of the particles average behavior. Particles moving in opposite directions
have velocities of opposite signs. Since gas particles are in random motion, it's
plausible that there'll be about as several moving in one direction as within the other
way, which means that the average velocity for a collection of gas particles equals
zero; as this value is unhelpful, the average of velocities can be determined using an
alternative method.
"""

UNIVERSAL_GAS_CONSTANT = 8.3144598


def rms_speed_of_molecule(temperature: float, molar_mass: float) -> float:
    """
    >>> rms_speed_of_molecule(100, 2)
    35.315279554323226
    >>> rms_speed_of_molecule(273, 12)
    23.821458421977443
    """
    if temperature < 0:
        raise Exception("Temperature cannot be less than 0 K")
    if molar_mass <= 0:
        raise Exception("Molar mass cannot be less than or equal to 0 kg/mol")
    else:
        return (3 * UNIVERSAL_GAS_CONSTANT * temperature / molar_mass) ** 0.5


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()

    # example
    temperature = 300
    molar_mass = 28
    vrms = rms_speed_of_molecule(temperature, molar_mass)
    print(f"Vrms of Nitrogen gas at 300 K is {vrms} m/s")
