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
    f: Callable[[float], float],
    f_prime: Callable[[float], float],
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 1000
) -> float:
    """
    Perform the Modified Newton-Raphson method to find the root of the equation f(x) = 0.

    Parameters:
    -----------
    f : function
        The function for which we want to find the root.
    f_prime : function
        The derivative of the function f.
    x0 : float
        Initial guess for the root.
    tol : float, optional
        Tolerance for the convergence of the method. Default is 1e-7.
    max_iter : int, optional
        Maximum number of iterations. Default is 1000.

    Returns:
    --------
    float
        The approximate root of the equation f(x) = 0.

    Raises:
    -------
    ValueError
        If the method does not converge within the maximum number of iterations.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / fpx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Modified Newton-Raphson method did not converge")

if __name__ == "__main__":
    import math

    def f(x):
        return x**3 - 2*x - 5

    def f_prime(x):
        return 3*x**2 - 2

    root = modified_newton_raphson(f, f_prime, 2.0)
    print(f"The root is: {root}")