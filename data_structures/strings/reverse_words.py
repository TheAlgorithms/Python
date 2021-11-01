def reverse_words(input_str: str) -> str:
    """
    Reverses words in a given string
    >>> reverse_words("I love Python")
    'Python love I'
    >>> reverse_words("I     Love          Python")
    'Python Love I'
    """
    return " ".join(input_str.split()[::-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
