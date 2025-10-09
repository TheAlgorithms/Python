"""
Conversion of volume units.
Available Units:- Cubic metre,Litre,KiloLitre,Gallon,Cubic yard,Cubic foot,cup
USAGE :
-> Import this file into their respective project.
-> Use the function length_conversion() for conversion of volume units.
-> Parameters :
    -> value : The number of from units you want to convert
    -> from_type : From which type you want to convert
    -> to_type : To which type you want to convert
REFERENCES :
-> Wikipedia reference: https://en.wikipedia.org/wiki/Cubic_metre
-> Wikipedia reference: https://en.wikipedia.org/wiki/Litre
-> Wikipedia reference: https://en.wiktionary.org/wiki/kilolitre
-> Wikipedia reference: https://en.wikipedia.org/wiki/Gallon
-> Wikipedia reference: https://en.wikipedia.org/wiki/Cubic_yard
-> Wikipedia reference: https://en.wikipedia.org/wiki/Cubic_foot
-> Wikipedia reference: https://en.wikipedia.org/wiki/Cup_(unit)
"""

from typing import NamedTuple


class FromTo(NamedTuple):
    from_factor: float
    to_factor: float


METRIC_CONVERSION = {
    "cubic meter": FromTo(1, 1),
    "litre": FromTo(0.001, 1000),
    "kilolitre": FromTo(1, 1),
    "gallon": FromTo(0.00454, 264.172),
    "cubic yard": FromTo(0.76455, 1.30795),
    "cubic foot": FromTo(0.028, 35.3147),
    "cup": FromTo(0.000236588, 4226.75),
}


def volume_conversion(value: float, from_type: str, to_type: str) -> float:
    """
    Conversion between volume units.
    >>> volume_conversion(4, "cubic meter", "litre")
    4000
    >>> volume_conversion(1, "litre", "gallon")
    0.264172
    >>> volume_conversion(1, "kilolitre", "cubic meter")
    1
    >>> volume_conversion(3, "gallon", "cubic yard")
    0.017814279
    >>> volume_conversion(2, "cubic yard", "litre")
    1529.1
    >>> volume_conversion(4, "cubic foot", "cup")
    473.396
    >>> volume_conversion(1, "cup", "kilolitre")
    0.000236588
    >>> volume_conversion(4, "wrongUnit", "litre")
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'  Supported values are:
    cubic meter, litre, kilolitre, gallon, cubic yard, cubic foot, cup
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
    return (
        value
        * METRIC_CONVERSION[from_type].from_factor
        * METRIC_CONVERSION[to_type].to_factor
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
