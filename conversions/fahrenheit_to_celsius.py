""" Convert temperature from Fahrenheit to Celsius """


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert a given value from Fahrenheit to Celsius and round it to 2 decimal places.

    >>> print(fahrenheit_to_celsius(0))
    -17.78
    >>> print(fahrenheit_to_celsius(20))
    -6.67
    >>> print(fahrenheit_to_celsius(40))
    4.44
    >>> print(fahrenheit_to_celsius(60))
    15.56
    >>> print(fahrenheit_to_celsius(80))
    26.67
    >>> print(fahrenheit_to_celsius(100))
    37.78
    >>> print(fahrenheit_to_celsius("fahrenheit"))
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    fahrenheit = float(fahrenheit)
    return round((fahrenheit - 32) * 5 / 9, 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
