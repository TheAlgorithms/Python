from typing import Sequence


def evaluate_poly(poly: Sequence[float], x: float) -> float:
    """Evaluate a polynomial f(x) at specified point x and return the value.

    Arguments:
    poly -- the coefficients of a polynomial as an iterable in order of
            ascending degree
    x -- the point at which to evaluate the polynomial

    >>> evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), 10.0)
    79800.0
    """
    return sum(c * (x ** i) for i, c in enumerate(poly))


def horner(poly: Sequence[float], x: float) -> float:
    """Evaluate a polynomial at specified point using Horner's method.

    In terms of computational complexity, Horner's method is an efficient method
    of evaluating a polynomial. It avoids the use of expensive exponentiation,
    and instead uses only multiplication and addition to evaluate the polynomial
    in O(n), where n is the degree of the polynomial.

    https://en.wikipedia.org/wiki/Horner's_method

    Arguments:
    poly -- the coefficients of a polynomial as an iterable in order of
            ascending degree
    x -- the point at which to evaluate the polynomial

    >>> horner((0.0, 0.0, 5.0, 9.3, 7.0), 10.0)
    79800.0
    """
    result = 0.0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result


if __name__ == "__main__":
    """
    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)  # f(x) = 7.0x^4 + 9.3x^3 + 5.0x^2
    >>> x = -13.0
    >>> # f(-13) = 7.0(-13)^4 + 9.3(-13)^3 + 5.0(-13)^2 = 180339.9
    >>> print(evaluate_poly(poly, x))
    180339.9
    """
    poly = (0.0, 0.0, 5.0, 9.3, 7.0)
    x = 10.0
    print(evaluate_poly(poly, x))
    print(horner(poly, x))
