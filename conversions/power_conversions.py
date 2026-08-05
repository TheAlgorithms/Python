"""
convert power units between
watts, kilowatts, megawatts, gigawatts, horsepower
"""


def watts_to_kilowatts(watts: float) -> float:
    """
    >>> watts_to_kilowatts(1000)
    1.0
    """
    return watts / 1000


def watts_to_megawatts(watts: float) -> float:
    """
    >>> watts_to_megawatts(1000000)
    1.0
    """
    return watts / 1000000


def watts_to_gigawatts(watts: float) -> float:
    """
    >>> watts_to_gigawatts(1000000000)
    1.0
    """
    return watts / 1000000000


def watts_to_horsepower(watts: float) -> float:
    """
    >>> watts_to_horsepower(745.699872)
    1.0
    """
    return watts / 745.699872


def kilowatts_to_watts(kilowatts: float) -> float:
    """
    >>> kilowatts_to_watts(2.2)
    2200.0
    """
    return kilowatts * 1000


def kilowatts_to_megawatts(kilowatts: float) -> float:
    """
    >>> kilowatts_to_megawatts(1000)
    1.0
    """
    return kilowatts / 1000


def kilowatts_to_gigawatts(kilowatts: float) -> float:
    """
    >>> kilowatts_to_gigawatts(1000000)
    1.0
    """
    return kilowatts / 1000000


def kilowatts_to_horsepower(kilowatts: float) -> float:
    """
    >>> kilowatts_to_horsepower(745.699872)
    1.0
    """
    return kilowatts / 745.699872


def megawatts_to_watts(megawatts: float) -> float:
    """
    >>> megawatts_to_watts(2.2)
    2200000.0
    """
    return megawatts * 1000000


def megawatts_to_kilowatts(megawatts: float) -> float:
    """
    >>> megawatts_to_kilowatts(2.2)
    2200.0
    """
    return megawatts * 1000


def megawatts_to_gigawatts(megawatts: float) -> float:
    """
    >>> megawatts_to_gigawatts(1000)
    1.0
    """
    return megawatts / 1000


def megawatts_to_horsepower(megawatts: float) -> float:
    """
    >>> megawatts_to_horsepower(745.699872)
    1.0
    """
    return megawatts / 745.699872


def gigawatts_to_watts(gigawatts: float) -> float:
    """
    >>> gigawatts_to_watts(2.2)
    2200000000.0
    """
    return gigawatts * 1000000000


def gigawatts_to_kilowatts(gigawatts: float) -> float:
    """
    >>> gigawatts_to_kilowatts(1000.2)
    1000200000.0
    """
    return gigawatts * 1000000


def gigawatts_to_megawatts(gigawatts: float) -> float:
    """
    >>> gigawatts_to_megawatts(1000.2)
    1000200.0
    """
    return gigawatts * 1000


def gigawatts_to_horsepower(gigawatts: float) -> float:
    """
    >>> gigawatts_to_horsepower(745.699872)
    1.0
    """
    return gigawatts / 745.699872


def horsepower_to_watts(horsepower: float) -> float:
    """
    >>> horsepower_to_watts(2)
    1491.399744
    """
    return horsepower * 745.699872


def horsepower_to_kilowatts(horsepower: float) -> float:
    """
    >>> horsepower_to_kilowatts(1000)
    745.699872
    """
    return horsepower * 745.699872 / 1000


def horsepower_to_megawatts(horsepower: float) -> float:
    """
    >>> horsepower_to_megawatts(1000)
    0.745699872
    """
    return horsepower * 745.699872 / 1000000


def horsepower_to_gigawatts(horsepower: float) -> float:
    """
    >>> horsepower_to_gigawatts(1000)
    0.0007456998719999999
    """
    return horsepower * 745.699872 / 1000000000


if __name__ == "__main__":
    import doctest

    doctest.testmod()
