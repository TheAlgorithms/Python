"""
A unit of time is any particular time interval, used as a standard
way of measuring or expressing duration.
The base unit of time in the International System of Units (SI),
and by extension most of the Western world, is the second,
defined as about 9 billion oscillations of the caesium atom.

WIKI: https://en.wikipedia.org/wiki/Unit_of_time
"""

time_chart: dict[str, float] = {
    "seconds": 1.0,
    "minutes": 60.0,  # 1 minute = 60 sec
    "hours": 3600.0,  # 1 hour = 60 minutes = 3600 seconds
    "days": 86400.0,  # 1 day = 24 hours = 1440 min = 86400 sec
    "weeks": 604800.0,  # 1 week=7d=168hr=10080min = 604800 sec
}

time_chart_inverse: dict[str, float] = {
    "seconds": 1.0,
    "minutes": 1 / 60.0,  # 1 minute = 1/60 hours
    "hours": 1 / 3600.0,  # 1 hour = 1/3600 days
    "days": 1 / 86400.0,  # 1 day = 1/86400 weeks
    "weeks": 1 / 604800.0,  # 1 week = 1/604800 seconds
}


def convert_time(time_value: float, unit_from: str, unit_to: str) -> float:
    """
    Convert time from one unit to another using the time_chart above.

    >>> convert_time(3600, "seconds", "hours")
    1.0
    >>> convert_time(1, "days", "hours")
    24.0
    >>> convert_time(120, "minutes", "seconds")
    7200.0
    >>> convert_time(2, "weeks", "days")
    14.0
    >>> convert_time(0.5, "hours", "minutes")
    30.0
    """
    if unit_to not in time_chart or unit_from not in time_chart_inverse:
        msg = (
            f"Incorrect 'from_type' or 'to_type' value: {unit_from!r}, {unit_to!r}\n"
            f"Valid values are: {', '.join(time_chart_inverse)}"
        )
        raise ValueError(msg)
    return round(time_value * time_chart[unit_from] * time_chart_inverse[unit_to], 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(convert_time(3600, "seconds", "hours"))
