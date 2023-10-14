"""
https://en.wikipedia.org/wiki/Drift_velocity

Title: Calculating current using Drift Velocity
Description:
In physics, drift velocity is the average velocity attained by charged particles, such as electrons, in a material due to an electric field. In general, an electron in a conductor will propagate randomly at the Fermi velocity, resulting in an average velocity of zero. Applying an electric field adds to this random motion a small net flow in one direction; this is the drift.
Drift velocity of electrons
Drift velocity is proportional to current. In a resistive material, it is also proportional to the magnitude of an external electric field. Thus Ohm's law can be explained in terms of drift velocity.
"""


def compute_current(n: float, e: float, A: float, Vd: float) -> float:
    """
    n - charge carrier number density

    e - electronic charge

    A - Cross sectional area

    Vd - Drift velocity

    >>> compute_current(1, 1.602e-19, 1, 1)
    1.602e-19
    """
    i = n * e * A * Vd
    return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
