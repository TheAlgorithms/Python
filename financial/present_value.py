# Reference: https://www.investopedia.com/terms/p/presentvalue.asp

# Algorithm that calculates the present value of a stream of yearly cash flows given...
# 1. The discount rate (as a decimal, not a percent)
# 2. An array of cash flows, with the index of the cash flow being the associated year

# Note: This algorithm assumes that cash flows are paid at the end of the specified year


def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """
    >>> round(present_value(0.13, [10, 20.70, -293, 297]), 2)
    4.69
    """
    present_value = 0.0

    if discount_rate == -1:
        raise ValueError("Invalid discount rate, please choose a rate other than -1")

    for idx, cash_flow in enumerate(cash_flows):
        present_value += cash_flow / ((1 + discount_rate) ** idx)

    return present_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
