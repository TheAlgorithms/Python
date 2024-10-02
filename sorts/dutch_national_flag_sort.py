"""
A pure implementation of Dutch national flag (DNF) sort algorithm in Python.
Originally designed by Edsger Dijkstra, it optimally sorts a sequence of three unique values
(e.g., 0, 1, 2) with [0 <= a[i] <= 2] in O(n) complexity in a single pass.

The task is to randomly arrange balls of white, red, and blue so that balls of the same color
are grouped together. DNF sorts a sequence of 0, 1, and 2's in linear time without consuming
extra space. The algorithm works only on sequences with three unique elements.

1) Time complexity is O(n).
2) Space complexity is O(1).

For more info: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

For doctests run:
python3 -m doctest -v dutch_national_flag_sort.py

For manual testing run:
python dnf_sort.py
"""

# Python program to sort a sequence containing only 0, 1, and 2 in a single pass.
RED = 0  # The first color (red).
WHITE = 1  # The second color (white).
BLUE = 2  # The third color (blue).
ALLOWED_VALUES = (RED, WHITE, BLUE)


def dutch_national_flag_sort(sequence: list) -> list:
    """
    A Python implementation of the Dutch National Flag sorting algorithm.
    :param sequence: A list of integers containing only 0, 1, and 2
    :return: Sorted sequence with the values 0, 1, 2 in ascending order

    >>> dutch_national_flag_sort([])
    []
    >>> dutch_national_flag_sort([0])
    [0]
    >>> dutch_national_flag_sort([2, 1, 0, 0, 1, 2])
    [0, 0, 1, 1, 2, 2]
    >>> dutch_national_flag_sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    >>> dutch_national_flag_sort("abacab")
    Traceback (most recent call last):
      ...
    ValueError: The elements inside the sequence must contain only (0, 1, 2) values
    >>> dutch_national_flag_sort([3, 2, 3, 1, 3, 0, 3])
    Traceback (most recent call last):
      ...
    ValueError: The elements inside the sequence must contain only (0, 1, 2) values
    >>> dutch_national_flag_sort([-1, 2, -1, 1, -1, 0, -1])
    Traceback (most recent call last):
      ...
    ValueError: The elements inside the sequence must contain only (0, 1, 2) values
    >>> dutch_national_flag_sort([1.1, 2, 1.1, 1, 1.1, 0, 1.1])
    Traceback (most recent call last):
      ...
    ValueError: The elements inside the sequence must contain only (0, 1, 2) values
    """
    if not sequence:
        return []
    if len(sequence) == 1:
        return sequence

    low, mid, high = 0, 0, len(sequence) - 1

    while mid <= high:
        if sequence[mid] == RED:
            sequence[low], sequence[mid] = sequence[mid], sequence[low]
            low += 1
            mid += 1
        elif sequence[mid] == WHITE:
            mid += 1
        elif sequence[mid] == BLUE:
            sequence[mid], sequence[high] = sequence[high], sequence[mid]
            high -= 1
        else:
            raise ValueError(
                f"The elements inside the sequence must contain only {ALLOWED_VALUES} values"
            )

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # User input for manual testing
    user_input = input("Enter numbers separated by commas (0, 1, 2 only):\n").strip()
    try:
        unsorted = [int(item.strip()) for item in user_input.split(",")]
        if all(x in ALLOWED_VALUES for x in unsorted):
            print(f"Sorted sequence: {dutch_national_flag_sort(unsorted)}")
        else:
            print("Error: Input must only contain the values 0, 1, and 2.")
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
