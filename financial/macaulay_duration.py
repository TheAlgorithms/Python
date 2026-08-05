"""
Calculate the Macaulay Duration of a bond.
Reference: https://www.investopedia.com/terms/m/macaulayduration.asp
"""

from __future__ import annotations


def macaulay_duration(
    face_value: float,
    coupon_rate: float,
    periods: int,
    yield_rate: float,
) -> float:
    """
    Calculates the Macaulay Duration of a bond.

    :param face_value: The final payout amount of the bond.
    :param coupon_rate: The annual interest rate paid by the bond.
    :param periods: The number of years until the bond matures.
    :param yield_rate: The current market interest rate used to discount
                       future cash flows.
    :return: The Macaulay Duration of the bond in years.

    >>> round(macaulay_duration(1000.0, 0.05, 8, 0.04), 2)
    6.83
    >>> round(macaulay_duration(987435.34, 0.07, 5, 0.038), 2)
    4.43
    >>> round(macaulay_duration(3564.2, 0.023, 6, 0.071), 2)
    5.62
    >>> macaulay_duration(-1000.0, 0.05, 8, 0.04)
    Traceback (most recent call last):
        ...
    ValueError: face_value must be > 0
    >>> macaulay_duration(1000.0, -0.05, 8, 0.04)
    Traceback (most recent call last):
        ...
    ValueError: coupon_rate must be >= 0
    >>> macaulay_duration(1000.0, 0.05, 0, 0.04)
    Traceback (most recent call last):
        ...
    ValueError: periods must be > 0
    >>> macaulay_duration(1000.0, 0.05, 8, -0.04)
    Traceback (most recent call last):
        ...
    ValueError: yield_rate must be > 0
    """
    if face_value <= 0:
        raise ValueError("face_value must be > 0")
    if coupon_rate < 0:
        raise ValueError("coupon_rate must be >= 0")
    if periods < 1:
        raise ValueError("periods must be > 0")
    if yield_rate <= 0:
        raise ValueError("yield_rate must be > 0")

    total_present_value: float = 0.0
    total_time_weighted_value: float = 0.0

    for period in range(1, periods + 1):
        cash_flow: float = face_value * coupon_rate + (
            face_value if period == periods else 0
        )

        time_weighted_value: float = (period * cash_flow) / pow(1 + yield_rate, period)
        total_time_weighted_value += time_weighted_value

        present_value: float = cash_flow / pow(1 + yield_rate, period)
        total_present_value += present_value

    return total_time_weighted_value / total_present_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
