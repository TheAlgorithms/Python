"""
Functions useful for conversion fo weight units
"""


def weightConversion(from_type: str, to_type: str, value: float) -> any:
    """
    Conversion of weight unit with the help of kilogram_chart

    "kilogram" : 1,
    "gram" : pow(10, 3),
    "milligram" : pow(10, 6),
    "metric-ton" : pow(10, -3),
    "long-ton" : 0.0009842073,
    "short-ton" : 0.0011023122,
    "pound" : 2.2046244202,
    "ounce" : 35.273990723,
    "carrat" : 5000,
    "atomic-mass-unit" : 6.022136652E+26

    Wikipedia reference: https://en.wikipedia.org/wiki/Conversion_of_units


    >>> weightConversion("kilogram","kilogram",5)
    5
    >>> weightConversion("kilogram","carrat",5)
    25000
    >>> weightConversion("ounce","short-ton",3)
    9.37499991417e-05
    """
    kilogram_chart = {
        "kilogram": 1,
        "gram": pow(10, 3),
        "milligram": pow(10, 6),
        "metric-ton": pow(10, -3),
        "long-ton": 0.0009842073,
        "short-ton": 0.0011023122,
        "pound": 2.2046244202,
        "ounce": 35.273990723,
        "carrat": 5000,
        "atomic-mass-unit": 6.022136652e26,
    }

    weight_type_chart = {
        "kilogram": 1,
        "gram": pow(10, -3),
        "milligram": pow(10, -6),
        "metric-ton": pow(10, 3),
        "long-ton": 1016.04608,
        "short-ton": 907.184,
        "pound": 0.453592,
        "ounce": 0.0283495,
        "carrat": 0.0002,
        "atomic-mass-unit": 1.660540199e-27,
    }

    return value * kilogram_chart.get(to_type) * weight_type_chart.get(from_type)


if __name__ == "__main__":

    import doctest

    doctest.testmod()
