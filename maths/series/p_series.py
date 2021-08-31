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


def p_series(nth_term: int, power: float) -> list:
    """Pure Python implementation of P-Series algorithm

    :return: The P-Series starting from 1 to last (nth) term

    Examples:
    >>> p_series(5, 2)
    [1, '1/4', '1/9', '1/16', '1/25']
    >>> p_series(-5, 2)
    []
    >>> p_series(5, -2)
    [1, '1/0.25', '1/0.1111111111111111', '1/0.0625', '1/0.04']
    >>> p_series(0, 0)
    []
    >>> p_series(1, 1)
    [1]
    """
    # raise error if nth_term input is not an int
    if not isinstance(nth_term, int):
        raise ValueError("n_th term has to be an integer")
    # raise error if power input is not a real number
    if not isinstance(power, (int, float)):
        raise ValueError("power has to be a real number")
    series: list = []
    for temp in range(int(nth_term)):
        series.append(f"1/{pow(temp + 1, int(power))}" if series else 1)
    return series


if __name__ == "__main__":
    print("Formula of P-Series => 1+1/2^p+1/3^p ..... 1/n^p")
    nth_term_input = input("Enter the last number (nth term) of the P-Series: ").strip()
    # keep asking for nth_term till input is not an integer
    done = False
    while not done:
        try:
            nth_term = int(nth_term_input)
            done = True
        except ValueError:
            print("nth term should be an integer")
            nth_term_input = input(
                "Enter the last number (nth term) of the P-Series: "
            ).strip()
    power_input = input("Enter the power for  P-Series: ").strip()
    # keep asking for power till input is not a float
    done = 0
    while not done:
        try:
            power = float(power_input)
            done = 1
        except ValueError:
            print("power should be a real number")
            power_input = input("Enter the power for  P-Series: ").strip()
    print(p_series(nth_term, power))
