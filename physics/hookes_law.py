"""
Hooke's Law states that the force needed to extend or compress a spring
is proportional to the distance of that extension or compression.

    F = -k * x

Where:
    F = Force applied (in Newtons)
    k = Spring constant (in Newtons per meter, N/m)
    x = Displacement from equilibrium (in meters)

The negative sign indicates the force is a restoring force (opposite to displacement).

Reference: https://en.wikipedia.org/wiki/Hooke%27s_law
"""


def hookes_law(spring_constant: float, displacement: float) -> float:
    """
    Calculate the restoring force of a spring using Hooke's Law.

    Parameters:
        spring_constant: stiffness of the spring in N/m (must be positive)
        displacement: extension or compression in meters

    Returns:
        Restoring force in Newtons (negative means opposing displacement)

    >>> hookes_law(spring_constant=50, displacement=0.1)
    -5.0
    >>> hookes_law(spring_constant=100, displacement=0.5)
    -50.0
    >>> hookes_law(spring_constant=200, displacement=-0.2)
    40.0
    >>> hookes_law(spring_constant=0, displacement=0.1)
    Traceback (most recent call last):
        ...
    ValueError: Spring constant must be positive.
    >>> hookes_law(spring_constant=-10, displacement=0.1)
    Traceback (most recent call last):
        ...
    ValueError: Spring constant must be positive.
    """
    if spring_constant <= 0:
        raise ValueError("Spring constant must be positive.")
    return -spring_constant * displacement


if __name__ == "__main__":
    import doctest

    doctest.testmod()
