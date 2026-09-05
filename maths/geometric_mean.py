"""
The Geometric Mean of n numbers is defined as the n-th root of the product
of those numbers. It is used to measure the central tendency of the numbers.
https://en.wikipedia.org/wiki/Geometric_mean
"""


def compute_geometric_mean(*args: int) -> float:
    """
    Return the geometric mean of the argument numbers.
    >>> compute_geometric_mean(2,8)
    4.0
    >>> compute_geometric_mean('a', 4)
    Traceback (most recent call last):
        ...
    TypeError: Not a Number
    >>> compute_geometric_mean(5, 125)
    25.0
    >>> compute_geometric_mean(1, 0)
    0.0
    >>> compute_geometric_mean(1, 5, 25, 5)
    5.0
    >>> compute_geometric_mean(2, -2)
    Traceback (most recent call last):
        ...
    ArithmeticError: Cannot Compute Geometric Mean for these numbers.
    >>> compute_geometric_mean(-5, 25, 1)
    -5.0
    """
    product = 1
    for number in args:
        if not isinstance(number, int) and not isinstance(number, float):
            raise TypeError("Not a Number")
        product *= number
    # Cannot calculate the even root for negative product.
    # Frequently they are restricted to being positive.
    if product < 0 and len(args) % 2 == 0:
        raise ArithmeticError("Cannot Compute Geometric Mean for these numbers.")
    mean = abs(product) ** (1 / len(args))
    # Since python calculates complex roots for negative products with odd roots.
    if product < 0:
        mean = -mean
    # Since it does floating point arithmetic, it gives 64**(1/3) as 3.99999996
    possible_mean = float(round(mean))
    # To check if the rounded number is actually the mean.
    if possible_mean ** len(args) == product:
        mean = possible_mean
    return mean


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="compute_geometric_mean")
    print(compute_geometric_mean(-3, -27))
