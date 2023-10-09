def timeConversion(sec: int) -> int:
    """
    This simple python program converts seconds to days, hours, minutes and seconds

    Usage examples:
    >>> timeConversion(458964)
    (5, 7, 29, 24)
    >>> timeConversion(185683)
    (2, 3, 34, 43)
    >>> timeConversion(76896)
    (0, 21, 21, 36)
    >>> timeConversion(7896543)
    (91, 9, 29, 3)
    >>> timeConversion(1000000)
    (11, 13, 46, 40)
    >>> timeConversion(256)
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
    seconds = 256  # assign the input here
    print(
        f"{timeConversion(seconds)[0]} days {timeConversion(seconds)[1]} hours\
 {timeConversion(seconds)[2]} minutes {timeConversion(seconds)[3]} seconds"
    )
