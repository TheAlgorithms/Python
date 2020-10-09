"""
This is a pure Python implementation of the quick sort algorithm,
in distributed manner with Ray.

NOTE: it extends from quick_sort.py in this same directory

For doctests run following command:
python -m doctest -v quick_sort_distributed.py
or
python3 -m doctest -v quick_sort_distributed.py

For manual testing run:
python quick_sort_distributed.py
"""
import ray
from numpy import random
import time

ray.init()


def quick_sort(collection):
    """Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> quick_sort([])
    []

    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    if length <= 1:
        return collection
    else:
        # Use the last element as the first pivot
        pivot = collection.pop()
        # Put elements greater than pivot in greater list
        # Put elements lesser than pivot in lesser list
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


@ray.remote
def quick_sort_distributed(collection):
    length = len(collection)
    if length <= 200000:
        return quick_sort(collection)
    else:
        pivot = collection.pop()
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)

        lesser = quick_sort_distributed.remote(lesser)
        greater = quick_sort_distributed.remote(greater)
        return ray.get(lesser) + [pivot] + ray.get(greater)


if __name__ == "__main__":
    unsorted = random.randint(1000000, size=(4000000)).tolist()
    s = time.time()
    quick_sort(unsorted)
    print("Sequential execution: " + str(time.time() - s))
    s = time.time()
    ray.get(quick_sort_distributed.remote(unsorted))
    print("Distributed execution: " + str(time.time() - s))
