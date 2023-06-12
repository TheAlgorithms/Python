#!/usr/bin/python3
def bubble_sort(collection: list, isascending: bool = True):
    """
    This Is a Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :param isAccending: a boolean that determines if the output should be\
    Sorted in an Ascending or Descending manner (Defaults to Acceding\
    if not specified)
    :return: the same collection ordered by the isAccending param

    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([0, 5, 2, 3, 2], False)
    [5, 3, 2, 2, 0]
    >>> bubble_sort([0, 5, 2, 3, 2], True) == sorted([0, 5, 2, 3, 2])
    True
    >>> bubble_sort([], False) == sorted([])
    False
    >>> bubble_sort([-2, -45, -5]) == sorted([-2, -45, -5])
    True
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    >>> bubble_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> bubble_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> bubble_sort(collection) == sorted(collection)
    True
    """
    if len(collection) == 0:
        return "None"
    else:
        point = 0
        end = len(collection)
        while point < end:
            point2 = end - 1
            while point2 > point:
                if collection[point2] < collection[point]:
                    temp = collection[point2]
                    collection[point2] = collection[point]
                    collection[point] = temp
                point2 -= 1
            point += 1
        if isascending:
            return collection
        else:
            reverse = list(reversed(collection))
            return reverse


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time() - start)%1e9 + 7}")
