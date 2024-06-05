"""
Rainfall Intensity
==================
This module contains functions to calculate the intensity of
a rainfall event for a given duration and return period.
"""


def rainfall_intensity(
    k: float, a: float, b: float, c: float, tr: float, t: float
) -> float:
    """
    Calculate the intensity of a rainfall event for a given duration and return period.
    The coefficients K, a, b, and c are obtained from the Sherman
    intensity-duration-frequency curve for a specific location.

    Parameters
    ----------
    k : float
        Coefficient [adm].
    a : float
        Coefficient [adm].
    b : float
        Coefficient [adm].
    c : float
        Coefficient [adm].
    tr : float
        Return period in years.
    t : float
        Rainfall event duration in minutes.

    Returns
    -------
    intensity : float
        Intensity of the rainfall event in mm/h.

    References
    ----------
    - Aparicio, F. (1997): Fundamentos de Hidrología de Superficie.
        Balderas, México, Limusa. 303 p.
    - https://en.wikipedia.org/wiki/Intensity-duration-frequency_curve

    Examples
    --------

    >>> rainfall_intensity(1000, 0.2, 11.6, 0.81, 10, 60)
    49.83339231138578

    >>> rainfall_intensity(1000, 0.2, 11.6, 0.81, 10, 30)
    77.36319588106228

    >>> rainfall_intensity(1000, 0.2, 11.6, 0.81, 5, 60)
    43.382487747633625

    >>> rainfall_intensity(0, 0.2, 11.6, 0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, -0.2, 11.6, 0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0.2, -11.6, 0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0.2, 11.6, -0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0, 11.6, 0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0.2, 0, 0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0.2, 11.6, 0, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(0, 0.2, 11.6, 0.81, 10, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0.2, 11.6, 0.81, 0, 60)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    >>> rainfall_intensity(1000, 0.2, 11.6, 0.81, 10, 0)
    Traceback (most recent call last):
    ...
    ValueError: Please ensure that all parameters are positive.

    """
    if k <= 0 or a <= 0 or b <= 0 or c <= 0 or tr <= 0 or t <= 0:
        raise ValueError("Please ensure that all parameters are positive.")
    intensity = (k * (tr**a)) / ((t + b) ** c)
    return intensity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
