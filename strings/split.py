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
    """
    if len(separator) != 1:
        raise ValueError("separator must be a single character")
    return string.split(separator)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

