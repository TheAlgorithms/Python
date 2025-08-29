from math import gcd


def proper_fractions(denominator: int) -> list[str]:
    """
    this algorithm returns a list of proper fractions, in the
    range between 0 and 1, which can be formed with the given denominator
    https://en.wikipedia.org/wiki/Fraction#Proper_and_improper_fractions

    >>> proper_fractions(10)
    ['1/10', '3/10', '7/10', '9/10']
    >>> proper_fractions(5)
    ['1/5', '2/5', '3/5', '4/5']
    >>> proper_fractions(-15)
    Traceback (most recent call last):
        ...
    ValueError: The Denominator Cannot be less than 0
    >>> proper_fractions(0)
    []
    >>> proper_fractions(1.2)
    Traceback (most recent call last):
        ...
    ValueError: The Denominator must be an integer
    """

    if denominator < 0:
        raise ValueError("The Denominator Cannot be less than 0")
    elif isinstance(denominator, float):
        raise ValueError("The Denominator must be an integer")
    return [
        f"{numerator}/{denominator}"
        for numerator in range(1, denominator)
        if gcd(numerator, denominator) == 1
    ]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
