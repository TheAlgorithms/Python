def timeconversion(sec: int) -> int:
    """
    This simple python program converts seconds to days, hours, minutes and seconds

    Usage examples:
    >>> timeconversion(458964)
    (5, 7, 29, 24)
    >>> timeconversion(185683)
    (2, 3, 34, 43)
    >>> timeconversion(76896)
    (0, 21, 21, 36)
    >>> timeconversion(7896543)
    (91, 9, 29, 3)
    >>> timeconversion(1000000)
    (11, 13, 46, 40)
    >>> timeconversion(256)
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
        f"{timeconversion(seconds)[0]} days {timeconversion(seconds)[1]} hours\
 {timeconversion(seconds)[2]} minutes {timeconversion(seconds)[3]} seconds"
    )
