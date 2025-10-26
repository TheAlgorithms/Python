"""
reverse_words_in_sentence.py
----------------------------
Reverses the order of words in a given sentence.

Example:
    >>> reverse_words_in_sentence("hello world")
    'world hello'

    >>> reverse_words_in_sentence("Python is fun")
    'fun is Python'
"""

def reverse_words_in_sentence(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.
    Words are separated by spaces.
    """
    words = sentence.strip().split()
    return " ".join(reversed(words))


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(reverse_words_in_sentence(sentence))
