def time_conversion(sec: int) -> tuple:
    """
    This simple python program converts seconds to days, hours, minutes and seconds

    Usage examples:
    >>> time_conversion(458964)
    (5, 7, 29, 24)
    >>> time_conversion(185683)
    (2, 3, 34, 43)
    >>> time_conversion(76896)
    (0, 21, 21, 36)
    >>> time_conversion(7896543)
    (91, 9, 29, 3)
    >>> time_conversion(1000000)
    (11, 13, 46, 40)
    >>> time_conversion(256)
    (0, 0, 4, 16)
    """
    days = sec // 86400
    sec = sec % 86400
    hours = sec // 3600
    sec = sec % 3600
    minutes = sec // 60
    seconds = sec % 60

    return days, hours, minutes, seconds


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    seconds = 256  # assign the input here
    print(
        f"{time_conversion(seconds)[0]} days {time_conversion(seconds)[1]} hours\
 {time_conversion(seconds)[2]} minutes {time_conversion(seconds)[3]} seconds"
    )
