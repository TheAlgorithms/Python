"""
Convert speed units

https://en.wikipedia.org/wiki/Kilometres_per_hour
https://en.wikipedia.org/wiki/Miles_per_hour
https://en.wikipedia.org/wiki/Knot_(unit)
https://en.wikipedia.org/wiki/Metre_per_second
"""

speed_chart: dict[str, float] = {
    "km/h": 1.0,
    "m/s": 3.6,
    "mph": 1.609344,
    "knot": 1.852,
}

speed_chart_inverse: dict[str, float] = {
    "km/h": 1.0,
    "m/s": 0.277777778,
    "mph": 0.621371192,
    "knot": 0.539956803,
}


def convert_speed(speed: float, unit_from: str, unit_to: str) -> float:
    """
    Convert speed from one unit to another using the speed_chart above.

    "km/h": 1.0,
    "m/s": 3.6,
    "mph": 1.609344,
    "knot": 1.852,

    >>> convert_speed(100, "km/h", "m/s")
    27.778
    >>> convert_speed(100, "km/h", "mph")
    62.137
    >>> convert_speed(100, "km/h", "knot")
    53.996
    >>> convert_speed(100, "m/s", "km/h")
    360.0
    >>> convert_speed(100, "m/s", "mph")
    223.694
    >>> convert_speed(100, "m/s", "knot")
    194.384
    >>> convert_speed(100, "mph", "km/h")
    160.934
    >>> convert_speed(100, "mph", "m/s")
    44.704
    >>> convert_speed(100, "mph", "knot")
    86.898
    >>> convert_speed(100, "knot", "km/h")
    185.2
    >>> convert_speed(100, "knot", "m/s")
    51.444
    >>> convert_speed(100, "knot", "mph")
    115.078
    """
    if unit_to not in speed_chart or unit_from not in speed_chart_inverse:
        raise ValueError(
            f"Incorrect 'from_type' or 'to_type' value: {unit_from!r}, {unit_to!r}\n"
            f"Valid values are: {', '.join(speed_chart_inverse)}"
        )
    return round(speed * speed_chart[unit_from] * speed_chart_inverse[unit_to], 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
