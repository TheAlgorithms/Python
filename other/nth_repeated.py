# Created by sarathkaul on 04/02/20
# Script to print second most repeated character in sequence
from collections import Counter


def count_repeated(sequence: list, nth_repeated: int) -> str:
    """
    >>> sequence = ['Algorithms','Algorithm','Python','Python','The','Python','The']
    >>> nth_repeated = 2
    >>> print(count_repeated(sequence, nth_repeated))
    The
    """
    return "" if nth_repeated < 1 else Counter(sequence).most_common()[nth_repeated - 1][0]

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
    print(count_repeated(input_sequence, nth_repeated))
