"""
    Calculate the power radiated by a black body using the Stefan-Boltzmann law.

    Args:
        surface_area (float): Surface area of the black body (in square meters).
        temperature (float): Absolute temperature of the black body (in kelvins).

    Returns:
        float: Power radiated by the black body (in watts).

    Equation:
    P = σ * A * T^4

    P: Power radiated
    σ: Stefan-Boltzmann constant (5.67e-8 W/m^2·K^4)
    A: Surface area
    T: Absolute temperature (in kelvins)

    Source:
    https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law
"""


def stefan_boltzmann_law(surface_area: float, temperature: float) -> float:
    """
    >>> stefan_boltzmann_law(1.0, 5778)
    63196526.546029195
    >>> stefan_boltzmann_law(0.5, 300)
    229.635
    >>> stefan_boltzmann_law(10, 1000)
    567000.0
    """
    # Stefan-Boltzmann constant
    sigma = 5.67e-8  # W/m^2·K^4

    # Calculate the power radiated
    power = sigma * surface_area * (temperature**4)

    return power


if __name__ == "__main__":
    import doctest

    doctest.testmod()
