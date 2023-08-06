"""
Conversion of pressure units.
Available Units:- Pascal,Bar,Kilopascal,Megapascal,psi(pound per square inch),
inHg(in mercury column),torr,atm
USAGE :
-> Import this file into their respective project.
-> Use the function pressure_conversion() for conversion of pressure units.
-> Parameters :
    -> value : The number of from units you want to convert
    -> from_type : From which type you want to convert
    -> to_type : To which type you want to convert
REFERENCES :
-> Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)
-> Wikipedia reference: https://en.wikipedia.org/wiki/Pound_per_square_inch
-> Wikipedia reference: https://en.wikipedia.org/wiki/Inch_of_mercury
-> Wikipedia reference: https://en.wikipedia.org/wiki/Torr
-> https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
-> https://msestudent.com/what-are-the-units-of-pressure/
-> https://www.unitconverters.net/pressure-converter.html
"""

from collections import namedtuple

from_to = namedtuple("from_to", "from_ to")

PRESSURE_CONVERSION = {
    "atm": from_to(1, 1),
    "pascal": from_to(0.0000098, 101325),
    "bar": from_to(0.986923, 1.01325),
    "kilopascal": from_to(0.00986923, 101.325),
    "megapascal": from_to(9.86923, 0.101325),
    "psi": from_to(0.068046, 14.6959),
    "inHg": from_to(0.0334211, 29.9213),
    "torr": from_to(0.00131579, 760),
}


def pressure_conversion(value: float, from_type: str, to_type: str) -> float:
    """
    Conversion between pressure units.
    >>> pressure_conversion(4, "atm", "pascal")
    405300
    >>> pressure_conversion(1, "pascal", "psi")
    0.00014401981999999998
    >>> pressure_conversion(1, "bar", "atm")
    0.986923
    >>> pressure_conversion(3, "kilopascal", "bar")
    0.029999991892499998
    >>> pressure_conversion(2, "megapascal", "psi")
    290.074434314
    >>> pressure_conversion(4, "psi", "torr")
    206.85984
    >>> pressure_conversion(1, "inHg", "atm")
    0.0334211
    >>> pressure_conversion(1, "torr", "psi")
    0.019336718261000002
    >>> pressure_conversion(4, "wrongUnit", "atm")
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'  Supported values are:
    atm, pascal, bar, kilopascal, megapascal, psi, inHg, torr
    """
    if from_type not in PRESSURE_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}  Supported values are:\n"
            + ", ".join(PRESSURE_CONVERSION)
        )
    if to_type not in PRESSURE_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(PRESSURE_CONVERSION)
        )
    return (
        value * PRESSURE_CONVERSION[from_type].from_ * PRESSURE_CONVERSION[to_type].to
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
