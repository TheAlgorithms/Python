import random
from typing import List

def bogo_sort(collection: List[int]) -> List[int]:
    """Pure implementation of the bogosort algorithm in Python.
    Bogosort generates random permutations until it guesses the correct one.
    
    More info on: https://en.wikipedia.org/wiki/Bogosort
    Args:
        collection (List[int]): A mutable ordered collection with comparable items.
    Returns:
        List[int]: The same collection ordered by ascending.
    Examples:
    >>> bogo_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bogo_sort([])
    []
    >>> bogo_sort([-2, -5, -45])
    [-45, -5, -2]
    Raises:
        ValueError: If the input is not a list of integers.
    Note:
        This is not an efficient sorting algorithm and is mainly used for educational purposes.
    For doctests, run the following command:
    python -m doctest -v bogo_sort.py
    or
    python3 -m doctest -v bogo_sort.py
    
    For manual testing, run:
    python bogo_sort.py
    """

    def is_sorted(collection: List[int]) -> bool:
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not is_sorted(collection):
        random.shuffle(collection)
    return collection

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(bogo_sort(unsorted))
