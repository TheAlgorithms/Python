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
    """

    split_words = []
    start = 0

    while True:
        index = string.find(separator, start)
        if index == -1:
            split_words.append(string[start:])
            break
        split_words.append(string[start:index])
        start = index + len(separator)

    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
