def shortest_word(sentence: str) -> str:
    """
    Find the longest word in a sentence.
    If there are multiple words that are the same length, return the last one.

    www.geeksforgeeks.org/python-program-to-find-the-longest-word-in-a-sentence/

    >>> shortest_word("I love Python")
    'Python'
    >>> shortest_word("Find the shortest word in a sentence.")
    'sentence.'
    >>> shortest_word("Black Stack")
    'Stack'
    >>> shortest_word("funny bunny rabbit")
    'rabbit'
    """

    # Split the sentence into a list of words
    # Sort by length and take the first element
    word_list = sentence.split()
    word_list.sort(key=len)
    return word_list[-1]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
