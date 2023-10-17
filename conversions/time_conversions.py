from datetime import datetime, timedelta


def seconds_to_minutes(seconds: int) -> int:
    """
    Convert seconds to minutes.

    Args:
        seconds (int): The number of seconds.

    Returns:
        int: The equivalent number of minutes.

    >>> seconds_to_minutes(60)
    1
    >>> seconds_to_minutes(300)
    5
    >>> seconds_to_minutes(3600)
    60
    """
    minutes = seconds // 60
    return minutes


def minutes_to_hours(minutes: int) -> int:
    """
    Convert minutes to hours.

    Args:
        minutes (int): The number of minutes.

    Returns:
        int: The equivalent number of hours.

    >>> minutes_to_hours(60)
    1
    >>> minutes_to_hours(120)
    2
    >>> minutes_to_hours(180)
    3
    """
    hours = minutes // 60
    return hours


def hours_to_days(hours: int) -> int:
    """
    Convert hours to days.

    Args:
        hours (int): The number of hours.

    Returns:
        int: The equivalent number of days.

    >>> hours_to_days(24)
    1
    >>> hours_to_days(48)
    2
    >>> hours_to_days(72)
    3
    """
    days = hours // 24
    return days


def string_to_datetime(date_str: str, date_format: str = "%Y-%m-%d") -> datetime:
    """
    Convert a date string to a datetime object.

    Args:
        date_str (str): The date string.
        date_format (str, optional): The format of the date string. Default is '%Y-%m-%d'.

    Returns:
        datetime: The datetime object.

    >>> date_str = "2023-10-15"
    >>> date_obj = string_to_datetime(date_str)
    >>> date_obj.strftime('%Y-%m-%d')
    '2023-10-15'
    """
    date_obj = datetime.strptime(date_str, date_format)
    return date_obj


def datetime_to_string(date_obj: datetime, date_format: str = "%d/%m/%Y") -> str:
    """
    Convert a datetime object to a date string.

    Args:
        date_obj (datetime): The datetime object.
        date_format (str, optional): The desired format of the date string. Default is '%d/%m/%Y'.

    Returns:
        str: The date string.

    >>> date_obj = datetime(2023, 10, 15)
    >>> datetime_to_string(date_obj)
    '15/10/2023'
    """
    date_string = date_obj.strftime(date_format)
    return date_string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
