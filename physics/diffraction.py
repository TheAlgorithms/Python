import math


def check_min_intensity(
    slit_width: float = 1.0, diff_angle: float = 0.0, wavelength: float = 100.0
) -> bool:
    """
    Checks for the condition of minimum intensity in a diffraction pattern.

    Args:
        slit_width (float): The width of the slit in millimeters.
        diff_angle (float): The diffraction angle in radians.
        wavelength (float): The wavelength of light in nanometers.

    Returns:
        bool: True if minimum intensity is met, otherwise False.

    >>> check_min_intensity(4, 0.25, 300)
    False
    >>> check_min_intensity(1, 0.0001, 100)
    True
    """
    wavelength *= 10**-6
    n_val = round(slit_width * (diff_angle) / wavelength, 5)
    r_val = n_val - math.floor(n_val) == 0
    return r_val


def check_max_intensity(
    slit_width: float = 1.0, diff_angle: float = 0.0, wavelength: float = 100.0
) -> bool:
    """
    Checks for the condition of maximum intensity in a diffraction pattern.

    Args:
        slit_width (float): The width of the slit in millimeters.
        diff_angle (float): The diffraction angle in radians.
        wavelength (float): The wavelength of light in nanometers.

    Returns:
        bool: True if maximum intensity is met, otherwise False.

    >>> check_max_intensity(1, 0.001, 100)
    False
    >>> check_max_intensity(1, 0.00005, 100)
    True
    """
    wavelength *= 10**-6
    n_val = round(((2 * slit_width * diff_angle) - wavelength) / (2 * wavelength), 4)
    r_val = n_val - math.floor(n_val) == 0
    return r_val


def intensity_single_slit(
    slit_width: float = 1.0, diff_angle: float = 0.0, wavelength: float = 100.0
) -> str:
    """
    Computes the intensity for a single slit diffraction pattern.

    Args:
        slit_width (float): The width of the slit in millimeters.
        diff_angle (float): The diffraction angle in radians.
        wavelength (float): The wavelength of light in nanometers.

    Returns:
        str: The intensity of the diffraction pattern.

    >>> intensity_single_slit(1, 0.0005, 100)
    '0.9999999999177533 I0'
    """
    beta = math.pi * slit_width * (math.sin(diff_angle) / wavelength)
    i_coeff = (math.sin(beta) / beta) ** 2
    return f"{i_coeff} I0"


def intensity_double_slit(path_diff: int = 0, intensity_max: str | float = "I0") -> str:
    """
    Computes the intensity for a double slit diffraction pattern.

    Args:
        path_diff (float): The path difference in the two waves.
        intensity_max (str or int): The maximum intensity.

    Returns:
        str or float: The intensity of the diffraction pattern.

    >>> intensity_double_slit(0, 1)
    '4.0'
    >>> intensity_double_slit(0.001, 1)
    '3.999999000000084'
    >>> intensity_double_slit(0)
    '4.0 I0'
    """
    r_val = (
        str(4 * intensity_max * (math.cos(path_diff / 2)) ** 2)
        if (type(intensity_max) is float or type(intensity_max) is int)
        else f"{4*(math.cos(path_diff/2)**2)} I0"
    )
    return r_val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # pass
