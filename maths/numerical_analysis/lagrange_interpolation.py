"""
Lagrange Interpolation

Given n+1 data points (x0, y0), (x1, y1), ..., (xn, yn) with distinct x-values,
the Lagrange interpolating polynomial is the unique polynomial of degree <= n that
passes through all given points.

For each i, the basis polynomial is:
    L_i(x) = product_{j != i} (x - x_j) / (x_i - x_j)

The interpolating polynomial is:
    P(x) = sum_i y_i * L_i(x)

Unlike Newton's forward-difference formula, Lagrange interpolation works for
arbitrarily spaced data points.

References:
    - https://en.wikipedia.org/wiki/Lagrange_polynomial
    - https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
"""

from __future__ import annotations


def lagrange_interpolation(x_points: list[float], y_points: list[float], x: float) -> float:
    """
    Estimate f(x) using the Lagrange interpolating polynomial through the
    given data points (x_points[i], y_points[i]).

    :param x_points: List of distinct x-coordinates of the data points.
    :param y_points: List of y-coordinates corresponding to x_points.
    :param x: The x-value at which to evaluate the interpolating polynomial.
    :return: The interpolated value P(x).
    :raises ValueError: If x_points and y_points have different lengths,
                        if fewer than 2 points are given, or if x_points
                        contains duplicate values.

    Examples — interpolating through known points of f(x) = x^2:
    >>> lagrange_interpolation([1, 2, 3], [1, 4, 9], 2.5)
    6.25
    >>> lagrange_interpolation([1, 2, 3], [1, 4, 9], 1.5)
    2.25
    >>> lagrange_interpolation([1, 2, 3], [1, 4, 9], 3.0)
    9.0

    Two-point linear interpolation:
    >>> lagrange_interpolation([0, 1], [0, 1], 0.5)
    0.5
    >>> lagrange_interpolation([0, 2], [0, 4], 1.0)
    2.0

    Four points from f(x) = x^3, interpolated at a non-grid point:
    >>> lagrange_interpolation([0, 1, 2, 3], [0, 1, 8, 27], 1.5)
    3.375

    Error cases:
    >>> lagrange_interpolation([1, 2], [1], 1.5)
    Traceback (most recent call last):
        ...
    ValueError: x_points and y_points must have the same length
    >>> lagrange_interpolation([1], [1], 1.0)
    Traceback (most recent call last):
        ...
    ValueError: at least 2 data points are required
    >>> lagrange_interpolation([1, 1, 3], [1, 2, 3], 2.0)
    Traceback (most recent call last):
        ...
    ValueError: x_points must be distinct (duplicate found: 1)
    """
    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length")
    n = len(x_points)
    if n < 2:
        raise ValueError("at least 2 data points are required")
    seen: set[float] = set()
    for val in x_points:
        if val in seen:
            raise ValueError(f"x_points must be distinct (duplicate found: {val})")
        seen.add(val)

    result = 0.0
    for i in range(n):
        basis = 1.0
        for j in range(n):
            if j != i:
                basis *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += y_points[i] * basis
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
