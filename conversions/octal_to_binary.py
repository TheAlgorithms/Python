"""
Convert a octal value to its binary equivalent
>>> octal_to_binary("17")
'1111'
>>> octal_to_binary("52523")
'101010101010011'
>>> octal_to_binary("532.51")
'101011010.101001'
"""


from operator import index


def octal_to_binary(octal_string: str) -> str:
    if not all(char in "01234567." for char in octal_string):
        raise ValueError("Non-octal value was passed to the function")
    if not octal_string:
        raise ValueError("Empty string was passed to the function")
    binary_string = ""
    dict_of_octal_to_binary = {
        "0": "000",
        "1": "001",
        "2": "010",
        "3": "011",
        "4": "100",
        "5": "101",
        "6": "110",
        "7": "111",
    }
    indexl = 0
    for i in octal_string:
        if i == ".":
            binary_string += "."
            continue
        if binary_string == "":
            for char in dict_of_octal_to_binary[i]:
                if char != "0" or indexl >= 1:
                    binary_string += char
                    indexl += 1
        else:
            binary_string += dict_of_octal_to_binary[i]
    return binary_string


if __name__ == "__main__":
    from doctest import testmod

    testmod()
