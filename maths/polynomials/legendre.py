# Imports de bibliothèques standard
from math import factorial

# Imports de bibliothèques tierces
import pytest
from numpy.polynomial import Polynomial


def legendre(n: int) -> [float]:
    """
    Compute the coefficients of the nth Legendre polynomial.

    The Legendre polynomials are solutions to Legendre's differential equation
    and are widely used in physics and engineering.

    Parameters:
        n (int): The order of the Legendre polynomial.

    Returns:
        list[float]: Coefficients of the polynomial in ascending order of powers.
    """
    legendre_polynomial = (1 / (factorial(n) * (2**n))) * (Polynomial([-1, 0, 1]) ** n)
    return legendre_polynomial.deriv(n).coef.tolist()


def test_legendre_0():
    """Test the 0th Legendre polynomial."""
    assert legendre(0) == [1.0], "The 0th Legendre polynomial should be [1.0]"


def test_legendre_1():
    """Test the 1st Legendre polynomial."""
    assert legendre(1) == [0.0, 1.0], "The 1st Legendre polynomial should be [0.0, 1.0]"


def test_legendre_2():
    """Test the 2nd Legendre polynomial."""
    assert legendre(2) == [
        -0.5,
        0.0,
        1.5,
    ], "The 2nd Legendre polynomial should be [-0.5, 0.0, 1.5]"


def test_legendre_3():
    """Test the 3rd Legendre polynomial."""
    assert legendre(3) == [
        0.0,
        -1.5,
        0.0,
        2.5,
    ], "The 3rd Legendre polynomial should be [0.0, -1.5, 0.0, 2.5]"


def test_legendre_4():
    """Test the 4th Legendre polynomial."""
    assert legendre(4) == pytest.approx([0.375, 0.0, -3.75, 0.0, 4.375])
    "The 4th Legendre polynomial should be [0.375, 0.0, -3.75, 0.0, 4.375]"


if __name__ == "__main__":
    pytest.main()
