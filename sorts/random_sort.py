import random
from typing import List

def is_sorted(lista: List[int]) -> bool:
    """
    Given a list of integer, return True if all are ordered

    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 2, 1])
    False
    """
    values = [lista[i] <= lista[i+1] for i in range(len(lista) - 1)]
    return all(values)

def random_sort(lista: List[int]) -> List[int]:
    """
    efficiency? where are we going we don't need that

    >>> random_sort([1, 2, 3])
    [1, 2, 3]
    >>> random_sort([3, 2, 1])
    [1, 2, 3]
    """
    while not is_sorted(lista):
        random.shuffle(lista)
        # print(lista)

    return lista


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(random_sort(unsorted))
