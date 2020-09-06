def count_chars(text: str) -> int:
    """
    This function iterates over characters of a string and keeps a counter called result
    to count the number of total charecters within a string
    >>> count_chars('pythonpy')
    8
    >>> count_chars('name')
    4
    >>> count_chars('gitHub')
    6
    """
    result = 0
    for char in text:
        result += 1
    return result


if __name__ == "__main__":

    from doctest import testmod

    testmod()
