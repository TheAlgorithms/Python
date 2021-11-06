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


def p_series(nth_term: int, power: int) -> list[float]:
    """
    Pure Python implementation of P-Series algorithm
    :return: The P-Series starting from 1 to last (nth) term
    Examples:
    >>> p_series(5, 2)
    [1.0, 0.25, 0.1111111111111111, 0.0625, 0.04]
    >>> p_series(-5, 2)
    []
    >>> p_series(5, -2)
    [1.0, 4.0, 9.0, 16.0, 25.0]
    >>> p_series(0, 0)
    []
    >>> p_series(1, 1)
    [1.0]
    """
    series: list[float] = []
    for temp in range(nth_term):
        series.append(1 / (pow(temp + 1, power)) if series else 1.0)
    return series


if __name__ == "__main__":
    import doctest

    doctest.testmod()
