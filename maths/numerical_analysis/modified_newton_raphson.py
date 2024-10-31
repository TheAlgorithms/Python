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
    ZeroDivisionError
        If the derivative is zero.
    ValueError
        If the method does not converge within the maximum number of iterations.
    """
    x = initial_guess
    for _ in range(max_iterations):
        fx = function(x)
        fpx = derivative_function(x)
        if fpx == 0:
            raise ZeroDivisionError("Derivative is zero. No solution found.")
        x_new = x - fx / fpx
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Modified Newton-Raphson did not converge")

if __name__ == "__main__":
    import math

    def compute_function(current_x: float) -> float:
        return current_x**3 - 2 * current_x - 5

    def compute_derivative(current_x: float) -> float:
        return 3 * current_x**2 - 2

    root = modified_newton_raphson(
        function=polynomial_function,
        derivative_function=derivative_polynomial_function,
        initial_guess=2.0
    )
    print(f"The root is: {root}")
