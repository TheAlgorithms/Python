from collections.abc import Callable


def brent_method(
    func: Callable[[float], float],
    left: float,
    right: float,
    tol: float = 1e-8,
    max_iter: int = 100,
) -> float:
    """
    Find the root of function func in the interval [left, right] using Brent's Method.

    Brent's Method combines bisection, secant, and inverse quadratic interpolation.


    Parameters
    ----------
    func : Callable[[float], float]
        Function for which to find the root.
    left : float
        Left endpoint of interval.
    right : float
        Right endpoint of interval.
    tol : float
        Tolerance for convergence (default 1e-8).
    max_iter : int
        Maximum number of iterations (default 100).


    Returns
    -------
    float
        Approximate root of func in [left, right].

    Raises
    ------
    ValueError
        If func(left) and func(right) do not have opposite signs.

    Examples
    --------
    >>> def f(x): return x**3 - x - 2
    >>> round(brent_method(f, 1, 2), 5)
    1.52138

    >>> def f2(x): return x**2 + 1
    >>> brent_method(f2, 0, 1)
    Traceback (most recent call last):
    ...
    ValueError: func(left) and func(right) must have opposite signs
    """
    fl = func(left)
    fr = func(right)

    if fl * fr >= 0:
        raise ValueError("func(left) and func(right) must have opposite signs")

    if abs(fl) < abs(fr):
        left, right = right, left
        fl, fr = fr, fl

    c = left
    fc = fl
    d = right - left

    for iteration in range(max_iter):
        if fr == 0:
            return right

        if fc not in (fl, fr):
            # Inverse quadratic interpolation
            s = (
                left * fr * fc / ((fl - fr) * (fl - fc))
                + right * fl * fc / ((fr - fl) * (fr - fc))
                + c * fl * fr / ((fc - fl) * (fc - fr))
            )
        else:
            # Secant method
            s = right - fr * (right - left) / (fr - fl)

        conditions = [
            not ((3 * left + right) / 4 < s < right)
            if right > left
            else not (right < s < (3 * left + right) / 4),
            iteration > 1 and abs(s - right) >= abs(right - c) / 2,
            iteration <= 1 and abs(s - right) >= abs(c - d) / 2,
            iteration > 1 and abs(right - c) < tol,
            iteration <= 1 and abs(c - d) < tol,
        ]

        if any(conditions):
            # Bisection fallback
            s = (left + right) / 2
            d = right - left

        fs = func(s)
        d, c = c, right
        fc = fr

        if fl * fs < 0:
            right = s
            fr = fs
        else:
            left = s
            fl = fs

        if abs(fl) < abs(fr):
            left, right = right, left
            fl, fr = fr, fl

        if abs(right - left) < tol:
            return right

    return right


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
