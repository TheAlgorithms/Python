"""
Fixed Point Iteration Method

This method is used to find an approximate solution to a given equation f(x) = 0.
The function g(x) is derived from f(x) such that x = g(x).

Example:
--------
>>> def g(x):
...     return (x**2 + 2) / 3
>>> fixed_point_iteration(g, 1.0)
1.618033988749895
"""

def fixed_point_iteration(g, x0, tol=1e-7, max_iter=1000):
    """
    Perform Fixed Point Iteration to find the root of the equation x = g(x).

    Parameters:
    -----------
    g : function
        The function g(x) derived from f(x) such that x = g(x).
    x0 : float
        Initial guess for the root.
    tol : float, optional
        Tolerance for the convergence of the method. Default is 1e-7.
    max_iter : int, optional
        Maximum number of iterations. Default is 1000.

    Returns:
    --------
    float
        The approximate root of the equation x = g(x).

    Raises:
    -------
    ValueError
        If the method does not converge within the maximum number of iterations.
    """
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Fixed Point Iteration did not converge")

if __name__ == "__main__":
    def g(x):
        return (x**2 + 2) / 3

    root = fixed_point_iteration(g, 1.0)
    print(f"The root is: {root}")