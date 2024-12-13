#!/bin/python3
# Doomsday algorithm info: https://en.wikipedia.org/wiki/Doomsday_rule

DOOMSDAY_LEAP = [4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
DOOMSDAY_NOT_LEAP = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
WEEK_DAY_NAMES = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}


def get_week_day(year: int, month: int, day: int) -> str:
    """Returns the week-day name out of a given date.

    >>> get_week_day(2020, 10, 24)
    'Saturday'
    >>> get_week_day(2017, 10, 24)
    'Tuesday'
    >>> get_week_day(2019, 5, 3)
    'Friday'
    >>> get_week_day(1970, 9, 16)
    'Wednesday'
    >>> get_week_day(1870, 8, 13)
    'Saturday'
    >>> get_week_day(2040, 3, 14)
    'Wednesday'

    """
    # minimal input check:
    assert len(str(year)) > 2, "year should be in YYYY format"
    assert 1 <= month <= 12, "month should be between 1 to 12"
    assert 1 <= day <= 31, "day should be between 1 to 31"

    # Doomsday algorithm:
    century = year // 100
    century_anchor = (5 * (century % 4) + 2) % 7
    centurian = year % 100
    centurian_m = centurian % 12
    dooms_day = (
        (centurian // 12) + centurian_m + (centurian_m // 4) + century_anchor
    ) % 7
    day_anchor = (
        DOOMSDAY_NOT_LEAP[month - 1]
        if (year % 4 != 0) or ((centurian == 0) and (year % 400 != 0))
        else DOOMSDAY_LEAP[month - 1]
    )
    week_day = (dooms_day + day - day_anchor) % 7
    return WEEK_DAY_NAMES[week_day]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
