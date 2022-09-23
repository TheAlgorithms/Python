# Created by sarathkaul on 17/11/19
# Modified by Arkadip Bhattacharya(@darkmatter18) on 20/04/2020
from collections import defaultdict
from typing import DefaultDict


def word_occurrence(sentence: str) -> dict:
    """
    >>> from collections import Counter
    >>> SENTENCE = "a b A b c b d b d e f e g e h e i e j e 0"
    >>> occurence_dict = word_occurrence(SENTENCE)
    >>> all(occurence_dict[word] == count for word, count
    ...     in Counter(SENTENCE.split()).items())
    True
    >>> dict(word_occurrence("Two  spaces"))
    {'Two': 1, 'spaces': 1}
    """
    occurrence: DefaultDict[str, int] = defaultdict(int)
    # Creating a dictionary containing count of each word
    for word in sentence.split():
        occurrence[word] += 1
    return occurrence


if __name__ == "__main__":
    for word, count in word_occurrence("INPUT STRING").items():
        print(f"{word}: {count}")
