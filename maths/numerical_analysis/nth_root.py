"""
Approximate the nth root of a real number using the Newton's Method.

The nth root of a real number R can be computed with Newton's method,
which starts with an initial guess x_0 and then iterates using the
recurrence relation:

x_{k + 1} = x_k - ((x_k)**n - R)/(n*(x_k)**(n-1))

The recurrence relation can be rewritten for computational efficiency:

x_{k + 1} = (n-1)/n*x_k + R/(n*(x_k)**(n-1))

Given a tolerance TOL, a stopping criterion can be set as:

abs(x_{k + 1} - x_k) < TOL

References:
- https://en.wikipedia.org/wiki/Nth_root#Using_Newton's_method
- Sauer, T. (2011): Numerical analysis.
    USA. Addison-Wesley Publishing Company.
"""

from math import pow


def nth_root(radicand: float, index: int, tolerance: float = 0.0001) -> float:
    """
    Approximate the nth root of the radicand for the given index

    Args:
        radicand: number from which the root is taken
        index: positive integer which is the degree of the root
        tolerance: positive real number that establishes the stopping criterion

    Returns:
        new_aproximation: approximation of the nth root of the radicand for the
        given index

    Raises:
        TypeError: radicand is not real number
        TypeError: index is not integer
        ValueError: index is not positive integer
        TypeError: tolerance is not real number
        ValueError: tolerance is not positive real number
        ValueError: math domain error

    >>> round(nth_root(9, 2),1)
    3.0

    >>> int(round(nth_root(-8, 3, 0.001)))
    -2

    >>> int(round(nth_root(256, 4, 0.001)))
    4

    >>> round(nth_root(2, 2), 5)
    1.41421

    >>> round(nth_root(0.25, 2, 0.00000001), 1)
    0.5

    >>> round(nth_root(-8/27, 3, 0.0000001), 5)
    -0.66667

    >>> nth_root(0, 2, 0.1)
    0.0

    >>> nth_root(0.0, 5)
    0.0

    >>> all(abs(nth_root(k, k, 0.00000001) - k**(1/k)) <= 1e-10 for k in range(1,10))
    True

    >>> nth_root('invalid input', 3, 0.0001)
    Traceback (most recent call last):
        ...
    TypeError: radicand must be real number, not str

    >>> nth_root(4, 0.5, 0.0001)
    Traceback (most recent call last):
        ...
    TypeError: index must be integer, not float

    >>> nth_root(16, -4, 0.001)
    Traceback (most recent call last):
        ...
    ValueError: index must be positive integer, -4 <= 0

    >>> nth_root(4, 2, '0.000001')
    Traceback (most recent call last):
        ...
    TypeError: tolerance must be real number, not str

    >>> nth_root(9, 2, -0.01)
    Traceback (most recent call last):
        ...
    ValueError: tolerance must be positive real number, -0.01 <= 0

    >>> nth_root(-256, 4, 0.0001)
    Traceback (most recent call last):
        ...
    ValueError: math domain error, radicand must be nonnegative for even index
    """
    if not isinstance(radicand, (int, float)):
        error_message = f"radicand must be real number, not {type(radicand).__name__}"
        raise TypeError(error_message)

    if not isinstance(index, int):
        error_message = f"index must be integer, not {type(index).__name__}"
        raise TypeError(error_message)

    if index <= 0:
        error_message = f"index must be positive integer, {index} <= 0"
        raise ValueError(error_message)

    if not isinstance(tolerance, (int, float)):
        error_message = f"tolerance must be real number, not {type(tolerance).__name__}"
        raise TypeError(error_message)

    if tolerance <= 0:
        error_message = f"tolerance must be positive real number, {tolerance} <= 0"
        raise ValueError(error_message)

    if radicand < 0 and index % 2 == 0:
        error_message = "math domain error, radicand must be nonnegative for even index"
        raise ValueError(error_message)

    if radicand == 0.0:
        return 0.0

    # Set initial guess
    new_aproximation = radicand
    # Set old_aproximation to enter the loop
    old_aproximation = new_aproximation + tolerance + 0.1

    # Iterate as long as the stop criterion is not satisfied
    while tolerance <= abs(old_aproximation - new_aproximation):
        old_aproximation = new_aproximation
        # Compute new_approximation with the recurrence relation described above
        first_summand = (index - 1) / index * old_aproximation
        second_summand = radicand / (index * pow(old_aproximation, index - 1))
        new_aproximation = first_summand + second_summand

    return new_aproximation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
