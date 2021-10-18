"""
Conversion of length units.
Available Units:- Metre,Kilometre,Feet,Inch,Centimeter,Yard,Foot,Mile,Millimeter

USAGE :
-> Import this file into their respective project.
-> Use the function length_conversion() for conversion of length units.
-> Parameters :
    -> from_type : From which type you want to convert
    -> to_type : To which type you want to convert
    -> value : the value which you want to convert

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

METER_CHART: dict[str, float] = {
    "meter": 1,
    "kilometer": 0.001,
    "feet": 3.28084,
    "inch": 39.3701,
    "centimeter": 100,
    "yard": 1.09361,
    "foot": 3.28084,
    "mile": 0.000621371,
    "millimeter": 1000,
}

LENGTH_TYPE_CHART: dict[str, float] = {
    "meter": 1,
    "kilometer": 1000,
    "feet": 0.3048,
    "inch": 0.0254,
    "centimeter": 0.01,
    "yard": 0.9144,
    "foot": 0.3048,
    "mile": 1609.34,
    "millimeter": 0.001,
}


def length_conversion(from_type: str, to_type: str, value: float) -> float:
    """
    Conversion of length unit with the help of LENGTH_CHART
     "meter": 1,
    "kilometer": 0.001,
    "feet": 3.28084,
    "inch": 39.3701,
    "centimeter": 100,
    "yard": 1.09361,
    "foot": 3.28084,
    "mile": 0.000621371,
    "millimeter": 1000,
    >>> length_conversion("meter","feet",4)
    13.12336
    >>> length_conversion("meter","kilometer",1)
    0.001
    >>> length_conversion("kilometer","inch",1)
    39370.1
    >>> length_conversion("kilometer","mile",3)
    1.8641130000000001
    >>> length_conversion("feet","meter",2)
    0.6096
    >>> length_conversion("feet","yard",4)
    1.333329312
    >>> length_conversion("inch","meter",1)
    0.0254
    >>> length_conversion("inch","mile",2)
    3.15656468e-05
    >>> length_conversion("centimeter","millimeter",2)
    20.0
    >>> length_conversion("centimeter","yard",2)
    0.0218722
    >>> length_conversion("yard","meter",4)
    3.6576
    >>> length_conversion("yard","kilometer",4)
    0.0036576
    >>> length_conversion("foot","meter",3)
    0.9144000000000001
    >>> length_conversion("foot","inch",3)
    36.00001944
    >>> length_conversion("mile","kilometer",4)
    6.43736
    >>> length_conversion("mile","inch",2)
    126719.753468
    >>> length_conversion("millimeter","centimeter",3)
    0.3
    >>> length_conversion("millimeter","inch",3)
    0.1181103
    >>> length_conversion("wrongUnit","inch",4 )
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.length_conversion[18]>", line 1, in <module>
        length_conversion("wrongUnit","inch",4 )
      File "<string>", line 104, in length_conversion
    ValueError: Invalid 'from_type' or 'to_type' value: 'wrongUnit', 'inch'
    Supported values are: meter, kilometer, feet, inch, centimeter, yard, foot, mile, millimeter
    """
    if to_type not in METER_CHART or from_type not in LENGTH_TYPE_CHART:
        raise ValueError(
            f"Invalid 'from_type' or 'to_type' value: {from_type!r}, {to_type!r}\n"
            f"Supported values are: {', '.join(LENGTH_TYPE_CHART)}"
        )
    return value * METER_CHART[to_type] * LENGTH_TYPE_CHART[from_type]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
