import math


def bragg_angle(distance: float, order: int, wavelength: float) -> float:
    """
    Calculate the Bragg diffraction angle using the formula:
    sin(θ) = (n * λ) / (2 * d)

    Parameters:
    distance d (float): Distance between crystal planes (in meters).
    order n (int): Order of reflection.
    wavelength λ (float): Wavelength of the radiation (in meters).

    Examples:
    >>> bragg_angle(2.2e-10, 1, 2.2e-10)
    30.0

    >>> bragg_angle(5e-10, 2, 1e-10)
    11.5

    >>> bragg_angle(4e-10, 1, 4e-10)
    30.0

    # Test case for an invalid sine value (out of range)
    >>> bragg_angle(1e-10, 2, 3e-10)
    Traceback (most recent call last):
        ...
    ValueError: The calculated sine value is out of the valid range.
    """
    sine_theta = (order * wavelength) / (2 * distance)
    if sine_theta > 1 or sine_theta < -1:
        raise ValueError("The calculated sine value is out of the valid range.")
    theta_radians = math.asin(sine_theta)
    theta_degrees = math.degrees(theta_radians)
    return round(theta_degrees, 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
