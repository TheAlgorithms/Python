def reverse_letters(sentence: str, length: int = 0) -> str:
    """
    Reverse words in a sentence that are longer than a specified length.

    Parameters:
    sentence (str): The input sentence containing words
    length (int): Minimum length of words to be reversed (default is 0)

    Returns:
    str: Sentence with selected words reversed

    Examples:
    >>> reverse_letters("Hey wollef sroirraw", 3)
    'Hey fellow warriors'
    >>> reverse_letters("nohtyP is nohtyP", 2)
    'Python is Python'
    >>> reverse_letters("1 12 123 1234 54321 654321", 0)
    '1 21 321 4321 12345 123456'
    >>> reverse_letters("racecar")
    'racecar'
    """

    # Split the sentence into individual words
    words = sentence.split()

    # Reverse words that have length greater than the specified value
    result = [
        word[::-1] if len(word) > length else word  # reverse using slicing
        for word in words
    ]

    # Join the processed words back into a sentence
    return " ".join(result)


if __name__ == "__main__":
    import doctest

    # Run test cases defined in docstring
    doctest.testmod()

    # Example execution
    print(reverse_letters("Hey wollef sroirraw"))
