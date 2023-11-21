"""
This is an optimized Python implementation of the Levenshtein distance algorithm.
Levenshtein distance is a metric for measuring differences between sequences.

For doctests, run the following command:
python -m doctest -v levenshtein_distance.py
or
python3 -m doctest -v levenshtein_distance.py

For manual testing, run:
python levenshtein_distance.py
"""


def levenshtein_distance_optimized(first_word: str, second_word: str) -> int:
    """
    Compute the Levenshtein distance between two words (strings).

    The function is optimized for efficiency by modifying rows in place.

    Parameters:
    first_word (str): The first word to measure the difference.
    second_word (str): The second word to measure the difference.

    Returns:
    int: The Levenshtein distance between the two words.

    Examples:
    >>> levenshtein_distance_optimized("planet", "planetary")
    3
    >>> levenshtein_distance_optimized("", "test")
    4
    >>> levenshtein_distance_optimized("book", "back")
    2
    >>> levenshtein_distance_optimized("book", "book")
    0
    >>> levenshtein_distance_optimized("test", "")
    4
    >>> levenshtein_distance_optimized("", "")
    0
    >>> levenshtein_distance_optimized("orchestration", "container")
    10
    """
    if len(first_word) < len(second_word):
        return levenshtein_distance_optimized(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = list(range(len(second_word) + 1))

    for i, c1 in enumerate(first_word):
        current_row = [i + 1] + [0] * len(second_word)

        for j, c2 in enumerate(second_word):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row[j + 1] = min(insertions, deletions, substitutions)

        previous_row = current_row

    return previous_row[-1]


if __name__ == "__main__":
    first_word = input("Enter the first word:\n").strip()
    second_word = input("Enter the second word:\n").strip()

    result = levenshtein_distance_optimized(first_word, second_word)
    print(f"Levenshtein distance between {first_word} and {second_word} is {result}")
