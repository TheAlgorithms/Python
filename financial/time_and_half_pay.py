"""
Calculate time and a half pay
"""


def pay(hours_worked: float, pay_rate: float, hours: float = 40) -> float:
    """
    hours_worked = The total hours worked
    pay_rate = Amount of money per hour
    hours = Number of hours that must be worked before you receive time and a half

    >>> pay(41, 1)
    41.5
    >>> pay(65, 19)
    1472.5
    >>> pay(10, 1)
    10.0
    """
    # Check that all input parameters are float or integer
    assert isinstance(hours_worked, (float, int)), (
        "Parameter 'hours_worked' must be of type 'int' or 'float'"
    )
    assert isinstance(pay_rate, (float, int)), (
        "Parameter 'pay_rate' must be of type 'int' or 'float'"
    )
    assert isinstance(hours, (float, int)), (
        "Parameter 'hours' must be of type 'int' or 'float'"
    )

    normal_pay = hours_worked * pay_rate
    over_time = max(0, hours_worked - hours)
    over_time_pay = over_time * pay_rate / 2
    return normal_pay + over_time_pay


if __name__ == "__main__":
    # Test
    import doctest

    doctest.testmod()
