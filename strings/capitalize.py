from string import ascii_lowercase, ascii_uppercase


def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word
    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("123 hello world")
    '123 hello world'
    >>> capitalize(" hello world")
    ' hello world'
    """
    lower_upper_dict = {
        lower: upper for lower, upper in zip(ascii_lowercase, ascii_uppercase)
    }
    return lower_upper_dict.get(sentence[0], sentence[0]) + sentence[1:]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
