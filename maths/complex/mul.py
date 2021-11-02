from complex import Complex


def complex_mul(complex_1: Complex, complex_2: Complex) -> Complex:
    """
    Multiplicate two complex numbers and return the result.
    >>> complex_1 = Complex(0, 1)
    >>> complex_2 = Complex(0, 1)
    >>> c = complex_mul(complex_1, complex_2)
    >>> c.__repr__()
    (-1, 0)
    """
    return Complex(
        complex_1.real_part * complex_2.real_part
        - complex_1.imaginary_part * complex_2.imaginary_part,
        complex_1.real_part * complex_2.imaginary_part
        + complex_2.real_part * complex_1.imaginary_part,
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
