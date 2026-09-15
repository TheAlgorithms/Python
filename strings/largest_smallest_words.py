def find_smallest_and_largest_words(input_string: str) -> tuple:
    """
    Find the smallest and largest words in a given input string based on their length.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        tuple: A tuple containing the smallest and largest words found.
        If no words are found, both values in the tuple will be None.

    Examples:
    >>> find_smallest_and_largest_words("My name is abc")
    ('My', 'name')

    >>> find_smallest_and_largest_words("Hello guys")
    ('guys', 'Hello')

    >>> find_smallest_and_largest_words("OnlyOneWord")
    ('OnlyOneWord', 'OnlyOneWord')
    """
    words = input_string.split()
    if not words:
        return None, None

    # Handle punctuation and special characters
    words = [word.strip(".,!?()[]{}") for word in words]

    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)

    return smallest_word, largest_word


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    input_string = input("Enter a sentence:\n").strip()
    smallest, largest = find_smallest_and_largest_words(input_string)

    if smallest and largest:
        print(f"The smallest word in the given sentence is '{smallest}'")
        print(f"The largest word in the given sentence is '{largest}'")
    else:
        print("No words found in the input sentence.")
