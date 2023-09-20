"""
Program using Dividend Discount Model to pricing a company's stock, given
- Value of the next year dividend
- Constant cost of equity capital
- constant growth rate in perpetuity

Wikipedia Reference: https://en.wikipedia.org/wiki/Dividend_discount_model
"""


def dividend_discount_model(
    next_dividend: float, constant_cost: float, constant_growth: float
) -> float:
    """
    Formula for Dividend Discount Model:
    P = D1/(r-g)
    where P is the expected price of a company's stock, r is the rate of interest per month
    and n is the number of payments

    >>> dividend_discount_model(25000, 0.12, 0.03)
    277777.7777777778
    >>> dividend_discount_model(25000, 0.12, 0.10)
    1250000.0000000007
    >>> dividend_discount_model(0, 0.12, 0.03)
    Traceback (most recent call last):
        ...
    Exception: The rate of constant cost must be >= 0
    >>> dividend_discount_model(25000, -0.12, 0.03)
    Traceback (most recent call last):
        ...
    Exception: The constant growth must be >= 0
    >>> dividend_discount_model(25000, 0.12, 0)
    Traceback (most recent call last):
        ...
    """
    if next_dividend <= 0:
        raise Exception("The next year's dividend must be > 0")
    if constant_cost < 0:
        raise Exception("The rate of constant cost must be >= 0")
    if constant_growth <= 0:
        raise Exception("The constant growth must be >= 0")

    return next_dividend / (constant_cost - constant_growth)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
