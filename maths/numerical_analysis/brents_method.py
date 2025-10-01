from collections.abc import Callable

def brent_method(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-14,
    max_iter: int = 100
) -> float:
    """
    Root finding using Brent's method.

    >>> brent_method(lambda x: x**3 - 1, -5, 5)
    1.0
    >>> brent_method(lambda x: x**2 - 4*x + 3, 0, 2)
    1.0
    >>> brent_method(lambda x: x**2 - 4*x + 3, 2, 4)
    3.0
    >>> brent_method(lambda x: x**2 - 4*x + 3, 4, 1000)
    Traceback (most recent call last):
        ...
    ValueError: Root is not bracketed.
    """

    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        raise ValueError("Root is not bracketed.")

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c = a
    fc = fa
    d = b - a  # Only d is used, e removed
    mflag = True

    for _ in range(max_iter):
        if fb == 0:
            return b
        if fa != fc and fb != fc:
            # Inverse quadratic interpolation
            s = (
                a * fb * fc / ((fa - fb) * (fa - fc)) +
                b * fa * fc / ((fb - fa) * (fb - fc)) +
                c * fa * fb / ((fc - fa) * (fc - fb))
            )
        else:
            # Secant method
            s = b - fb * (b - a) / (fb - fa)

        conditions = [
            not ((3 * a + b) / 4 < s < b if b > a else b < s < (3 * a + b) / 4),
            mflag and abs(s - b) >= abs(b - c) / 2,
            not mflag and abs(s - b) >= abs(c - d) / 2,
            mflag and abs(b - c) < tol,
            not mflag and abs(c - d) < tol,
        ]
        if any(conditions):
            s = (a + b) / 2
            mflag = True
        else:
            mflag = False

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

        if abs(b - a) < tol or fb == 0:
            return b

    return b

if __name__ == "__main__":
    from doctest import testmod
    testmod()
