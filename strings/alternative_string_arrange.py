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

    # Base Condition
    if len(first_str)==0:
        return second_str
    if len(second_str)==0:
        return first_str

    first_str_length: int = len(first_str)
    second_str_length: int = len(second_str)
    abs_length: int = (
        first_str_length if first_str_length < second_str_length else second_str_length   # Take length of Minimum length
    )
    output_list: list = []
    for char_count in range(abs_length):
        if char_count < first_str_length:
            output_list.append(first_str[char_count])
        else:
        	break
        if char_count < second_str_length:
            output_list.append(second_str[char_count])
        else:
        	break
    return "".join(output_list) + second_str[char_count+1:] + first_str[char_count+1:]


if __name__ == "__main__":
    print(alternative_string_arrange("AB", "XYZ"), end=" ")
