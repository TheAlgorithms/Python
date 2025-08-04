def capitalize(sentence: str) -> str:
    """
    Capitalizes the first character of the string if it is a lowercase letter.

    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("123 hello world")
    '123 hello world'
    >>> capitalize(" hello world")
    ' hello world'
    >>> capitalize("a")
    'A'
    >>> capitalize("")
    ''
    """
    if not sentence:
        return ""

    # Get the first character of the sentence
    first_char = sentence[0]
    # Check if the first character is a lowercase letter
    if 'a' <= first_char <= 'z':
        # Convert the lowercase letter to uppercase using ASCII value
        first_char = chr(ord(first_char) - 32)
    # Return the capitalized first character concatenated with the rest of the sentence
    return first_char + sentence[1:]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
