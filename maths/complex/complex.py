"""
Complex number implementation.

Definition:
    A complex number is an ordered pair of real numbers (a, b). The first
    component, a, is called the real part; the second component, b, is called
    the imaginary part.
"""


class Complex:
    def __init__(self, real_part: float, imaginary_part: float) -> None:
        """
        Both a and b are real numbers (float in Python).
        """
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __repr__(self) -> str:
        """
        Represent the complex number as a 2-tuple.
        >>> complex_1 = Complex(1, 2)
        >>> complex_1.__repr__()
        (1, 2)
        """
        return (self.real_part, self.imaginary_part)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
