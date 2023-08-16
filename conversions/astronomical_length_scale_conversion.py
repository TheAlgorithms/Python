"""
Conversion of length units.
Available Units:
Metre, Kilometre, Megametre, Gigametre,
Terametre, Petametre, Exametre, Zettametre, Yottametre

USAGE :
-> Import this file into their respective project.
-> Use the function length_conversion() for conversion of length units.
-> Parameters :
    -> value : The number of from units you want to convert
    -> from_type : From which type you want to convert
    -> to_type : To which type you want to convert

REFERENCES :
-> Wikipedia reference: https://en.wikipedia.org/wiki/Meter
-> Wikipedia reference: https://en.wikipedia.org/wiki/Kilometer
-> Wikipedia reference: https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)
"""

UNIT_SYMBOL = {
    "meter": "m",
    "kilometer": "km",
    "megametre": "Mm",
    "gigametre": "Gm",
    "terametre": "Tm",
    "petametre": "Pm",
    "exametre": "Em",
    "zettametre": "Zm",
    "yottametre": "Ym",
}
# Exponent of the factor(meter)
METRIC_CONVERSION = {
    "m": 0,
    "km": 3,
    "Mm": 6,
    "Gm": 9,
    "Tm": 12,
    "Pm": 15,
    "Em": 18,
    "Zm": 21,
    "Ym": 24,
}


def length_conversion(value: float, from_type: str, to_type: str) -> float:
    """
    Conversion between astronomical length units.

    >>> length_conversion(1, "meter", "kilometer")
    0.001
    >>> length_conversion(1, "meter", "megametre")
    1e-06
    >>> length_conversion(1, "gigametre", "meter")
    1000000000
    >>> length_conversion(1, "gigametre", "terametre")
    0.001
    >>> length_conversion(1, "petametre", "terametre")
    1000
    >>> length_conversion(1, "petametre", "exametre")
    0.001
    >>> length_conversion(1, "terametre", "zettametre")
    1e-09
    >>> length_conversion(1, "yottametre", "zettametre")
    1000
    >>> length_conversion(4, "wrongUnit", "inch")
    Traceback (most recent call last):
      ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'.
    Conversion abbreviations are: m, km, Mm, Gm, Tm, Pm, Em, Zm, Ym
    """

    from_sanitized = from_type.lower().strip("s")
    to_sanitized = to_type.lower().strip("s")

    from_sanitized = UNIT_SYMBOL.get(from_sanitized, from_sanitized)
    to_sanitized = UNIT_SYMBOL.get(to_sanitized, to_sanitized)

    if from_sanitized not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'from_type' value: {from_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    if to_sanitized not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'to_type' value: {to_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    from_exponent = METRIC_CONVERSION[from_sanitized]
    to_exponent = METRIC_CONVERSION[to_sanitized]
    exponent = 1

    if from_exponent > to_exponent:
        exponent = from_exponent - to_exponent
    else:
        exponent = -(to_exponent - from_exponent)

    return value * pow(10, exponent)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
