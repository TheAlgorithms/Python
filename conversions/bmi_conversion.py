"""Converts height and mass to Body Mass Index"""


def metric_units_bmi(kg: int, cm: int) -> int:
    """
    Convert mass in kilograms and height in centimetres to Body Mass Index
    >>> metric_units_bmi(50, 160)
    19.53
    >>> metric_units_bmi(80, 175)
    26.12
    >>> metric_units_bmi(20, 0)
    "Cm couldn't be 0"
    """
    if cm == 0:
        return "Height couldn't be 0"

    metre_square = (cm / 100) ** 2
    return round(kg / metre_square, 2)


def us_units_bmi(pounds: int, inches: int) -> int:
    """
    Convert mass in pounds and height in inches to Body Mass Index
    >>> us_units_bmi(200, 75)
    25.0
    >>> us_units_bmi(130, 65)
    21.63
    >>> us_units_bmi(40, 0)
    "Inches couldn't be 0"
    """
    if inches == 0:
        return "Height couldn't be 0"

    inches_square = inches ** 2
    return round(703 * (pounds / inches_square), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
