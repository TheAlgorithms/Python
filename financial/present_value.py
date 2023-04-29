# Reference: https://www.investopedia.com/terms/p/presentvalue.asp

# Algorithm that calculates the present value of a stream of yearly cash flows given...
# 1. The discount rate (as a decimal, not a percent)
# 2. An array of cash flows, with the index of the cash flow being the associated year

# Note: This algorithm assumes that cash flows are paid at the end of the specified year


def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """
    >>> round(present_value(0.13, [10, 20.70, -293, 297]), 2)
    4.69
    >>> round(present_value(0.07, [-109129.39, 30923.23, 15098.93, 29734,39]), 2)
    -42739.63
    >>> round(present_value(0.07, [109129.39, 30923.23, 15098.93, 29734,39]), 2)
    175519.15
    >>> present_value(-1, [109129.39, 30923.23, 15098.93, 29734,39])
    Traceback (most recent call last):
        ...
    ValueError: Invalid discount rate, please choose a rate other than -1
    """
    present_value = 0.0

    if discount_rate == -1:
        raise ValueError("Invalid discount rate, please choose a rate other than -1")

    for idx, cash_flow in enumerate(cash_flows):
        present_value += cash_flow / ((1 + discount_rate) ** idx)

    return (
        present_value
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
