from typing import Tuple, Optional


def find_smallest_and_largest_words(
    input_string: str,
) -> Tuple[Optional[str], Optional[str]]:
    """
    Find the smallest and largest words in a given input string based on their length.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        Tuple[Optional[str], Optional[str]]: A tuple containing the smallest and largest words found.
        If no words are found, both values in the tuple will be None.

    Example:
    >>> find_smallest_and_largest_words("My name is abc")
    ('My', 'name')

    >>> find_smallest_and_largest_words("")
    (None, None)
    """
    words = input_string.split()
    if not words:
        return None, None

    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)

    return smallest_word, largest_word


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    input_string = input("Enter a sentence:\n").strip()
    smallest, largest = find_smallest_and_largest_words(input_string)

    if smallest is not None and largest is not None:
        print(f"The smallest word in the given sentence is '{smallest}'")
        print(f"The largest word in the given sentence is '{largest}'")
    else:
        print("No words found in the input sentence.")
