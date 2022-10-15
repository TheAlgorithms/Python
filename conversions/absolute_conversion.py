"""
    Convert any interval into a 0 to 100 scale and see a respective number in between
    percentage of the whole.
    Instalation:
        - Import this file
        - Call the absolute_conversion function
        - Parameters:
            - interv_start: The start of your internal scale.
            - interv_end: The end of your internal scale.
            - number_between: The number you want to know the percentage that it
            represents of the scale.
    Exemples:
    interv_start:0
    interv_end:100
    number_between:50
    output: 50.0
    interv_start:6
    interv_end:12
    number_between:9
    output:50.0
"""


def absolute_conversion(interv_start: float, interv_end: float, number_between: float):
    if interv_start > interv_end:
        return print("Invalid arguments, start is higher than the end.")
    elif interv_start == interv_end:
        return print("Invalid arguments, start and end shoud be different.")
    else:
        native_interval = interv_end - interv_start
        return (100 * (number_between - interv_start)) / native_interval


if __name__ == "__main__":
    from doctest import testmod

    testmod()
