"""
This is a pure Python implementation of the Harmonic Series algorithm
https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)

For doctests run following command:
python -m doctest -v harmonic_series.py
or
python3 -m doctest -v harmonic_series.py

For manual testing run:
python3 harmonic_series.py
"""
from fractions import Fraction


def harmonic_series(n_term: int) -> list[Fraction]:
    """Pure Python implementation of Harmonic Series algorithm

    :param n_term: The last (nth) term of Harmonic Series
    :return: The Harmonic Series starting from 1 to last (nth) term

    Examples:
    >>> harmonic_series(5)
    ['1', '1/2', '1/3', '1/4', '1/5']
    >>> harmonic_series(5.0)
    ['1', '1/2', '1/3', '1/4', '1/5']
    >>> harmonic_series(5.1)
    ['1', '1/2', '1/3', '1/4', '1/5']
    >>> harmonic_series(-5)
    []
    >>> harmonic_series(0)
    []
    >>> harmonic_series(1)
    ['1']
    """
    series = []
    for temp in range(int(n_term)):
        series.append(Fraction(1, temp + 1))
    return series


if __name__ == "__main__":
    nth_term = int(input("Enter the last number (nth term) of the Harmonic Series: "))
    print("Formula of Harmonic Series => 1+1/2+1/3 ..... 1/n")
    print([str(i) for i in harmonic_series(nth_term)])
