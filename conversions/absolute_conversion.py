"""
    Convert any interval into a 0 to 100 scale and see a respective number in between
    percentage of the whole.
    Installation:
        - Import this file
        - Call the absolute_conversion function
        - Parameters:
            - interv_start: The start of your internal scale.
            - interv_end: The end of your internal scale.
            - number: The number you want to know the percentage that it
            represents of the scale.
    Examples:
    interv_start:0
    interv_end:100
    number:50
    output: 50.0
    interv_start:6
    interv_end:12
    number:9
    output:50.0

    Link: https://en.wikipedia.org/wiki/Conversion_of_units
"""


def absolute_conversion(interv_start: float, interv_end: float, number: float) -> float:
    """
    >>> absolute_conversion(0, 10, 4)
    40.0
    >>> absolute_conversion(120, 140, 125)
    25.0
    >>> absolute_conversion(0,20,21)
    105.0
    """
    if interv_start > interv_end:
        return print("Invalid arguments, start is higher than the end.")
    elif interv_start == interv_end:
        return print("Invalid arguments, start and end should be different.")
    else:
        native_interval = interv_end - interv_start
        value_percentage = float((100 * (number - interv_start)) / native_interval)
        return value_percentage


if __name__ == "__main__":
    from doctest import testmod

    testmod()
