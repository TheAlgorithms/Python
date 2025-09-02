"""
@author: MatteoRaso
"""

from collections.abc import Callable
from math import pi, sqrt
from random import uniform
from statistics import mean


def is_in_unit_circle(x: float, y: float) -> bool:
    """
    Checks whether the point (x, y) lies inside or on the boundary
    of a unit circle centered at the origin.

    >>> is_in_unit_circle(0.0, 0.0)
    True
    >>> is_in_unit_circle(1.0, 0.0)
    True
    >>> is_in_unit_circle(1.0, 1.0)
    False
    """
    return sqrt(x**2 + y**2) <= 1


def pi_estimator(iterations: int) -> float:
    """
    Estimate the value of pi using the Monte Carlo method.

    The method simulates random points in the square and checks how
    many fall within the inscribed unit circle.

    Intuition:
    1. Draw a 2x2 square centred at (0,0).
    2. Inscribe a unit circle within the square.
    3. For each iteration, place a dot randomly within the square.
    4. Divide the number of dots within the circle by the total number of dots.
    5. Multiply this ratio by 4 to estimate pi.

    Args:
        iterations: Number of random points to generate.

    Returns:
        Estimated value of pi.

    >>> round(pi_estimator(100000), 2) in [3.13, 3.14, 3.15]
    True
    """

    if iterations <= 0:
        raise ValueError("Number of iterations must be positive")

    inside_circle = sum(
        is_in_unit_circle(uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for _ in range(iterations)
    )
    return (inside_circle / iterations) * 4


def area_under_curve_estimator(
    iterations: int,
    function_to_integrate: Callable[[float], float],
    min_value: float = 0.0,
    max_value: float = 1.0,
) -> float:
    """
    Estimate the definite integral of a continuous, non-negative function f(x)
    over a bounded interval [min_value, max_value] using the Monte Carlo method.

    Intuition:
    1. Randomly sample x values uniformly from [min_value, max_value].
    2. Compute the average of f(x) at the sample points.
       This estimates the expected value of f(x).
    3. Multiply this average by the interval width to estimate the integral.

    Args:
        iterations: Number of random samples to draw.
        function_to_integrate: A function f(x) to integrate over [min_value, max_value].
        min_value: Lower bound of the interval.
        max value: Upper bound of the interval.

    Returns:
        Estimated area under the curve (integral of f from min_value to max_value).

    Raises:
        ValueError: If iterations <= 0 or min_value >= max_value.

    Example:
    >>> def f(x): return x
    >>> round(area_under_curve_estimator(100000, f), 2) in [0.49, 0.5, 0.51]
    True
    """
    if iterations <= 0:
        raise ValueError("Number of iterations must be positive")
    if min_value >= max_value:
        raise ValueError("min_value must be less than max_value")

    samples = (
        function_to_integrate(uniform(min_value, max_value)) for _ in range(iterations)
    )
    return mean(samples) * (max_value - min_value)


def area_under_line_estimator_check(
    iterations: int, min_value: float = 0.0, max_value: float = 1.0
) -> tuple[float, float, float]:
    """
    Demonstrate the Monte Carlo integration method by estimating
    the area under the line y = x over [min_value, max_value].

    The exact integral of f(x) = x over [a, b] is:
        (b**2 - a**2) / 2

    This helps illustrate that the Monte Carlo method produces
    a reasonable estimate for a simple, well-understood function.

    Args:
        iterations: Number of samples to use in estimation.
        min_value: Lower bound of the integration interval.
        max_value: Upper bound of the integration interval.

    Returns:
        A tuple of (estimated_value, expected_value, absolute_error).

    >>> result = area_under_line_estimator_check(100000)
    >>> round(result[0], 2) in [0.49, 0.5, 0.51]
    True
    """

    def identity_function(x: float) -> float:
        return x

    estimated_value = area_under_curve_estimator(
        iterations, identity_function, min_value, max_value
    )
    expected_value = (max_value**2 - min_value**2) / 2
    error = abs(estimated_value - expected_value)
    return estimated_value, expected_value, error


def pi_estimator_using_area_under_curve(iterations: int) -> tuple[float, float, float]:
    """
    Estimate the value of pi using Monte Carlo integration.

    The area under the curve y = sqrt(4 - x**2) from x = 0 to 2 is equal to pi.
    This function uses that fact to estimate pi.

    Args:
        iterations: Number of random samples to use for estimation.

    Returns:
        A tuple of (estimated_value, expected_value, absolute_error).

    >>> result = pi_estimator_using_area_under_curve(100000)
    >>> round(result[0], 2) in [3.13, 3.14, 3.15]
    True
    """

    def semicircle_function(x: float) -> float:
        """
        Represents semi-circle with radius 2
        >>> [semicircle_function(x) for x in [-2.0, 0.0, 2.0]]
        [0.0, 2.0, 0.0]
        """
        return sqrt(4.0 - x * x)

    estimated_value = area_under_curve_estimator(
        iterations, semicircle_function, 0.0, 2.0
    )
    expected_value = pi
    error = abs(estimated_value - expected_value)

    return estimated_value, expected_value, error
