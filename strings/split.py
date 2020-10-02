def split(string, separator):
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
    """

    split_words = []
    split_words = string.split(separator)
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    print(split("12:13:63",":"))
