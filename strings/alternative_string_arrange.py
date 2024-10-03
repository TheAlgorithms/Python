def alternative_string_arrange(first_str: str, second_str: str) -> str:
    """
    Return the alternative arrangements of the two strings.

    This function alternates characters from two input strings. If one string
    is longer, the remaining characters will be appended to the end of the
    resulting string.

    :param first_str: The first string to arrange.
    :param second_str: The second string to arrange.
    :return: A new string with alternating characters from the input strings.

    >>> alternative_string_arrange("ABCD", "XY")
    'AXBYCD'
    >>> alternative_string_arrange("XY", "ABCD")
    'XAYBCD'
    >>> alternative_string_arrange("AB", "XYZ")
    'AXBYZ'
    >>> alternative_string_arrange("ABC", "")
    'ABC'
    """
    max_length: int = max(len(first_str), len(second_str))
    result_chars: list = []

    for i in range(max_length):
        if i < len(first_str):
            result_chars.append(first_str[i])
        if i < len(second_str):
            result_chars.append(second_str[i])

    return "".join(result_chars)


if __name__ == "__main__":
    print(alternative_string_arrange("AB", "XYZ"), end=" ")
