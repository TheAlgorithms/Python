def word_count(txt):
    """
    >>> word_count("Hello")
    1
    >>> word_count("Hello, World")
    2
    """
    x = txt.split()
    return len(x)


def char_count(txt):
    """
    >>> char_count("Hello")
    5
    >>> char_count("Hello, World")
    12
    """
    return len(txt)
