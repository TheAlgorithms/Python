def reverse_letters(sentence: str, length: int) -> str:
    """
    Reverse all words that are longer than the given length of characters in a sentence.

    >>> reverse_letters("Hey wollef sroirraw", 3)
    'Hey fellow warriors'
    >>> reverse_letters("nohtyP is nohtyP", 2)
    'Python is Python'
    >>> reverse_letters("1 12 123 1234 54321 654321", 5)
    '1 12 123 1234 54321 123456'
    """
    return " ".join(
        "".join(word[::-1]) if len(word) > length else word for word in sentence.split()
    )



if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    print(reverse_letters("Hey wollef sroirraw"))
