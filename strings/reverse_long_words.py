def reverse_long_words(sentence: str) -> str:
    """
    Reverse all words that are longer than 4 characters in a sentence.

    >>> reverse_long_words("Hey wollef sroirraw")
    'Hey fellow warriors'
    >>> reverse_long_words("nohtyP is nohtyP")
    'Python is Python'
    >>> reverse_long_words("1 12 123 1234 54321 654321")
    '1 12 123 1234 12345 123456'
    """
    return " ".join(
        "".join(word[::-1]) if len(word) > 4 else word for word in sentence.split()
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(reverse_long_words("Hey wollef sroirraw"))
