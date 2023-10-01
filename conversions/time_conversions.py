from typing import Union


def seconds_to_minutes(seconds: Union[int, float], ndigits: int = 2) -> float:
    """
    Convert seconds to minutes and round it to the specified number of decimal places.

    >>> seconds_to_minutes(60)
    1.0
    >>> seconds_to_minutes(150)
    2.5
    >>> seconds_to_minutes(3600)
    60.0
    >>> seconds_to_minutes(65.4321, 3)
    1.091
    >>> seconds_to_minutes("120")
    2.0
    >>> seconds_to_minutes("seconds")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'seconds'
    """
    return round(float(seconds) / 60, ndigits)


def minutes_to_seconds(minutes: Union[int, float], ndigits: int = 2) -> float:
    """
    Convert minutes to seconds and round it to the specified number of decimal places.

    >>> minutes_to_seconds(1)
    60.0
    >>> minutes_to_seconds(2.5)
    150.0
    >>> minutes_to_seconds(60)
    3600.0
    >>> minutes_to_seconds(1.09, 3)
    65.4
    >>> minutes_to_seconds("2")
    120.0
    >>> minutes_to_seconds("minutes")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'minutes'
    """
    return round(float(minutes) * 60, ndigits)


def hours_to_minutes(hours: Union[int, float], ndigits: int = 2) -> float:
    """
    Convert hours to minutes and round it to the specified number of decimal places.

    >>> hours_to_minutes(1)
    60.0
    >>> hours_to_minutes(2.5)
    150.0
    >>> hours_to_minutes(24)
    1440.0
    >>> hours_to_minutes(1.5, 3)
    90.0
    >>> hours_to_minutes("2")
    120.0
    >>> hours_to_minutes("hours")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'hours'
    """
    return round(float(hours) * 60, ndigits)


def minutes_to_hours(minutes: Union[int, float], ndigits: int = 2) -> float:
    """
    Convert minutes to hours and round it to the specified number of decimal places.

    >>> minutes_to_hours(60)
    1.0
    >>> minutes_to_hours(150)
    2.5
    >>> minutes_to_hours(1440)
    24.0
    >>> minutes_to_hours(90, 3)
    1.5
    >>> minutes_to_hours("120")
    2.0
    >>> minutes_to_hours("minutes")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'minutes'
    """
    return round(float(minutes) / 60, ndigits)


def days_to_hours(days: Union[int, float], ndigits: int = 2) -> float:
    """
    Convert days to hours and round it to the specified number of decimal places.

    >>> days_to_hours(1)
    24.0
    >>> days_to_hours(0.5)
    12.0
    >>> days_to_hours(7)
    168.0
    >>> days_to_hours(3.5, 3)
    84.0
    >>> days_to_hours("2")
    48.0
    >>> days_to_hours("days")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'days'
    """
    return round(float(days) * 24, ndigits)


def hours_to_days(hours: Union[int, float], ndigits: int = 2) -> float:
    """
    Convert hours to days and round it to the specified number of decimal places.

    >>> hours_to_days(24)
    1.0
    >>> hours_to_days(12)
    0.5
    >>> hours_to_days(168)
    7.0
    >>> hours_to_days(84, 3)
    3.5
    >>> hours_to_days("48")
    2.0
    >>> hours_to_days("hours")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'hours'
    """
    return round(float(hours) / 24, ndigits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
