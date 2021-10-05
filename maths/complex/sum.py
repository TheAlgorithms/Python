from complex import Complex


def complex_sum(a: Complex, b: Complex) -> Complex:
    """
    Add two complex numbers and return the result.
    >>> a = Complex(1, 2)
    >>> b = Complex(0, -1)
    >>> c = complex_sum(a, b)
    >>> c.__repr__()
    (1, 1)
    """
    return Complex(a.real_part + b.real_part, a.imaginary_part + b.imaginary_part)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
