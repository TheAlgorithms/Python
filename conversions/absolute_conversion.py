"""
    Convert any interval into a 0 to 100 scale and see a respective number in between
    percentage of the whole.
    Instalation:
        - Import this file
        - Call the absolute_conversion function
        - Parameters:
            - interval_start: The start of your internal scale.
            - interval_end: The end of your internal scale.
            - number: The number you want to know the percentage that it
            represents of the scale.
    Exemples:
    interval_start:0
    interval_end:100
    number:50
    output: 50.0
    interval_start:6
    interval_end:12
    number:9
    output:50.0

    Link: https://en.wikipedia.org/wiki/Conversion_of_units
"""


def absolute_conversion(interval_start: float, interval_end: float, number: float) -> float:
    """
    >>> absolute_conversion(0, 10, 4)
    40.0
    >>> absolute_conversion(120, 140, 125)
    25.0
    >>> absolute_conversion(0,20,21)
    105.0
    """
    if interval_start > interval_end:
        return print("Invalid arguments, start is higher than the end.")
    elif interval_start == interval_end:
        return print("Invalid arguments, start and end shoud be different.")
    else:
        native_interval = interval_end - interval_start
        return (100 * (number - interval_start)) / native_interval


if __name__ == "__main__":
    from doctest import testmod

    testmod()
