# Created by sarathkaul on 17/11/19
# Modified by Arkadip Bhattacharya(@darkmatter18) on 20/04/2020
from collections import defaultdict
from typing import DefaultDict, Dict


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


# approach with .get method
test_data: Dict[str, Dict[str, int]] = {
    "": dict(),

    "hello world hello":
        {
            "hello": 2,
            "world": 1
        }
    ,

    "a b c a b c d d c":
        {
            "a": 2,
            "b": 2,
            "c": 3,
            "d": 2
        }
}


def word_occurence_with_get(sentence: str) -> Dict[str, int]:
    """Function takes sentence as string and returns occurences of words
    in sentence as dictionary
    Args:
        sentence (str)
    Returns:
        dictionary with key as word from sentence and value as number of word occurences

    Example:
        sentence = "cat bat cat bat chair"

        will return:

        {
        "cat" : 2,
        "bat": 2,
        "chair": 1
        }

    """

    occurences: Dict[str, int] = dict()
    for w in sentence.split():
        occurences[w] = occurences.get(w, 0) + 1
    return occurences


if __name__ == "__main__":
    for word, count in word_occurrence("INPUT STRING").items():
        print(f"{word}: {count}")
    # tests for .get approach
    for sentence, expected_result in test_data.items():
        actual: Dict[str, int] = word_occurence_with_get(sentence)
        expected: Dict[str, int] = expected_result
        assert actual == expected_result


