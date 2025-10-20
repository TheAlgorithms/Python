"""
Generalized combinations (n choose r) calculator for real total and integer choose.
Wikipedia URL:
https://en.wikipedia.org/wiki/Binomial_coefficient
"""

from math import factorial as math_factorial


def combinations(total: float, choose: int) -> float:
    """
    Compute the number of combinations 
    using the formula:

        combinations = total * (total-1) * ... * (total-choose+1) / choose!

    Parameters
    ----------
    total : float
        Total number of items. Can be any real number.
    choose : int
        Number of items to select. Must be a non-negative integer.

    Returns
    -------
    float
        The number of combinations.

    Raises
    ------
    ValueError
        If choose is not a non-negative integer.

    Examples
    --------
    >>> combinations(5, 2)
    10.0
    >>> combinations(5.5, 2)
    12.375
    >>> combinations(10, 0)
    1.0
    >>> combinations(0, 0)
    1.0
    >>> combinations(5, -1)
    Traceback (most recent call last):
        ...
    ValueError: choose must be a non-negative integer
    >>> combinations(5, 2.5)
    Traceback (most recent call last):
        ...
    ValueError: choose must be a non-negative integer
    """
    if not isinstance(choose, int) or choose < 0:
        raise ValueError("choose must be a non-negative integer")

    if choose == 0:
        return 1.0

    numerator = 1.0
    for i in range(choose):
        numerator *= total - i

    denominator = math_factorial(choose)
    return numerator / denominator


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    total_input = float(input("Enter total (real number): ").strip() or 0)
    choose_input = int(input("Enter choose (non-negative integer): ").strip() or 0)
    print(
        f"combinations({total_input}, {choose_input}) = "
        f"{combinations(total_input, choose_input)}"
    )
