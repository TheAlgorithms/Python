"""
Calculate time and a half pay

"""


def pay(hours_worked: float, pay_rate: float, hours: float = 40) -> float:
    """
    hours_worked = The total hours worked
    pay_rate = Ammount of money per hour
    hours = Number of hours that must be worked before you recieve time and a half
    >>> pay(41, 1)
    41.5
    >>> pay(65, 19)
    1472.5
    >>> pay(10, 1)
    10.0
    """
    # Check that all input parameters are float or integer
    assert type(hours_worked) is float or type(hours_worked) is int, (
        "Parameter 'hours_worked' must be of type 'int' or 'float'"
    )
    assert type(pay_rate) is float or type(pay_rate) is int, (
        "Parameter 'hours_worked' must be of type 'int' or 'float'"
    )
    assert type(hours) is float or type(hours) is int, (
        "Parameter 'hours_worked' must be of type 'int' or 'float'"
    )

    normal_pay = hours_worked * pay_rate
    over_time = hours_worked - hours
    # Another way
    """over_time_pay = ((over_time * ((over_time + (over_time ** 2) ** 0.5) / (2 * over_time))) / 2) * pay_rate"""
    over_time_pay = (max(0, over_time) / 2) * pay_rate
    total_pay = normal_pay + over_time_pay
    return total_pay


if __name__ == "__main__":
    # Test
    import doctest

    doctest.testmod()
