"""
This module provides a numerical implementation of the Laplace Transform.

https://en.wikipedia.org/wiki/Laplace_transform

"""

import numpy as np


def laplace_transform(
    function_values: np.ndarray, s_value: float, delta_t: float
) -> float:
    """
    Calculate the numerical Laplace Transform of a function given its values.

    Args:
        function_values: A numpy array of the function values f(t).
        s_value: The real-valued Laplace parameter 's'.
        delta_t: The positive time step between samples.

    Returns:
        The approximate real-valued Laplace transform at s_value.

    >>> t = np.linspace(0, 50, 10000, endpoint=False)
    >>> f_t = np.ones_like(t)
    >>> res = laplace_transform(f_t, s_value=2.0, delta_t=50/10000)
    >>> abs(res - 0.5) < 1e-3
    True

    >>> t = np.linspace(0, 50, 10000, endpoint=False)
    >>> f_t = np.exp(-t)
    >>> res = laplace_transform(f_t, s_value=1.0, delta_t=50/10000)
    >>> abs(res - 0.5) < 1e-3
    True
    """
    if delta_t <= 0:
        raise ValueError("delta_t must be a positive value.")
    if function_values.size == 0:
        raise ValueError("function_values array cannot be empty.")

    # Time vector corresponding to the function values
    time_vector = np.arange(len(function_values)) * delta_t

    # The integrand: f(t) * e^(-s*t)
    integrand = function_values * np.exp(-s_value * time_vector)

    # Numerical integration using the trapezoid rule
    return float(np.trapezoid(integrand, dx=delta_t))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
