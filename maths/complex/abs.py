from math import sqrt

from complex import Complex


def complex_abs(c: Complex) -> float:
    """
    Computes the absolute value of a complex number.
    The result is a non-negative real number, that represents the lenght
    of the vector (real_part, imaginary_part) in R².
    >>> c = Complex(-3, 4)
    >>> complex_abs(c)
    5.0
    """
    return sqrt(c.real_part ** 2 + c.imaginary_part ** 2)
