"""
Zadeh's fuzzy-set operators on membership vectors.

A fuzzy set over a universe of discourse ``X`` is described by a *membership
function* ``mu: X -> [0, 1]``.  Once the universe is sampled on a grid, that
function becomes a NumPy vector of membership degrees and the classic set
operations reduce to element-wise arithmetic.

This module implements the standard (Zadeh) operators plus a few common
alternatives.  Unlike ``fuzzy_operations.FuzzySet`` -- which stores a *triangular
fuzzy number* by its three defining points -- the functions here work on the
sampled membership vectors directly, so they apply to *any* membership shape
(triangular, trapezoidal, Gaussian, ...).

References:
  - https://en.wikipedia.org/wiki/Fuzzy_set#Fuzzy_set_operations
  - https://en.wikipedia.org/wiki/Fuzzy_logic
  - https://en.wikipedia.org/wiki/T-norm

Requirements:
  - numpy

Originally contributed as a ``scikit-fuzzy`` demo by Jigyasa Gandhi; rewritten
here to be dependency-free (NumPy only) and covered by doctests.
"""

import numpy as np
from numpy.typing import NDArray


def triangular_membership(
    grid: NDArray[np.float64], left: float, peak: float, right: float
) -> NDArray[np.float64]:
    """
    Sample a triangular membership function on the ``grid``.

    The membership rises linearly from 0 at ``left`` to 1 at ``peak`` and falls
    back to 0 at ``right``.

    >>> grid = np.array([0.0, 25.0, 50.0])
    >>> triangular_membership(grid, 0, 25, 50)
    array([0., 1., 0.])
    >>> triangular_membership(np.array([10.0, 12.5]), 0, 25, 50)
    array([0.4, 0.5])
    """
    if not left <= peak <= right:
        msg = f"Expected left <= peak <= right, got {left}, {peak}, {right}"
        raise ValueError(msg)
    left_slope = (
        (grid - left) / (peak - left) if peak > left else np.where(grid < peak, 0, 1)
    )
    right_slope = (
        (right - grid) / (right - peak) if right > peak else np.where(grid > peak, 0, 1)
    )
    return np.clip(np.minimum(left_slope, right_slope), 0.0, 1.0)


def fuzzy_union(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Union (logical OR): ``max(mu_A(x), mu_B(x))``.

    >>> fuzzy_union(np.array([0.2, 0.7]), np.array([0.5, 0.1]))
    array([0.5, 0.7])
    """
    return np.maximum(membership_a, membership_b)


def fuzzy_intersection(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Intersection (logical AND): ``min(mu_A(x), mu_B(x))``.

    >>> fuzzy_intersection(np.array([0.2, 0.7]), np.array([0.5, 0.1]))
    array([0.2, 0.1])
    """
    return np.minimum(membership_a, membership_b)


def fuzzy_complement(membership: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Complement (logical NOT): ``1 - mu_A(x)``.

    >>> fuzzy_complement(np.array([0.0, 0.3, 1.0]))
    array([1. , 0.7, 0. ])
    """
    return 1.0 - membership


def fuzzy_difference(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Difference ``A / B``: ``min(mu_A(x), 1 - mu_B(x))``.

    >>> fuzzy_difference(np.array([0.6, 0.4]), np.array([0.2, 0.9]))
    array([0.6, 0.1])
    """
    return np.minimum(membership_a, 1.0 - membership_b)


def algebraic_sum(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Algebraic (probabilistic) sum: ``mu_A + mu_B - mu_A * mu_B``.

    >>> algebraic_sum(np.array([0.5, 1.0]), np.array([0.5, 0.2]))
    array([0.75, 1.  ])
    """
    return membership_a + membership_b - membership_a * membership_b


def algebraic_product(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Algebraic product: ``mu_A * mu_B``.

    >>> algebraic_product(np.array([0.5, 1.0]), np.array([0.5, 0.2]))
    array([0.25, 0.2 ])
    """
    return membership_a * membership_b


def bounded_sum(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Bounded sum (Lukasiewicz t-conorm): ``min(1, mu_A + mu_B)``.

    >>> bounded_sum(np.array([0.5, 0.8]), np.array([0.2, 0.7]))
    array([0.7, 1. ])
    """
    return np.minimum(1.0, membership_a + membership_b)


def bounded_difference(
    membership_a: NDArray[np.float64], membership_b: NDArray[np.float64]
) -> NDArray[np.float64]:
    """
    Bounded difference (Lukasiewicz t-norm): ``max(0, mu_A + mu_B - 1)``.

    >>> bounded_difference(np.array([0.5, 0.8]), np.array([0.2, 0.7]))
    array([0. , 0.5])
    """
    return np.maximum(0.0, membership_a + membership_b - 1.0)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Reproduce the original "young vs. middle-aged" demo, dependency-free.
    universe = np.linspace(start=0, stop=75, num=75)
    young = triangular_membership(universe, 0, 25, 50)
    middle_aged = triangular_membership(universe, 25, 50, 75)

    operations = {
        "young": young,
        "middle_aged": middle_aged,
        "union": fuzzy_union(young, middle_aged),
        "intersection": fuzzy_intersection(young, middle_aged),
        "complement(young)": fuzzy_complement(young),
        "difference young/middle": fuzzy_difference(young, middle_aged),
        "algebraic_sum": algebraic_sum(young, middle_aged),
        "algebraic_product": algebraic_product(young, middle_aged),
        "bounded_sum": bounded_sum(young, middle_aged),
        "bounded_difference": bounded_difference(young, middle_aged),
    }

    try:
        import matplotlib.pyplot as plt

        plt.figure()
        for index, (title, values) in enumerate(operations.items(), start=1):
            plt.subplot(4, 3, index)
            plt.plot(universe, values)
            plt.title(title)
            plt.grid(True)
        plt.subplots_adjust(hspace=0.5)
        plt.show()
    except ImportError:
        for title, values in operations.items():
            print(f"{title}: peak membership = {values.max():.3f}")
