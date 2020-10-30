"""
Isolate the Decimal part of a Number
https://stackoverflow.com/questions/3886402/how-to-get-numbers-after-decimal-point
"""


def decimal_isolate(number, digitAmount):

    """
    Isolates the decimal part of a number.
    If digitAmount > 0 round to that decimal place, else print the entire decimal.
    >>> decimal_isolate(1.53, 0)
    0.53
    >>> decimal_isolate(35.345, 1)
    0.3
    >>> decimal_isolate(35.345, 2)
    0.34
    >>> decimal_isolate(35.345, 3)
    0.345
    >>> decimal_isolate(-14.789, 3)
    -0.789
    >>> decimal_isolate(0, 2)
    0
    >>> decimal_isolate(-14.123, 1)
    -0.1
    >>> decimal_isolate(-14.123, 2)
    -0.12
    >>> decimal_isolate(-14.123, 3)
    -0.123
    """
    if digitAmount > 0:
        return round(number - int(number), digitAmount)
    return number - int(number)


if __name__ == "__main__":
    print(decimal_isolate(1.53, 0))
    print(decimal_isolate(35.345, 1))
    print(decimal_isolate(35.345, 2))
    print(decimal_isolate(35.345, 3))
    print(decimal_isolate(-14.789, 3))
    print(decimal_isolate(0, 2))
    print(decimal_isolate(-14.123, 1))
    print(decimal_isolate(-14.123, 2))
    print(decimal_isolate(-14.123, 3))
