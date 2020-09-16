"""
The function below will convert any binary string to the octal equivalent.

>>> bin_to_octal("1111")
'17'

>>> bin_to_octal("101010101010011")
'52523'

>>> bin_to_octal("")
Traceback (most recent call last):
...
ValueError: Empty string was passed to the function
>>> bin_to_octal("a-1")
Traceback (most recent call last):
...
ValueError: Non-binary value was passed to the function
"""


def bin_to_octal(bin_string: str) -> str:
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    oct_string = ""
    while len(bin_string) % 3 != 0:
        bin_string = "0" + bin_string
    bin_string_in_3_list = [
        bin_string[index: index + 3]
        for index, value in enumerate(bin_string)
        if index % 3 == 0
    ]
    for bin_group in bin_string_in_3_list:
        oct_val = 0
        for index, val in enumerate(bin_group):
            oct_val += int(2 ** (2 - index) * int(val))
        oct_string += str(oct_val)
    return oct_string


if __name__ == "__main__":
    from doctest import testmod

    testmod()
