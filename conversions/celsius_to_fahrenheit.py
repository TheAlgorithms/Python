""" Convert temperature from Celsius to Fahrenheit """


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert a given value from Celsius to Fahrenheit and round it to 2 decimal places.

    >>> print(celsius_to_fahrenheit(-40))
    -40.0
    >>> print(celsius_to_fahrenheit(-20))
    -4.0
    >>> print(celsius_to_fahrenheit(0))
    32.0
    >>> print(celsius_to_fahrenheit(20))
    68.0
    >>> print(celsius_to_fahrenheit(40))
    104.0
    >>> print(celsius_to_fahrenheit("celsius"))
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """

    celsius = float(celsius)
    return round((celsius * 9 / 5) + 32, 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
