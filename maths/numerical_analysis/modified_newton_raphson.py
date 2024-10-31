"""
Modified Newton-Raphson Method

This method is used to find an approximate solution to a given equation f(x) = 0.
It is an iterative method that modifies the standard Newton-Raphson method to improve
convergence in certain cases, mostly when multiplicity is more than 1.

Example:
--------
>>> import math
>>> def f(x):
...     return x**3 - 2*x - 5
>>> def f_prime(x):
...     return 3*x**2 - 2
>>> modified_newton_raphson(f, f_prime, 2.0)
2.0945514815423265
"""

from typing import Callable


def modified_newton_raphson(
    function: Callable[[float], float],
    derivative_function: Callable[[float], float],
    initial_guess: float,
    tolerance: float = 1e-7,
    max_iterations: int = 1000,
) -> float:
    """
    Perform the Modified Newton-Raphson method to find the root of f(x) = 0.

    Parameters:
    -----------
    function : Callable[[float], float]
        The function for which the root is sought.
    derivative_function : Callable[[float], float]
        The derivative of the function.
    initial_guess : float
        Initial guess for the root.
    tolerance : float, optional
        Tolerance for convergence. Default is 1e-7.
    max_iterations : int, optional
        Maximum number of iterations. Default is 1000.

    Returns:
    --------
    float
        The approximate root of the equation.

    Raises:
    -------
    ValueError
        If the method does not converge within the maximum number of iterations.
    """
    x = initial_guess
    for _ in range(max_iterations):
        fx = function(x)
        fpx = derivative_function(x)
        if fpx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / fpx
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Modified Newton-Raphson method did not converge")


if __name__ == "__main__":

    def polynomial_function(value: float) -> float:
        """Polynomial function whose root is to be found."""
        return value**3 - 2 * value - 5

    def derivative_polynomial_function(value: float) -> float:
        """Derivative of the polynomial function."""
        return 3 * value**2 - 2

    root = modified_newton_raphson(
        function=polynomial_function,
        derivative_function=derivative_polynomial_function,
        initial_guess=2.0,
    )
    print(f"The root is: {root}")
