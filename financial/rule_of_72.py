"""
Reference: https://www.investopedia.com/terms/r/ruleof72.asp
The Rule of 72 refers to the time value of money. It helps you know the time (in terms of years)
required to double your money at a given interest rate. That's why it is popularly known as the
'doubling of money' principle.
"""


def rule_of_72(interest_rate: float) -> float:
    """
    >>> rule_of_72(12)
    6.0
    >>> rule_of_72(6)
    12.0
    >>> rule_of_72(2.5)
    28.8
    >>> rule_of_72(-1)
    Traceback (most recent call last):
        ...
    ValueError: Interest rate cannot be negative
    """
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")

    return round(72 / interest_rate, ndigits=2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
