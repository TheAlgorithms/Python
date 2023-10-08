def reverse_letters(sentence: str, length: int = 0) -> str:
    """
    Reverse all words that are longer than the given length of characters in a sentence. If unspecified, length is taken as 0

    >>> reverse_letters("Hey wollef sroirraw", 3)
    'Hey fellow warriors'
    >>> reverse_letters("nohtyP is nohtyP", 2)
    'Python is Python'
    >>> reverse_letters("1 12 123 1234 54321 654321", 0)
    '1 21 321 432112345 123456'
    >>> reverse_letters("To be or not to be")
    'oT eb ro ton ot eb'
    """
    return " ".join(
        "".join(word[::-1]) if len(word) > length else word for word in sentence.split()
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(reverse_letters("Hey wollef sroirraw"))
