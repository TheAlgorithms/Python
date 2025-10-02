"""
Brent's Method for Root Finding

Find a root of a function in a bracketing interval using Brent's method.

Brent's method combines bisection, secant, and inverse quadratic interpolation to efficiently and robustly find a root of a continuous function. It is guaranteed to converge as long as the root is bracketed.

See: https://en.wikipedia.org/wiki/Brent%27s_method

Author: [Aryan Singh (2nd year LNMIIT)]
"""

from collections.abc import Callable


def brent_method(
    function: Callable[[float], float],
    lower: float,
    upper: float,
    tolerance: float = 1e-14,
    max_iterations: int = 100,
) -> float:
    """
    Find a root of a function in a bracketing interval using Brent's method.

    Args:
        function: A continuous function for which the root is sought.
        lower: One end of the bracketing interval.
        upper: The other end of the bracketing interval.
        tolerance: The tolerance for convergence (default 1e-14).
        max_iterations: Maximum number of iterations (default 100).

    Returns:
        A float value approximating the root.

    Raises:
        ValueError: If the root is not bracketed in [lower, upper].

    Examples:
        >>> brent_method(lambda x: x**3 - 1, -5, 5)
        1.0
        >>> brent_method(lambda x: x**2 - 4*x + 3, 0, 2)
        1.0
        >>> brent_method(lambda x: x**2 - 4*x + 3, 2, 4)
        3.0
        >>> brent_method(lambda x: x**2 - 4*x + 3, 4, 1000)
        Traceback (most recent call last):
            ...
        ValueError: Root is not bracketed in the interval [4, 1000].
    """
    fa = function(lower)
    fb = function(upper)
    if fa * fb >= 0:
        raise ValueError(f"Root is not bracketed in the interval [{lower}, {upper}].")

    if abs(fa) < abs(fb):
        lower, upper = upper, lower
        fa, fb = fb, fa

    c = lower
    fc = fa
    d = upper - lower
    mflag = True

    for _ in range(max_iterations):
        if fb == 0:
            return upper
        if fc not in {fa, fb}:
            # Inverse quadratic interpolation
            s = (
                lower * fb * fc / ((fa - fb) * (fa - fc))
                + upper * fa * fc / ((fb - fa) * (fb - fc))
                + c * fa * fb / ((fc - fa) * (fc - fb))
            )
        else:
            # Secant method
            s = upper - fb * (upper - lower) / (fb - fa)

        conditions = [
            not (
                (3 * lower + upper) / 4 < s < upper
                if upper > lower
                else upper < s < (3 * lower + upper) / 4
            ),
            mflag and abs(s - upper) >= abs(upper - c) / 2,
            not mflag and abs(s - upper) >= abs(c - d) / 2,
            mflag and abs(upper - c) < tolerance,
            not mflag and abs(c - d) < tolerance,
        ]
        if any(conditions):
            s = (lower + upper) / 2
            mflag = True
        else:
            mflag = False

        fs = function(s)
        d, c = c, upper
        fc = fb

        if fa * fs < 0:
            upper = s
            fb = fs
        else:
            lower = s
            fa = fs

        if abs(fa) < abs(fb):
            lower, upper = upper, lower
            fa, fb = fb, fa

        if abs(upper - lower) < tolerance or fb == 0:
            return upper

    return upper


if __name__ == "__main__":
    import doctest

    doctest.testmod()
