def reverse_letters(sentence: str, length: int = 0) -> str:
    """Reverse all words longer than a given character length in a sentence.

    If ``length`` is not specified, it defaults to 0.

    >>> reverse_letters("Hey wollef sroirraw", 3)
    'Hey fellow warriors'
    >>> reverse_letters("nohtyP is nohtyP", 2)
    'Python is Python'
    >>> reverse_letters("1 12 123 1234 54321 654321", 0)
    '1 21 321 4321 12345 123456'
    >>> reverse_letters("racecar")
    'racecar'
    """
    return " ".join(
        word[::-1] if len(word) > length else word for word in sentence.split()
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(reverse_letters("Hey wollef sroirraw"))
