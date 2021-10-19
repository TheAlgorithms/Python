"""
Conversion of length units.
Available Units:- Metre,Kilometre,Feet,Inch,Centimeter,Yard,Foot,Mile,Millimeter

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
-> Wikipedia reference: https://en.wikipedia.org/wiki/Feet
-> Wikipedia reference: https://en.wikipedia.org/wiki/Inch
-> Wikipedia reference: https://en.wikipedia.org/wiki/Centimeter
-> Wikipedia reference: https://en.wikipedia.org/wiki/Yard
-> Wikipedia reference: https://en.wikipedia.org/wiki/Foot
-> Wikipedia reference: https://en.wikipedia.org/wiki/Mile
-> Wikipedia reference: https://en.wikipedia.org/wiki/Millimeter
"""

from collections import namedtuple

from_to = namedtuple("from_to", "from_ to")

METRIC_CONVERSION = {
    "meter": from_to(1, 1),
    "kilometer": from_to(1000, 0.001),
    "feet": from_to(0.3048, 3.28084),
    "inch": from_to(0.0254, 39.3701),
    "centimeter": from_to(0.01, 100),
    "yard": from_to(0.9144, 1.09361),
    "foot": from_to(0.3048, 3.28084),
    "mile": from_to(1609.34, 0.000621371),
    "millimeter": from_to(0.001, 1000),
}


def length_conversion(value: float, from_type: str, to_type: str) -> float:
    """
    Conversion between length units.

    >>> length_conversion(4, "meter", "feet")
    13.12336
    >>> length_conversion(1, "meter", "kilometer")
    0.001
    >>> length_conversion(1, "kilometer", "inch")
    39370.1
    >>> length_conversion(3, "kilometer", "mile")
    1.8641130000000001
    >>> length_conversion(2, "feet", "meter")
    0.6096
    >>> length_conversion(4, "feet", "yard")
    1.333329312
    >>> length_conversion(1, "inch", "meter")
    0.0254
    >>> length_conversion(2, "inch", "mile")
    3.15656468e-05
    >>> length_conversion(2, "centimeter", "millimeter")
    20.0
    >>> length_conversion(2, "centimeter", "yard")
    0.0218722
    >>> length_conversion(4, "yard", "meter")
    3.6576
    >>> length_conversion(4, "yard", "kilometer")
    0.0036576
    >>> length_conversion(3, "foot", "meter")
    0.9144000000000001
    >>> length_conversion(3, "foot", "inch")
    36.00001944
    >>> length_conversion(4, "mile", "kilometer")
    6.43736
    >>> length_conversion(2, "mile", "inch")
    126719.753468
    >>> length_conversion(3, "millimeter", "centimeter")
    0.3
    >>> length_conversion(3, "millimeter", "inch")
    0.1181103
    >>> length_conversion(4, "wrongUnit", "inch")
    Traceback (most recent call last):
      ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'  Supported values are:
    meter, kilometer, feet, inch, centimeter, yard, foot, mile, millimeter
    """
    if from_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    if to_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    return value * METRIC_CONVERSION[from_type].from_ * METRIC_CONVERSION[to_type].to


if __name__ == "__main__":
    import doctest

    doctest.testmod()
