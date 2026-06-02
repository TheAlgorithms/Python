def split(string: str, separator: str = " ") -> list:
    """
    Will split the string up into all the values separated by the separator (defaults to spaces)
    >>> split("apple#banana#cherry#orange",separator='#')
    ['apple', 'banana', 'cherry', 'orange']
    >>> split("Hello there")
    ['Hello', 'there']
    >>> split("11/22/63",separator = '/')
    ['11', '22', '63']
    >>> split("12:43:39",separator = ":")
    ['12', '43', '39']
    >>> split(";abbb;;c;", separator=';')
    ['', 'abbb', '', 'c', '']
    """
    if len(separator) != 1:
        raise ValueError("separator must be exactly one character long")

    # If the input string is empty, Python's split returns ['']
    if not string:
        return [""]

    split_words = []
    last_index = 0

    # Single-pass scan using string slicing for optimal memory and speed
    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index:index])
            last_index = index + 1

    # Append the remaining trailing substring after the last separator
    split_words.append(string[last_index:])

    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
