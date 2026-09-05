"""
A unit of time is any particular time interval, used as a standard way of measuring or
expressing duration.  The base unit of time in the International System of Units (SI),
and by extension most of the Western world, is the second, defined as about 9 billion
oscillations of the caesium atom.

https://en.wikipedia.org/wiki/Unit_of_time
"""

time_chart: dict[str, float] = {
    "seconds": 1.0,
    "minutes": 60.0,  # 1 minute = 60 sec
    "hours": 3600.0,  # 1 hour = 60 minutes = 3600 seconds
    "days": 86400.0,  # 1 day = 24 hours = 1440 min = 86400 sec
    "weeks": 604800.0,  # 1 week=7d=168hr=10080min = 604800 sec
    "months": 2629800.0,  # Approximate value for a month in seconds
    "years": 31557600.0,  # Approximate value for a year in seconds
}

time_chart_inverse: dict[str, float] = {
    key: 1 / value for key, value in time_chart.items()
}


def convert_time(time_value: float, unit_from: str, unit_to: str) -> float:
    """
    Convert time from one unit to another using the time_chart above.

    >>> convert_time(3600, "seconds", "hours")
    1.0
    >>> convert_time(3500, "Seconds", "Hours")
    0.972
    >>> convert_time(1, "DaYs", "hours")
    24.0
    >>> convert_time(120, "minutes", "SeCoNdS")
    7200.0
    >>> convert_time(2, "WEEKS", "days")
    14.0
    >>> convert_time(0.5, "hours", "MINUTES")
    30.0
    >>> convert_time(-3600, "seconds", "hours")
    Traceback (most recent call last):
        ...
    ValueError: 'time_value' must be a non-negative number.
    >>> convert_time("Hello", "hours", "minutes")
    Traceback (most recent call last):
        ...
    ValueError: 'time_value' must be a non-negative number.
    >>> convert_time([0, 1, 2], "weeks", "days")
    Traceback (most recent call last):
        ...
    ValueError: 'time_value' must be a non-negative number.
    >>> convert_time(1, "cool", "century")  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: Invalid unit cool is not in seconds, minutes, hours, days, weeks, ...
    >>> convert_time(1, "seconds", "hot")  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: Invalid unit hot is not in seconds, minutes, hours, days, weeks, ...
    """
    if not isinstance(time_value, (int, float)) or time_value < 0:
        msg = "'time_value' must be a non-negative number."
        raise ValueError(msg)

    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    if unit_from not in time_chart or unit_to not in time_chart:
        invalid_unit = unit_from if unit_from not in time_chart else unit_to
        msg = f"Invalid unit {invalid_unit} is not in {', '.join(time_chart)}."
        raise ValueError(msg)

    return round(
        time_value * time_chart[unit_from] * time_chart_inverse[unit_to],
        3,
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{convert_time(3600,'seconds', 'hours') = :,}")
    print(f"{convert_time(360, 'days', 'months') = :,}")
    print(f"{convert_time(360, 'months', 'years') = :,}")
    print(f"{convert_time(1, 'years', 'seconds') = :,}")
