"""
This is an implementation of logarithmic series in Python.
Reference: https://math.stackexchange.com/questions/3973429/what-is-a-logarithmic-series
"""


def logarithmic_series(x_value: float, n_terms: int = 5, expand: bool = False) -> list:
    """
    Returns the logarithmic series for a number x (log x) upto n terms.

    Parameters:
        x_value: a floating point number for log(x)
        n_terms: number of terms to be computed
        expand: Set this flag to get the terms as real numbers,
                unset for unsolved expressions

    Examples:
        >>> logarithmic_series(3)
        ['(2^1)/1', '-(2^2)/2', '(2^3)/3', '-(2^4)/4', '(2^5)/5']

        >>> logarithmic_series(-3)
        ['-(4^1)/1', '(4^2)/2', '-(4^3)/3', '(4^4)/4', '-(4^5)/5']

        >>> logarithmic_series(3, 6)
        ['(2^1)/1', '-(2^2)/2', '(2^3)/3', '-(2^4)/4', '(2^5)/5', '-(2^6)/6']

        >>> logarithmic_series(3, expand=True)
        [2.0, -2.0, 2.6666666666666665, -4.0, 6.4]
    """
    n_times_x_minus_1: float = x_value - 1
    n: int = 1
    series: list = []
    for _ in range(n_terms):
        if expand:
            series.append(((-1) ** (n + 1)) * (n_times_x_minus_1 / n))
            n_times_x_minus_1 *= x_value - 1
        else:
            sign: str = "-" if (-1) ** (n + 1) == -1 else ""
            term: str = (
                sign + "(" + str(x_value - 1) + "^" + str(n) + ")" + "/" + str(n)
            )
            if term.startswith("-(-"):
                term = "(" + term[3::]
            elif term.startswith("(-"):
                term = "-(" + term[2::]
            series.append(term)
        n += 1
    return series


if __name__ == "__main__":
    import doctest

    doctest.testmod()
