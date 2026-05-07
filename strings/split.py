def split(string: str, separator: str = " ") -> list[str]:
    """
    Split string into values separated by separator.

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
    """

    if len(separator) != 1:
        raise ValueError("separator must be exactly one character")

    parts: list[str] = []
    start = 0

    for index, char in enumerate(string):
        if char == separator:
            parts.append(string[start:index])
            start = index + 1

    parts.append(string[start:])
    return parts


if __name__ == "__main__":
    from doctest import testmod

    testmod()
