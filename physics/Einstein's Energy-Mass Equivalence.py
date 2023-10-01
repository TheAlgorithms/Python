"""
Title : Calculate Einstein's Energy-Mass Equivalence

Description :
    The below mentioned code gives Einstein's mass-energy equivalence, expressed by the famous equation E=mc^2
    states that energy (E) and mass (m) are interchangeable.
    It means that a certain amount of mass can be converted into an equivalent amount of energy, and vice versa, under the right conditions.
    This concept revolutionized our understanding of the fundamental relationship between matter and energy in the universe.

"""


def energy_equivalence(mass):
    """
    The most famous equation in the world, E=mc2, arrived rather quietly.
    In 1905, Einstein published two articles on the Special Theory of Relativity

    E=Energy  units:joule
    M=mass    units:kilograms
    c=speed of light  units:meter per second


    """
    c = 299792458

    E = mass * c**2
    return E
