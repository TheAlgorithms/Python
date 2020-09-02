def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word
    >>> capitalize("hello world")
        "Hello world"
    >>> capitalize("123 hello world)
        "123 hello world"
    >>> capitalize(" hello world")
       " hello world"
    """

    first_char = sentence[0]
    new_sentence = str.upper(first_char) + sentence[1:]
    return new_sentence


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
