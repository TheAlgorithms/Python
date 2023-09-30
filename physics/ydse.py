def calculateFW(lambda1: float, d: float, D: float):
    """
    This method calculates the value of the fringe width obtained during Young's Double Slit Experiment
    This is calculated by providing three values to the function: The value of wavelength lambda, the value of distance of slit from the screen D, the value of width of slits d

    Example 1 : Wavelength -> 589.3nm, d -> 3mm, D -> 1m
    Example 2 : Wavelength -> 696nm, d -> 5mm, D -> 2m

    >>> calculateFW(lamda1=5.93*10**-7, d=3*10**-3, D=1)
    1.779e-09
    >>> calculateFW(lamda1=6.96*10**-7, d=5*10**-3, D=2)
    1.74e-09


    """
    if lambda1 < 0:
        raise ValueError("Wavelength cannot be negative")
    if d < 0 or D < 0:
        raise ValueError("Distances cannot be negative")

    fringe = (lambda1 * d) / D
    return fringe


if __name__ == "__main__":
    import doctest

    doctest.testmod()
