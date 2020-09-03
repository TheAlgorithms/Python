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
    first_letter = sentence[0]
    lower_upper_dict = dict()
    lower_upper_dict = {
        lower: upper for lower, upper in zip(ascii_lowercase, ascii_uppercase)
    }
    if first_letter in lower_upper_dict:
        new_sentence = lower_upper_dict[first_letter] + sentence[1:]
    else:
        new_sentence = sentence
    return new_sentence


if __name__ == "__main__":
    from doctest import testmod

    testmod()
