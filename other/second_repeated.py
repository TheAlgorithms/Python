# Created by sarathkaul on 04/02/20
# Script to print second most repeated character in sequence
from collections import Counter


def second_repeated(sequence: list) -> str:
    """
    >>> sequence = ['Algorithms','Algorithm','Python','Python','The','Python','The']
    >>> print(second_repeated(sequence))
    The
    """
    sequence_dict = Counter(sequence)
    sequence_value = sorted(sequence_dict.values(), reverse=True)
    second_largest = sequence_value[1]
    for (key, value) in sequence_dict.items():
        if value == second_largest:
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
    print(second_repeated(input_sequence))
