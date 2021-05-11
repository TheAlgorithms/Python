hex_table = {hex(i)[2:]: i for i in range(16)}


def hex_to_binary(hex_string: str) -> int:
    """
    Convert hexadecimal string to binary string
    >>> hex_to_binary("3f")
    '0b00111111'
    >>> hex_to_binary("-D2")
    '-0b11010010'
    >>> hex_to_binary("Ac")
    '0b10101100'
    >>> hex_to_binary("45")
    '0b01000101'
    >>> hex_to_binary("")
    """

    hex_string = hex_string.strip().lower()
    if not hex_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = hex_string[0] == "-"
    if is_negative:
        hex_string = hex_string[1:]
    if not all(char in hex_table for char in hex_string):
        raise ValueError("Non hexadecimal value was passed to the function")

    binary_list: list[int] = []
    index_vals: list[int] = [8, 4, 2, 1]
    current_index = 0
    for char in hex_string:
        value = hex_table[char]
        for index_val in index_vals:
            if value // index_val == 1:
                binary_list.insert(current_index, 1)
                value -= index_val
            else:
                binary_list.insert(current_index, 0)
            current_index += 1

    if is_negative:
        return "-0b" + "".join(str(v) for v in binary_list)
    return "0b" + "".join(str(v) for v in binary_list)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
