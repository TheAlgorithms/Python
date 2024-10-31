from typing import Callable


def fixed_point_iteration(
    iteration_function: Callable[[float], float],
    initial_guess: float,
    tolerance: float = 1e-7,
    max_iterations: int = 1000,
) -> float:
    """
    Perform Fixed Point Iteration to find the root of the equation x = g(x).

    Parameters:
    -----------
    iteration_function : Callable[[float], float]
        The function derived from f(x) such that x = g(x).
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
        x_new = iteration_function(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Fixed Point Iteration did not converge")


if __name__ == "__main__":

    def quadratic_transform(current_value: float) -> float:
        """Quadratic transformation function for iteration."""
        return (current_value**2 + 2) / 3

    root = fixed_point_iteration(quadratic_transform, initial_guess=1.0)
    print(f"Approximate root: {root}")
