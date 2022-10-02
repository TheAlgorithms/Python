# https://en.wikipedia.org/wiki/Mechanical_energy


def calculate_gravitational_potential_energy(
    mass: float, gravity: float, height: float
) -> str:
    """
    Gravitational Potential Energy Is The Energy
    An Object Possesses Due To Its State Of Rest
    At A Height. The Kinetic Energy Applied To
    Transport a body to that particular state
    of rest is converted into potential energy
    and stored in the body, hence potential and
    kinetic energies are related.

    >>> calculate_gravitational_potential_energy(15,9.8,10)
    '1470.0 joules'
    >>> calculate_gravitational_potential_energy(1e100,1e100,1e100)
    '1e+300 joules'
    >>> calculate_gravitational_potential_energy(15.5,9.8,25.5)
    '3873.4500000000003 joules'
    """
    unit = "joules"

    try:
        gravitational_potential_energy = mass * gravity * height
    except Exception:
        return -0.0

    gravitational_potential_energy = str(gravitational_potential_energy)
    gravitational_potential_energy += " " + unit
    return gravitational_potential_energy


def calculate_kinetic_energy(mass: float, velocity: float) -> str:
    """
     Kinetic Energy is the energy a body possesses due
     to its state of motion. The Potential Energy applied
     on a body to change its state from motion to rest
     converts into kinetic energy, thus kinetic and potential
     energies are related.

    >>> calculate_kinetic_energy(10,20)
    '2000.0 joules'
    >>> calculate_kinetic_energy(10,40)
    '8000.0 joules'
    >>> calculate_kinetic_energy(4.25,18.9)
    '759.0712499999998 joules'
    """
    unit = "joules"

    try:
        kinetic_energy = 0.5 * mass * velocity * velocity
    except Exception:
        return -0.0

    kinetic_energy = str(kinetic_energy)
    kinetic_energy += " " + unit
    return kinetic_energy


if __name__ == "__main__":
    import doctest

    doctest.testmod()
