""" Convert between different units of temperature """


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert a given value from Celsius to Fahrenheit and round it to 2 decimal places.

    >>> celsius_to_fahrenheit(-40.0)
    -40.0
    >>> celsius_to_fahrenheit(-20.0)
    -4.0
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(20)
    68.0
    >>> celsius_to_fahrenheit("40")
    104.0
    >>> celsius_to_fahrenheit("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round((float(celsius) * 9 / 5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert a given value from Fahrenheit to Celsius and round it to 2 decimal places.

    >>> fahrenheit_to_celsius(0)
    -17.78
    >>> fahrenheit_to_celsius(20.0)
    -6.67
    >>> fahrenheit_to_celsius(40.0)
    4.44
    >>> fahrenheit_to_celsius(60)
    15.56
    >>> fahrenheit_to_celsius(80)
    26.67
    >>> fahrenheit_to_celsius("100")
    37.78
    >>> fahrenheit_to_celsius("fahrenheit")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    return round((float(fahrenheit) - 32) * 5 / 9, 2)


def celsius_to_kelvin(celsius: float) -> float:
    """
    Convert a given value from Celsius to Kelvin and round it to 2 decimal places.

    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(20.0)
    293.15
    >>> celsius_to_kelvin("40")
    313.15
    >>> celsius_to_kelvin("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round(float(celsius) + 273.15, 2)


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Convert a given value from Kelvin to Celsius and round it to 2 decimal places.

    >>> kelvin_to_celsius(273.15)
    0.0
    >>> kelvin_to_celsius(300)
    26.85
    >>> kelvin_to_celsius("315.5")
    42.35
    >>> kelvin_to_celsius("kelvin")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'kelvin'
    """
    return round(float(kelvin) - 273.15, 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
