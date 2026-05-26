def split(string: str, separator: str = " ") -> list:
    """
    Will split the string up into all the values separated by the separator
    (defaults to spaces)

    >>> split("apple#banana#cherry#orange", separator="#")
    ['apple', 'banana', 'cherry', 'orange']

    >>> split("Hello there")
    ['Hello', 'there']

    >>> split("11/22/63", separator="/")
    ['11', '22', '63']

    >>> split("12:43:39", separator=":")
    ['12', '43', '39']

    >>> split(";abbb;;c;", separator=";")
    ['', 'abbb', '', 'c', '']

    >>> split("apple--banana--cherry", separator="--")
    Traceback (most recent call last):
        ...
    ValueError: separator should be a single character

    >>> split("apple", separator="")
    Traceback (most recent call last):
        ...
    ValueError: separator should not be empty
    """

    if not separator:
        raise ValueError("separator should not be empty")

    if len(separator) != 1:
        raise ValueError("separator should be a single character")

    split_words = []

    last_index = 0
    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index:index])
            last_index = index + 1
        if index + 1 == len(string):
            split_words.append(string[last_index : index + 1])
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()