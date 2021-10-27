from __future__ import annotations

from calendar import day_name
from datetime import datetime

"""
Family of functions for calculating the day of week name from a date
"""


def day_of_week(datetime_obj: datetime) -> str:
    """
    Calculates the day name of the given datetime object
    :param datetime_obj:
    :return: String
    >>> day_of_week(datetime(year=2035, month=8, day=7))
    'Tuesday'
    >>> day_of_week(datetime(year=2021, month=8, day=7))
    'Saturday'
    >>> day_of_week(datetime(year=2021, month=8, day=1))
    'Sunday'
    >>> day_of_week(datetime(year=2021, month=1, day=1))
    'Friday'
    >>> day_of_week(datetime(year=2021, month=1, day=31))
    'Sunday'
    """
    day_of_week: int = datetime_obj.weekday()  # Monday = 0 .. Sunday = 6
    return day_name[day_of_week]


def day_of_week_fmt(date_string: str, format: str = "%Y%m%d") -> str:
    """
    Calculates the day name of the given date string decoded by format.

    See time.strptime for format parameters.

    :param date_string: date in dd/mm/yyyy format
    :param format: strptime compatible date format
    :return: String

    >>> day_of_week_fmt("20211026")
    'Tuesday'
    >>> day_of_week_fmt("2021/10/26", "%Y/%m/%d")
    'Tuesday'
    >>> day_of_week_fmt("2021-10-26", "%Y-%m-%d")
    'Tuesday'
    >>> day_of_week_fmt("7/8/2021", "%d/%m/%Y")
    'Saturday'
    >>> day_of_week_fmt("7/8/2021", "%m/%d/%Y")
    'Thursday'
    """
    datetime_obj = datetime.strptime(date_string, format)
    return day_of_week(datetime_obj)


def day_of_week_dmy(date_string: str) -> str:
    """
    Calculates the day name of the given date string in day/month/year format

    :param datestring: date in dd/mm/yyyy format
    :return: String
    >>> day_of_week_dmy("7/8/2035")
    'Tuesday'
    >>> day_of_week_dmy("7/8/2021")
    'Saturday'
    >>> day_of_week_dmy("7/08/2021")
    'Saturday'
    >>> day_of_week_dmy("07/8/2021")
    'Saturday'
    >>> day_of_week_dmy("07/08/2021")
    'Saturday'
    >>> day_of_week_dmy("1/1/2021")
    'Friday'
    >>> day_of_week_dmy("31/1/2021")
    'Sunday'
    """
    return day_of_week_fmt(date_string, format="%d/%m/%Y")


def day_of_week_mdy(date_string: str) -> str:
    """
    Calculates the day name of the given date string.
    :param date_mdy: date in mm/dd/yyyy format
    :return: String
    >>> day_of_week_mdy("8/7/2035")
    'Tuesday'
    >>> day_of_week_mdy("8/7/2021")
    'Saturday'
    >>> day_of_week_mdy("8/07/2021")
    'Saturday'
    >>> day_of_week_mdy("1/31/2021")
    'Sunday'
    >>> day_of_week_mdy("01/31/2021")
    'Sunday'
    """
    return day_of_week_fmt(date_string, format="%m/%d/%Y")


def day_of_week_ymd(date_string: str) -> str:
    """
    >>> day_of_week_ymd("2035/07/08")
    'Sunday'
    >>> day_of_week_ymd("2021/7/8")
    'Thursday'
    >>> day_of_week_ymd("2021/1/1")
    'Friday'
    """
    return day_of_week_fmt(date_string, format="%Y/%m/%d")


if __name__ == "__main__":
    print("Tuesday August 7, 2035:\n    ",
          day_of_week_fmt("7/8/2035", format="%d/%m/%Y"),
          day_of_week_fmt("8/07/2035", format="%m/%d/%Y"),
          day_of_week_fmt("2035-08-07", format="%Y-%m-%d"),
          day_of_week_fmt("20350807"),
          day_of_week_dmy("7/8/2035"),
          day_of_week_mdy("8/7/2035"),
          day_of_week_ymd("2035/08/07"))

    print("Sunday August 7, 2021:\n    ",
          day_of_week_fmt("7/8/2021", format="%d/%m/%Y"),
          day_of_week_fmt("8/07/2021", format="%m/%d/%Y"),
          day_of_week_fmt("2021-08-07", format="%Y-%m-%d"),
          day_of_week_fmt("20210807"),
          day_of_week_dmy("7/8/2021"),
          day_of_week_mdy("8/7/2021"),
          day_of_week_ymd("2021/08/07"))

    print("Friday January 1, 2021:\n    ",
          day_of_week_fmt("1/1/2021", format="%d/%m/%Y"),
          day_of_week_fmt("1/1/2021", format="%m/%d/%Y"),
          day_of_week_fmt("2021-01-01", format="%Y-%m-%d"),
          day_of_week_fmt("20210101"),
          day_of_week_dmy("1/1/2021"),
          day_of_week_mdy("1/1/2021"),
          day_of_week_ymd("2021/01/1"))

    print("Friday October 1, 2021:\n    ",
          day_of_week_fmt("1/10/2021", format="%d/%m/%Y"),
          day_of_week_fmt("10/1/2021", format="%m/%d/%Y"),
          day_of_week_fmt("2021-10-01", format="%Y-%m-%d"),
          day_of_week_fmt("20211001"),
          day_of_week_dmy("1/10/2021"),
          day_of_week_mdy("10/1/2021"),
          day_of_week_ymd("2021/10/01"))
