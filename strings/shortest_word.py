def shortest_word(sentence: str) -> str:
    """
    Find the shortest word in a sentence.
    If there are multiple words that are the same length, return the first one.

    www.geeksforgeeks.org/python-program-to-find-the-smallest-word-in-a-sentence/

    >>> shortest_word("I love Python")
    'I'
    >>> shortest_word("Find the shortest word in a sentence.")
    'a'
    >>> shortest_word("Black Stack")
    'Black'
    >>> shortest_word("funny bunny rabbit")
    'funny'
    """

    # Split the sentence into a list of words
    # Sort by length and take the first element
    word_list = sentence.split()
    for word in word_list:
        if len(word) == min(len(word) for word in word_list):
            return word


if __name__ == "__main__":
    from doctest import testmod

    testmod()
