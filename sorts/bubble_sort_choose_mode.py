def bubble_sort(collection, mode):

    
    """Pure implementation of bubble sort algorithm in Python

    code and comments below not relating to mode(ascending vs descending) are from the original file bubble_sort.py,
    added choosing ascending or descending order and sorting the numbers accordingly based on user input
    
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> bubble_sort([]) == sorted([])
    True
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
    length = len(collection)
    if mode == 'a':    
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if collection[j] > collection[j + 1]:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped:
                break  # Stop iteration if the collection is sorted.
        return collection
    elif mode == 'd':
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if collection[j] < collection[j + 1]:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped:
                break  # Stop iteration if the collection is sorted.
        return collection

if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    mode = input("Enter 'a' for ascending sort, 'd' for descending sort")
    print(*bubble_sort(unsorted, mode), sep=",")
    print(f"Processing time: {time.process_time() - start}")
