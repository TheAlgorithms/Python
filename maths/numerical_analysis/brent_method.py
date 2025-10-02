"""
Brent's Method for root finding.

This function implements Brent's Method, an efficient algorithm for finding the
root of a function. It combines the bisection method, the secant method, and
inverse quadratic interpolation.

Reference:
- https://en.wikipedia.org/wiki/Brent%27s_method
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html


>>> def f(x): return x**3 - x - 2
>>> round(brent_method(f, 1, 2), 6)
1.52138
>>> brent_method(f, 1, 1.5)  # No sign change, should raise an error
Traceback (most recent call last):
    ...
ValueError: f(a) and f(b) must have different signs
"""

from collections.abc import Callable


def brent_method(
    func: Callable[[float], float],
    left_bound: float,
    right_bound: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> float:
    """
    Find a root of the function f in the interval [a, b] using Brent's method.

    Args:
        func: The function for which we are trying to find a root.
        left_bound: The start of the interval.
        right_bound: The end of the interval.
        tol: The allowed error of the result.
        max_iter: Maximum number of iterations.

    Returns:
        A root of f in [a, b], accurate to within tol.

    Raises:
        ValueError: If f(a) and f(b) do not have opposite signs.
        RuntimeError: If the root is not found within max_iter iterations.
    """
    fa = func(left_bound)
    fb = func(right_bound)
    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have different signs")

    if abs(fa) < abs(fb):
        left_bound, right_bound = right_bound, left_bound
        fa, fb = fb, fa

    c, fc = left_bound, fa
    d = e = right_bound - left_bound

    for _ in range(max_iter):
        if fb == 0:
            return right_bound
        if fc not in (fa, fb):
            # Inverse quadratic interpolation
            s = (
                left_bound * fb * fc / ((fa - fb) * (fa - fc))
                + right_bound * fa * fc / ((fb - fa) * (fb - fc))
                + c * fa * fb / ((fc - fa) * (fc - fb))
            )
        else:
            # Secant Method
            s = right_bound - fb * (right_bound - left_bound) / (fb - fa)

        conditions = [
            not ((3 * left_bound + right_bound) / 4 < s < right_bound)
            if right_bound > left_bound
            else not (right_bound < s < (3 * left_bound + right_bound) / 4),
            (e is not None and abs(s - right_bound) >= abs(e / 2)),
            (d is not None and abs(d) >= abs(e / 2)),
            abs(right_bound - left_bound) < tol,
        ]
        if any(conditions):
            s = (left_bound + right_bound) / 2  # Bisection method
            e = d = right_bound - left_bound
        else:
            d = e
            e = right_bound - s

        fs = func(s)
        c, fc = right_bound, fb
        if fa * fs < 0:
            right_bound, fb = s, fs
        else:
            left_bound, fa = s, fs
        if abs(fa) < abs(fb):
            left_bound, right_bound = right_bound, left_bound
            fa, fb = fb, fa
        if abs(right_bound - left_bound) < tol:
            return right_bound

    raise RuntimeError("Maximum number of iterations reached without convergence")
