def gcd(numerator: int, denominator: int) -> int:
    """
    >>> gcd(12, 18)
    6
    >>> gcd(20, 25)
    5
    >>> gcd(20, 0)
    Traceback (most recent call last):
    ValueError: The Denominator cannot be 0
    """
    if denominator == 0:
        raise ValueError("The Denominator cannot be 0")
    while denominator:
        numerator, denominator = denominator, numerator % denominator
    return numerator


def proper_fractions(denominator: int) -> list[str]:
    """
    this algorithm returns a list of proper fractions, in the
    range between 0 and 1, which can be formed with the given denominator
    >>> proper_fractions(10)
    ['1/10', '3/10', '7/10', '9/10']
    >>> proper_fractions(5)
    ['1/5', '2/5', '3/5', '4/5']
    >>> proper_fractions(-15)
    Traceback (most recent call last):
    ValueError: The Denominator Cannot be less than 0
    >>>
    """

    if denominator < 0:
        raise ValueError("The Denominator Cannot be less than 0")
    return [f"{numerator}/{denominator}" for numerator in range(1, denominator) if gcd(numerator, denominator) == 1]


if __name__ == "__main__":
    __import__("doctest").testmod()
