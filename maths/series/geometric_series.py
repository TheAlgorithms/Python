"""
This is a pure Python implementation of the Geometric Series algorithm
https://en.wikipedia.org/wiki/Geometric_series
Run the doctests with the following command:
python3 -m doctest -v geometric_series.py
or
python -m doctest -v geometric_series.py
For manual testing run:
python3 geometric_series.py
"""


from __future__ import annotations


def geometric_series(
    nth_term: float | int,
    start_term_a: float | int,
    common_ratio_r: float | int,
) -> list[float | int]:
    """
    Pure Python implementation of Geometric Series algorithm

    :param nth_term: The last term (nth term of Geometric Series)
    :param start_term_a : The first term of Geometric Series
    :param common_ratio_r : The common ratio between all the terms
    :return: The Geometric Series starting from first term a and multiple of common
        ration with first term with increase in power till last term (nth term)
    Examples:
    >>> geometric_series(4, 2, 2)
    [2, 4.0, 8.0, 16.0]
    >>> geometric_series(4.0, 2.0, 2.0)
    [2.0, 4.0, 8.0, 16.0]
    >>> geometric_series(4.1, 2.1, 2.1)
    [2.1, 4.41, 9.261000000000001, 19.448100000000004]
    >>> geometric_series(4, 2, -2)
    [2, -4.0, 8.0, -16.0]
    >>> geometric_series(4, -2, 2)
    [-2, -4.0, -8.0, -16.0]
    >>> geometric_series(-4, 2, 2)
    []
    >>> geometric_series(0, 100, 500)
    []
    >>> geometric_series(1, 1, 1)
    [1]
    >>> geometric_series(0, 0, 0)
    []
    """
    if not all((nth_term, start_term_a, common_ratio_r)):
        return []
    series: list[float | int] = []
    power = 1
    multiple = common_ratio_r
    for _ in range(int(nth_term)):
        if series == []:
            series.append(start_term_a)
        else:
            power += 1
            series.append(float(start_term_a * multiple))
            multiple = pow(float(common_ratio_r), power)
    return series


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    nth_term = float(input("Enter the last number (n term) of the Geometric Series"))
    start_term_a = float(input("Enter the starting term (a) of the Geometric Series"))
    common_ratio_r = float(
        input("Enter the common ratio between two terms (r) of the Geometric Series")
    )
    print("Formula of Geometric Series => a + ar + ar^2 ... +ar^n")
    print(geometric_series(nth_term, start_term_a, common_ratio_r))
