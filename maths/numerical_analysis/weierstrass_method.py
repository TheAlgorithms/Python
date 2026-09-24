from collections.abc import Callable

import numpy as np


def weierstrass_method(
    polynomial: Callable[[np.ndarray], np.ndarray],
    degree: int,
    roots: np.ndarray | None = None,
    max_iter: int = 100,
) -> np.ndarray:
    """
    Approximates all complex roots of a polynomial using the
    Weierstrass (Durand-Kerner) method.
    Args:
        polynomial: A function that takes a NumPy array of complex numbers and returns
                    the polynomial values at those points.
        degree: Degree of the polynomial (number of roots to find). Must be ≥ 1.
        roots:  Optional initial guess as a NumPy array of complex numbers.
                Must have length equal to 'degree'.
                If None, perturbed complex roots of unity are used.
        max_iter: Number of iterations to perform (default: 100).

    Returns:
        np.ndarray: Array of approximated complex roots.

    Raises:
        ValueError: If degree < 1, or if initial roots length doesn't match the degree.

    Note:
        - Root updates are clipped to prevent numerical overflow.

    Example:
        >>> import numpy as np
        >>> def check(poly, degree, expected):
        ...     roots = weierstrass_method(poly, degree)
        ...     return np.allclose(np.sort(roots), np.sort(expected))

        >>> check(
        ...     lambda x: x**2 - 1,
        ...     2,
        ...     np.array([-1, 1]))
        True

        >>> check(
        ...     lambda x: x**3 - 4.5*x**2 + 5.75*x - 1.875,
        ...     3,
        ...     np.array([1.5, 0.5, 2.5])
        ... )
        True

    See Also:
        https://en.wikipedia.org/wiki/Durand%E2%80%93Kerner_method
    """

    if degree < 1:
        raise ValueError("Degree of the polynomial must be at least 1.")

    if roots is None:
        # Use perturbed complex roots of unity as initial guesses
        rng = np.random.default_rng()
        roots = np.array(
            [
                np.exp(2j * np.pi * i / degree) * (1 + 1e-3 * rng.random())
                for i in range(degree)
            ],
            dtype=np.complex128,
        )

    else:
        roots = np.asarray(roots, dtype=np.complex128)
        if roots.shape[0] != degree:
            raise ValueError(
                "Length of initial roots must match the degree of the polynomial."
            )

    for _ in range(max_iter):
        # Construct the product denominator for each root
        denominator = np.array([root - roots for root in roots], dtype=np.complex128)
        np.fill_diagonal(denominator, 1.0)  # Avoid zero in diagonal
        denominator = np.prod(denominator, axis=1)

        # Evaluate polynomial at each root
        numerator = polynomial(roots).astype(np.complex128)

        # Compute update and clip to prevent overflow
        delta = numerator / denominator
        delta = np.clip(delta, -1e10, 1e10)
        roots -= delta

    return roots


if __name__ == "__main__":
    import doctest

    doctest.testmod()
