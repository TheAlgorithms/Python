"""
The Laplace Transform is defined as: L{f(t)} = integral from 0 to infinity of e^(-st) * f(t) dt.

Wiki: https://en.wikipedia.org/wiki/Laplace_transform

"""

import numpy as np


def laplace_transform(
    function_values: np.ndarray, s_value: float, delta_t: float
) -> float:
    """
    Calculate the numerical Laplace Transform of a function given its values over time.

    Args:
        function_values: A numpy array of the function values f(t).
        s_value: The complex frequency parameter 's' (modeled here as a float).
        delta_t: The time step between samples.

    Returns:
        The approximate value of the Laplace transform at s_value.

    Example: For f(t) = 1, the Laplace transform L{1} = 1/s.
    If s = 2, L{1} should be 0.5.
    
    >>> t = np.linspace(0, 50, 10000)
    >>> f_t = np.ones_like(t) # f(t) = 1
    >>> res = laplace_transform(f_t, s_value=2.0, delta_t=50/10000)
    >>> abs(res - 0.5) < 1e-3
    True
    
    Example: For f(t) = e^(-t), the Laplace transform L{e^-t} = 1/(s+1).
    If s = 1, L{e^-t} should be 0.5.

    >>> t = np.linspace(0, 50, 10000)
    >>> f_t = np.exp(-t)
    >>> res = laplace_transform(f_t, s_value=1.0, delta_t=50/10000)
    >>> abs(res - 0.5) < 1e-3
    True
    """
    if s_value < 0:
        raise ValueError("s_value must be non-negative for convergence.")

    # Time vector corresponding to the function values
    time_vector = np.arange(len(function_values)) * delta_t
    
    # The integrand: f(t) * e^(-s*t)
    integrand = function_values * np.exp(-s_value * time_vector)
    
    # Numerical integration using the trapezoidal rule
    result = np.trapezoid(integrand, dx=delta_t)
    
    return float(result)


if __name__ == "__main__":
    import doctest

    
    doctest.testmod()
    
