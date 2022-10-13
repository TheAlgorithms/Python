"""
Convert speed units

https://en.wikipedia.org/wiki/Kilometres_per_hour
https://en.wikipedia.org/wiki/Miles_per_hour
https://en.wikipedia.org/wiki/Knot_(unit)
https://en.wikipedia.org/wiki/Metre_per_second

"""

def convert_speed(speed: float, unit_from: str, unit_to: str) -> float:
    """
    Return speed units based on input
    
    >>> convert_speed(10, 'm/s', 'km/h')
    36.0

    >>> convert_speed(10, 'km/h', 'm/s')
    2.78
    
    >>> convert_speed(10, 'm/s', 'mph')
    22.37

    >>> convert_speed(10, 'mph', 'm/s')
    4.47

    >>> convert_speed(10, 'km/h', 'mph')
    6.21

    >>> convert_speed(10, 'mph', 'km/h')
    16.09

    >>> convert_speed(10, 'm/s', 'knots')
    19.44

    >>> convert_speed(10, 'knots', 'm/s')
    5.14

    >>> convert_speed(10, 'km/h', 'knots')
    5.4

    >>> convert_speed(10, 'knots', 'km/h')
    18.52

    >>> convert_speed(10, 'mph', 'knots')
    8.69

    >>> convert_speed(10, 'knots', 'mph')
    11.51
    
    >>> convert_speed(abc, 'm/s', 'km/h')
    Traceback (most recent call last):
        ...
    NameError: name 'abc' is not defined

    >>> convert_speed(10, 'abc', 'km/h')
    Traceback (most recent call last):
        ...
    ValueError: invalid literal for int() with base 10: abc
    """
    if unit_from == 'm/s':
        if unit_to == 'km/h':
            return round(speed * 3.6, 2)
        elif unit_to == 'mph':
            return round(speed * 2.23694, 2)
        elif unit_to == 'knots':
            return round(speed * 1.94384, 2)
        else:
            raise ValueError('invalid literal for int() with base 10: ' + unit_to)

    elif unit_from == 'km/h':
        if unit_to == 'm/s':
            return round(speed / 3.6, 2)
        elif unit_to == 'mph':
            return round(speed * 0.621371, 2)
        elif unit_to == 'knots':
            return round(speed * 0.539957, 2)
        else:
            raise ValueError('invalid literal for int() with base 10: ' + unit_to)

    elif unit_from == 'mph':
        if unit_to == 'm/s':
            return round(speed / 2.23694, 2)
        elif unit_to == 'km/h':
            return round(speed / 0.621371, 2)
        elif unit_to == 'knots':
            return round(speed * 0.868976, 2)
        else:
            raise ValueError('invalid literal for int() with base 10: ' + unit_to)

    elif unit_from == 'knots':
        if unit_to == 'm/s':
            return round(speed / 1.94384, 2)
        elif unit_to == 'km/h':
            return round(speed / 0.539957, 2)
        elif unit_to == 'mph':
            return round(speed / 0.868976, 2)
        else:
            raise ValueError('invalid literal for int() with base 10: ' + unit_to)
    else:
        raise ValueError('invalid literal for int() with base 10: ' + unit_from)


if __name__ == '__main__':
    """
    Run doctests
    
    >>> round(convert_speed(10, 'm/s', 'km/h'), 2)
    36.0

    >>> round(convert_speed(10, 'km/h', 'm/s'), 2)
    2.78

    >>> round(convert_speed(10, 'm/s', 'mph'), 2)
    22.37

    >>> round(convert_speed(10, 'mph', 'm/s'), 2)
    4.47

    >>> round(convert_speed(10, 'km/h', 'mph'), 2)
    6.21

    >>> round(convert_speed(10, 'mph', 'km/h'), 2)
    16.09

    >>> round(convert_speed(10, 'm/s', 'knots'), 2)
    19.44

    >>> round(convert_speed(10, 'knots', 'm/s'), 2)
    5.14

    >>> round(convert_speed(10, 'km/h', 'knots'), 2)
    5.4

    >>> round(convert_speed(10, 'knots', 'km/h'), 2)
    18.52

    >>> round(convert_speed(10, 'mph', 'knots'), 2)
    8.69

    >>> round(convert_speed(10, 'knots', 'mph'), 2)
    11.55

    >>> round(convert_speed(10, 'abc', 'km/h'), 2)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'abc'

    >>> round(convert_speed(abc, 'm/s', 'km/h'), 2)
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'abc'    

    """
    import doctest
    doctest.testmod()

    print("----Codes for speed units----")
    print("m/s: meters per second")
    print("km/h: kilometers per hour")
    print("mph: miles per hour")
    print("knots: nautical miles per hour")  

    from_unit = input('From unit code: ')
    to_unit = input('To unit code: ')
    speed = input('Speed: ')

    speed_converted = round(convert_speed(float(speed), from_unit, to_unit), 2)

    print(f'{speed} {from_unit} is {speed_converted} {to_unit}')