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
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> float:
    """
    Find a root of the function f in the interval [a, b] using Brent's method.

    Args:
        f: The function for which we are trying to find a root.
        a: The start of the interval.
        b: The end of the interval.
        tol: The allowed error of the result.
        max_iter: Maximum number of iterations.

    Returns:
        A root of f in [a, b], accurate to within tol.

    Raises:
        ValueError: If f(a) and f(b) do not have opposite signs.
        RuntimeError: If the root is not found within max_iter iterations.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have different signs")

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c, fc = a, fa
    d = e = b - a

    for _ in range(max_iter):
        if fb == 0:
            return b
        if fc not in (fa, fb):
            # Inverse quadratic interpolation
            s = (
                a * fb * fc / ((fa - fb) * (fa - fc))
                + b * fa * fc / ((fb - fa) * (fb - fc))
                + c * fa * fb / ((fc - fa) * (fc - fb))
            )
        else:
            # Secant Method
            s = b - fb * (b - a) / (fb - fa)

        conditions = [
            not ((3 * a + b) / 4 < s < b) if b > a else not (b < s < (3 * a + b) / 4),
            (e is not None and abs(s - b) >= abs(e / 2)),
            (d is not None and abs(d) >= abs(e / 2)),
            abs(b - a) < tol,
        ]
        if any(conditions):
            s = (a + b) / 2  # Bisection method
            e = d = b - a
        else:
            d = e
            e = b - s

        fs = f(s)
        c, fc = b, fb
        if fa * fs < 0:
            b, fb = s, fs
        else:
            a, fa = s, fs
        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa
        if abs(b - a) < tol:
            return b

    raise RuntimeError("Maximum number of iterations reached without convergence")
