"""
Reference: https://www.investopedia.com/terms/p/presentvalue.asp

An algorithm that calculates the present value of a stream of yearly cash flows given...
1. The discount rate (as a decimal, not a percent)
2. An array of cash flows, with the index of the cash flow being the associated year

Note: This algorithm assumes that cash flows are paid at the end of the specified year
"""


def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """
    >>> present_value(0.13, [10, 20.70, -293, 297])
    4.69
    >>> present_value(0.07, [-109129.39, 30923.23, 15098.93, 29734,39])
    -42739.63
    >>> present_value(0.07, [109129.39, 30923.23, 15098.93, 29734,39])
    175519.15
    >>> present_value(-1, [109129.39, 30923.23, 15098.93, 29734,39])
    Traceback (most recent call last):
        ...
    ValueError: Discount rate cannot be negative
    >>> present_value(0.03, [])
    Traceback (most recent call last):
        ...
    ValueError: Cash flows list cannot be empty
    """
    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative")
    if not cash_flows:
        raise ValueError("Cash flows list cannot be empty")
    present_value = sum(
        cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows)
    )
    return round(present_value, ndigits=2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
