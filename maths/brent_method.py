from typing import Callable

def brent_method(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-8,
    max_iter: int = 100
) -> float:
    """
    Find the root of function f in the interval [a, b] using Brent's Method.
    
    Brent's Method combines bisection, secant, and inverse quadratic interpolation.
    
    Parameters
    ----------
    f : Callable[[float], float]
        Function for which to find the root.
    a : float
        Left endpoint of interval.
    b : float
        Right endpoint of interval.
    tol : float
        Tolerance for convergence (default 1e-8).
    max_iter : int
        Maximum number of iterations (default 100).
    
    Returns
    -------
    float
        Approximate root of f in [a, b].
    
    Raises
    ------
    ValueError
        If f(a) and f(b) do not have opposite signs.
    
    Examples
    --------
    >>> def func(x): return x**3 - x - 2
    >>> round(brent_method(func, 1, 2), 5)
    1.52138

    >>> def func2(x): return x**2 + 1
    >>> brent_method(func2, 0, 1)
    Traceback (most recent call last):
    ...
    ValueError: f(a) and f(b) must have opposite signs
    """
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c = a
    fc = fa
    d = e = b - a

    for iteration in range(max_iter):
        if fb == 0:
            return b

        if fa != fc and fb != fc:
            # Inverse quadratic interpolation
            s = (
                a * fb * fc / ((fa - fb) * (fa - fc))
                + b * fa * fc / ((fb - fa) * (fb - fc))
                + c * fa * fb / ((fc - fa) * (fc - fb))
            )
        else:
            # Secant method
            s = b - fb * (b - a) / (fb - fa)

        conditions = [
            not ((3 * a + b) / 4 < s < b) if b > a else not (b < s < (3 * a + b) / 4),
            iteration > 1 and abs(s - b) >= abs(b - c) / 2,
            iteration <= 1 and abs(s - b) >= abs(c - d) / 2,
            iteration > 1 and abs(b - c) < tol,
            iteration <= 1 and abs(c - d) < tol,
        ]

        if any(conditions):
            # Bisection fallback
            s = (a + b) / 2
            d = e = b - a

        fs = f(s)
        d, c = c, b
        fc = fb

        if fa * fs < 0:
            b = s
            fb = fs
        else:
            a = s
            fa = fs

        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa

        if abs(b - a) < tol:
            return b

    # If we reach max iterations
    return b
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

