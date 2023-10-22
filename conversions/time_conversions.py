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
    >>> convert_time(1, "days", "hours")
    24.0
    >>> convert_time(120, "minutes", "seconds")
    7200.0
    >>> convert_time(2, "weeks", "days")
    14.0
    >>> convert_time(0.5, "hours", "minutes")
    30.0
    >>> convert_time(-3600, "seconds", "hours")
    Error: 'time_value' must be a non-negative number.
    >>> convert_time("Hello", "hours", "minutes")
    Error: 'time_value' must be a non-negative number.
    >>> convert_time([0, 1, 2], "weeks", "days")
    Error: 'time_value' must be a non-negative number.
    >>> convert_time(50, "HOURS", "days")
    2.083
    >>> convert_time(50, "hours", "YEARS")
    0.006
    """
    if unit_to.lower() not in time_chart or unit_from.lower() not in time_chart_inverse:
        valid_units = ", ".join(time_chart_inverse)
        print(
            f"Error: Invalid unit: "
            f"{unit_from if unit_from.lower() not in time_chart_inverse else unit_to}."
            f" Valid units are {valid_units}."
        )

        return None

    if not isinstance(time_value, (int, float)) or time_value < 0:
        print("Error: 'time_value' must be a non-negative number.")
        return None
    return round(
        time_value
        * time_chart[unit_from.lower()]
        * time_chart_inverse[unit_to.lower()],
        3,
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{convert_time(3600,'seconds', 'hours') = }")
    print(f"{convert_time(360, 'days', 'months') = }")
    print(f"{convert_time(360, 'months', 'years') = }")
    print(f"{convert_time(360, 'cool', 'months') = }")
