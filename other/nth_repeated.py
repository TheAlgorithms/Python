# Created by sarathkaul on 04/02/20
# Script to print second most repeated character in sequence
from collections import Counter


def nth_repeated(sequence: list, nth_repeated: int) -> str:
    """
    >>> sequence = ['Algorithms','Algorithm','Python','Python','The','Python','The']
    >>> nth_repeated = 2
    >>> print(nth_repeated(sequence, nth_repeated))
    The
    """
    if nth_repeated < 1:
        return ""
    sequence_dict = Counter(sequence)
    sequence_value = sorted(sequence_dict.values(), reverse=True)
    largest = sequence_value[nth_repeated - 1]
    for (key, value) in sequence_dict.items():
        if value == largest:
            return key
    return ""


if __name__ == "__main__":
    input_sequence = [
        "Python",
        "2.7",
        "is",
        "deprecated",
        "Python",
        "3+",
        "is",
        "active",
        "Love",
        "Python",
    ]
    nth_repeated = 2
    print(nth_repeated(input_sequence, nth_repeated))
