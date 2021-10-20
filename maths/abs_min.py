from __future__ import annotations

from .abs import abs_val


def abs_min(x: list[int]) -> int:
    """
    >>> abs_min([0,5,1,11])
    0
    >>> abs_min([3,-10,-2])
    -2
    >>> abs_min([])
    Traceback (most recent call last):
        ...
    ValueError: abs_min() arg is an empty sequence
    """
    if len(x) == 0:
        raise ValueError("abs_min() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs_val(i) < abs_val(j):
            j = i
    return j


def main():
    a = [-3, -1, 2, -11]
    print(abs_min(a))  # = -1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
