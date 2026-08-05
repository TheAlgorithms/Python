def split(string: str, separator: str = " ") -> list[str]:
    """
    Splits a string by the specified separator and returns a list of substrings.

    :param string: The string to be split.
    :param separator: The separator to split the string by (defaults to space).
    :return: List of substrings split by the separator.

    Examples:

    >>> split("apple#banana#cherry#orange", separator='#')
    ['apple', 'banana', 'cherry', 'orange']

    >>> split("Hello there")
    ['Hello', 'there']

    >>> split("11/22/63", separator='/')
    ['11', '22', '63']

    >>> split("12:43:39", separator=":")
    ['12', '43', '39']

    >>> split(";abbb;;c;", separator=';')
    ['', 'abbb', '', 'c', '']
    """
    split_words = []
    last_index = 0

    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index:index])
            last_index = index + 1

    # Append the remaining part of the string after the last separator
    split_words.append(string[last_index:])
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
