
from typing import Dict


def char_occurrence(sentence: str) -> Dict[str, int]:
    """
    Given a sentence, return the number of chars occurrence in the sentence.
    >>> SENTENCE = 'hello world! :)'
    >>> char_occurrence(SENTENCE)
    {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1, ':': 1, ')': 1}
    """
    chars_dict = {}
    for ch in sentence:
        chars_dict[ch] = chars_dict[ch] + 1 if ch in chars_dict else 1
    return chars_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(char_occurrence('hello world! :)'))
