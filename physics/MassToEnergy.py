# The speed of light

c = 299792458

# Mass ---> Energy
def get_energy(mass: float) -> float:

    # E = MC^2
    return mass * c ** 2


# Energy ---> Mass
def get_mass(energy: float) -> float:
    # M = E/C^2
    return energy / c ** 2

# Read More: https://en.wikipedia.org/wiki/Mass–energy_equivalence
