from complex import Complex


def complex_mul(a: Complex, b: Complex) -> Complex:
    """
    Multiplicate two complex numbers and return the result.
    >>> a = Complex(0, 1)
    >>> b = Complex(0, 1)
    >>> c = complex_mul(a, b)
    >>> c.__repr__()
    (-1, 0)
    """
    return Complex(
        a.real_part * b.real_part - a.imaginary_part * b.imaginary_part,
        a.real_part * b.imaginary_part + b.real_part * a.imaginary_part,
    )
