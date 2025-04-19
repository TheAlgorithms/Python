"""
Calculate time and a half pay
"""


def pay(hours_worked: float, pay_rate: float, hours: float = 40) -> float:
    """
    Calculate total pay including time-and-a-half for overtime.

    Parameters:
    hours_worked: Total number of hours worked.
    pay_rate: Pay rate per hour.
    hours: Number of hours to work before overtime applies (default 40).

    Returns:
    Total pay including overtime compensation.

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

    regular_hours = min(hours_worked, hours)
    overtime_hours = max(0, hours_worked - hours)

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5

    return regular_pay + overtime_pay


if __name__ == "__main__":
    # Run doctests
    import doctest

    doctest.testmod()
