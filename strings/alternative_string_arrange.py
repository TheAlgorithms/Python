def alternative_string_arrange(first_str: str, second_str: str) -> str:
    """
    Return the alternative arrangements of the two strings.
    :param first_str:
    :param second_str:
    :return: String
    >>> alternative_string_arrange("ABCD", "XY")
    'AXBYCD'
    >>> alternative_string_arrange("XY", "ABCD")
    'XAYBCD'
    >>> alternative_string_arrange("AB", "XYZ")
    'AXBYZ'
    >>> alternative_string_arrange("ABC", "")
    'ABC'
    """
    # Calculate the lengths of the input strings.
    first_str_length: int = len(first_str)
    second_str_length: int = len(second_str)

    # Determine the max length between the two input strings.
    abs_length: int = (
        first_str_length if first_str_length > second_str_length else second_str_length
    )

    # Initialize an empty list to store the characters of the combined string.
    output_list: list = []

    # Iterate through the characters up to the max length.
    for char_count in range(abs_length):
        # Append a character from the first string if it exists at this position.
        if char_count < first_str_length:
            output_list.append(first_str[char_count])

        # Append a character from the second string if it exists at this position.
        if char_count < second_str_length:
            output_list.append(second_str[char_count])

    # Join the characters in the list to form the final combined string.
    return "".join(output_list)


if __name__ == "__main__":
    print(alternative_string_arrange("AB", "XYZ"), end=" ")
