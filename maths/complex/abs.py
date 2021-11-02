from math import sqrt

from complex import Complex


def complex_abs(complex_1: Complex) -> float:
    """
    Computes the absolute value of a complex number.
    The result is a non-negative real number, that represents the length
    of the vector (real_part, imaginary_part) in R².
    >>> complex_1 = Complex(-3, 4)
    >>> complex_abs(complex_1)
    5.0
    """
    return sqrt(complex_1.real_part ** 2 + complex_1.imaginary_part ** 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
