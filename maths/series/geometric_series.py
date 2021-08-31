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


def geometric_series(nth_term: int, start_term_a: float, common_ratio_r: float) -> list:
    """Pure Python implementation of Geometric Series algorithm
    :param nth_term: The last term (nth term of Geometric Series)
    :param start_term_a : The first term of Geometric Series
    :param common_ratio_r : The common ratio between all the terms
    :return: The Geometric Series starting from first term a and multiple of common
        ration with first term with increase in power till last term (nth term)
    Examples:
    >>> geometric_series(4, 2, 2)
    [2, '4.0', '8.0', '16.0']
    >>> geometric_series(4, 2.0, 2.0)
    [2.0, '4.0', '8.0', '16.0']
    >>> geometric_series(4, 2.1, 2.1)
    [2.1, '4.41', '9.261000000000001', '19.448100000000004']
    >>> geometric_series(4, 2, -2)
    [2, '-4.0', '8.0', '-16.0']
    >>> geometric_series(4, -2, 2)
    [-2, '-4.0', '-8.0', '-16.0']
    >>> geometric_series(-4, 2, 2)
    []
    >>> geometric_series(0, 100, 500)
    []
    >>> geometric_series(1, 1, 1)
    [1]
    >>> geometric_series(0, 0, 0)
    []
    """
    # raise error if nth_term input is not an int
    if type(nth_term) != int:
        raise ValueError("n_th term has to be an integer")
    if type(start_term_a) not in [int, float] or type(common_ratio_r) not in [
        int,
        float,
    ]:
        raise ValueError("a and r have to be real numbers")
    series: list = []
    power = 1
    multiple = common_ratio_r
    for _ in range(int(nth_term)):
        if series == []:
            series.append(start_term_a)
        else:
            power += 1
            series.append(str(float(start_term_a) * float(multiple)))
            multiple = pow(float(common_ratio_r), power)
    return series


if __name__ == "__main__":
    nth_term_input = input(
        "Enter the last number (n term) of the Geometric Series"
    ).strip()
    # keep asking for nth_term till input is not an integer
    done = 0
    while not done:
        try:
            nth_term = int(nth_term_input)
            done = 1
        except ValueError:
            print("nth term should be an integer")
            nth_term_input = input(
                "Enter the last number (nth term) of the P-Series: "
            ).strip()

    start_term_a_input = input(
        "Enter the starting term (a) of the Geometric Series"
    ).strip()
    # keep asking for a till input is not a real number
    done = 0
    while not done:
        try:
            start_term_a = float(start_term_a_input)
            done = 1
        except ValueError:
            print("a should be a real number")
            start_term_a_input = input(
                "Enter the starting term (a) of the Geometric Series"
            ).strip()

    common_ratio_r_input = input(
        "Enter the common ratio between two terms (r) of the Geometric Series"
    ).strip()
    # keep asking for r till input is not a real number
    done = 0
    while not done:
        try:
            common_ratio_r = float(common_ratio_r_input)
            done = 1
        except ValueError:
            print("r should be a real number")
            common_ratio_r_input = input(
                "Enter the common ratio between two terms (r) of the Geometric Series"
            ).strip()

    print("Formula of Geometric Series => a + ar + ar^2 ... +ar^n")
    print(geometric_series(nth_term, start_term_a, common_ratio_r))
