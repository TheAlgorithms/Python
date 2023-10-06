"""
Finding the real root of a given degree of a given number, rounding to the nearest given number of decimal places without using **

Input:
    - number: 3
    - deg: 2
    - decimal_place: 5
Output:
    - Root of degree 2 of 3 up to 5 decimal places is 1.73205
"""


def finding_kth_root(number: float, deg: int, decimal_place: int) -> float:
    """
    Implementing binary search to find the kth root of a number
    Negative numbers are treated the same way as positive numbers, with the minus sign added at the end

    >>> finding_kth_root(3, 2, 5)
    1.73205
    >>> finding_kth_root(122.683, 10, 7)
    1.6176272
    >>> finding_kth_root(5, 1, 3)
    5.0
    >>> finding_kth_root(0, 2, 2)
    0.0
    >>> finding_kth_root(125.7, 2, 0)
    11.0
    >>> finding_kth_root(-123, 5, 3)
    -2.618
    >>> finding_kth_root(-123, 4, 3)
    Traceback (most recent call last):
        ...
    ValueError: Cannot calculate real root of an even degree of a negative number.
    >>> finding_kth_root(123, -1, 3)
    Traceback (most recent call last):
        ...
    ValueError: Degree of the root must be at least 1.

    """
    if deg < 1:
        raise ValueError("Degree of the root must be at least 1.")

    if deg % 2 == 0 and number < 0:
        raise ValueError(
            "Cannot calculate real root of an even degree of a negative number."
        )

    hi, lo = number, 0
    if number < 0:
        hi = -number

    error = 1
    for i in range(decimal_place + 1):
        error /= 10

    while hi - lo >= error:  # Precision is not reached, continue looping
        mid = (hi + lo) / 2
        product = 1
        for i in range(deg):
            product *= mid

        if product > abs(number):  # Overestimation, higher bound decreases to mid
            hi = mid

        else:  # Underestimation, lower bound increases to mid
            lo = mid

    if number < 0:
        return -round(lo, decimal_place)

    return round(lo, decimal_place)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
