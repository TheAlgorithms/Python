""" Convert temperature from Celsius to Fahrenheit """


def celsius_to_fahrenheit(celsius):
    """
    Convert a given value from Celsius to Fahrenheit

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
    >>> print(celsius_to_fahrenheit("40"))
    Traceback (most recent call last):
    ...
    TypeError: 'str' object cannot be interpreted as integer
    """

    if type(celsius) == str:
        """
        Check whether given value is string and raise Type Error
        """
        raise TypeError("'str' object cannot be interpreted as integer")

    fahrenheit = (celsius * 9 / 5) + 32  # value converted from celsius to fahrenheit
    return fahrenheit


if __name__ == "__main__":
    import doctest
    doctest.testmod()
