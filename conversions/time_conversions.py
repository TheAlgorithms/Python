"""
Conversion of time units.
Available Units:- Decade, Year, Month, Day, Week, Minutes, Seconds
USAGE :
-> Import this file into your respective project.
-> Use the function time_conversion() for conversion of time units.
-> Parameters :
    -> value : The number of units you want to convert
    -> from_type : From which type you want to convert
    -> to_type : To which type you want to convert
"""

from typing import NamedTuple


class FromTo(NamedTuple):
    from_factor: float
    to_factor: float


TIME_CONVERSION = {
    "decade": FromTo(315360000, 1/315360000),
    "year": FromTo(31536000, 1/31536000),
    "month": FromTo(2592000, 1/2592000),
    "day": FromTo(86400, 1/86400),
    "week": FromTo(604800,1/604800),
    "minutes": FromTo(60, 1/60),
    "seconds": FromTo(1, 1),
}


def time_conversion(value: float, from_type: str, to_type: str) -> float:
    """
    Conversion between time units.
    >>> time_conversion(4, "decade", "year")
    40.0
    >>> time_conversion(1, "month", "day")
    30.0
    >>> time_conversion(365, "day", "week")
    52.142857142857146
    >>> time_conversion(60, "minutes", "seconds")
    3600
    >>> time_conversion(2, "year", "month")
    24.333333333333332
    >>> time_conversion(1, "wrongUnit", "year")
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'  Supported values are:
    decade, year, month, day, week, minutes, seconds
    """
    if from_type not in TIME_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}  Supported values are:\n"
            + ", ".join(TIME_CONVERSION)
        )
    if to_type not in TIME_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(TIME_CONVERSION)
        )
    return (
        value
        * TIME_CONVERSION[from_type].from_factor
        * TIME_CONVERSION[to_type].to_factor
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
