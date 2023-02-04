# Present Value Formula
# https://en.wikipedia.org/wiki/Present_value


def present_value_compound(
    future_value: float, rate: float, interest_period: float
) -> float:

    """
    >>> present_value_compound(10000.0, 0.06, 10)
    5583.947769151178
    >>> present_value_compound(10, 0.05, 500)
    2.54302403598631e-10
    >>> present_value_compound(25, 1.5, 10)
    0.00262144
    """

    if future_value <= 0:
        raise ValueError("future_value must be greater than 0")
    if rate <= 0:
        raise ValueError("rate must be greater than 0")
    if interest_period <= 0:
        raise ValueError("interest_period must be greater than 0")
    return future_value / (1 + rate) ** interest_period
