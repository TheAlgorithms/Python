"""
Reference: https://www.auditexcel.co.za/blog/discounting-cash-flows-with-multiple-discount-rates/

An algorithm that calculates the present value of a stream of yearly cash flows given...
1. An array containing tuples of discount rates and their associated duration.

For example [(0.05, 2), (0.06, 3)] would mean that a discount rate of 5% is applied to
the first 2 cash flows, while a discount rate of 6% is applied to the next 3 cash flows.

If the discount rate is fixed for the entire duration, then the user may provide just
the discount rate(as a float).

2. An array of cash flows, with the index of the cash flow being the associated year

Note: This algorithm assumes that cash flows are paid at the end of the specified year
"""


def present_value(
    discount_rates: float | list[tuple], cash_flows: list[float]
) -> float:
    """
    >>> present_value(0.13, [10, 20.70, -293, 297])
    4.15
    >>> present_value([(0.13, 4)], [10, 20.70, -293, 297])
    4.15
    >>> present_value([(0.03, 4), (0.05, 1)], [6, 6, 6, 106, 6])
    115.85
    >>> present_value([(0.05, 1), (0.07, 1), (0.02, 1), (0.04, 1)],
    ... [32.21, 324.45, 524.9, 12])
    818.95
    >>> present_value([(0.07, 4)], [109129.39, 30923.23, 15098.93, 29734.39])
    164009.08
    >>> present_value([(-1, 4)], [109129.39, 30923.23, 15098.93, 29734.39])
    Traceback (most recent call last):
        ...
    ValueError: Discount rate cannot be negative
    >>> present_value([(0.03, 4)], [])
    Traceback (most recent call last):
        ...
    ValueError: Cash flows list cannot be empty
    >>> present_value([(0.03, 4)], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Sum of discount rates must equal # of cash flows.
    """

    if isinstance(discount_rates, float):
        discount_rates = [(discount_rates, len(cash_flows))]

    if len(discount_rates) == 0:
        raise ValueError("Discount rates list cannot be empty")

    for rate, duration in discount_rates:
        if rate < 0:
            raise ValueError("Discount rate cannot be negative")
        if duration < 1:
            raise ValueError("Discount rate duration cannot be negative or zero")

    if len(cash_flows) == 0:
        raise ValueError("Cash flows list cannot be empty")

    criteria = sum([duration for _, duration in discount_rates])
    if criteria != len(cash_flows):
        raise ValueError("Sum of discount rates must equal # of cash flows.")

    present_value = 0.0
    cash_flow_index = 0

    for rate, duration in discount_rates:
        for _ in range(duration):
            present_value += cash_flows[cash_flow_index] / (1 + rate) ** (
                cash_flow_index + 1
            )
            cash_flow_index += 1

    return round(present_value, ndigits=2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
