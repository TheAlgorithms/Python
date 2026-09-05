"""
This is a pure Python implementation of the P-Series algorithm
https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)#P-series
For doctests run following command:
python -m doctest -v p_series.py
or
python3 -m doctest -v p_series.py
For manual testing run:
python3 p_series.py
"""

from __future__ import annotations


def p_series(nth_term: float | str, power: float | str) -> list[str]:
    """
    Pure Python implementation of P-Series algorithm
    :return: The P-Series starting from 1 to last (nth) term
    Examples:
    >>> p_series(5, 2)
    ['1', '1 / 4', '1 / 9', '1 / 16', '1 / 25']
    >>> p_series(-5, 2)
    []
    >>> p_series(5, -2)
    ['1', '1 / 0.25', '1 / 0.1111111111111111', '1 / 0.0625', '1 / 0.04']
    >>> p_series("", 1000)
    ['']
    >>> p_series(0, 0)
    []
    >>> p_series(1, 1)
    ['1']
    """
    if nth_term == "":
        return [""]
    nth_term = int(nth_term)
    power = int(power)
    series: list[str] = []
    for temp in range(int(nth_term)):
        series.append(f"1 / {pow(temp + 1, int(power))}" if series else "1")
    return series


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    nth_term = int(input("Enter the last number (nth term) of the P-Series"))
    power = int(input("Enter the power for  P-Series"))
    print("Formula of P-Series => 1+1/2^p+1/3^p ..... 1/n^p")
    print(p_series(nth_term, power))
