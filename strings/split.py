def split(string: str, separator: str = " ") -> list:
    """
    Will split the string up into all the values separated by the separator
    (defaults to spaces)

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

    >>> split("a--b--c", separator="--")
    Traceback (most recent call last):
        ...
    ValueError: separator must be a single character

    >>> split("hello world", separator="")
    Traceback (most recent call last):
        ...
    ValueError: separator must be a single character
    """

    if len(separator) != 1:
        raise ValueError("separator must be a single character")

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
