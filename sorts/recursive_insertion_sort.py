"""
A recursive implementation of the insertion sort algorithm
"""

def rec_insertion_sort(collection, n):
    """
    Given a collection of numbers and its length, sorts the collections
    in ascending order

    :param collection: A mutable collection of heterogenous, comparable elements
    :param n: The length of collections

    >>> col = [1, 2, 1]
    >>> rec_insertion_sort(col, len(col))
    >>> print(col)
    [1, 1, 2]

    >>> col = [2, 1, 0, -1, -2]
    >>> rec_insertion_sort(col, len(col))
    >>> print(col)
    [-2, -1, 0, 1, 2]

    >>> col = [1]
    >>> rec_insertion_sort(col, len(col))
    >>> print(col)
    [1]
    """


    #Checks if the entire collection has been sorted
    if len(collection) <= 1 or n <= 1:
        return


    data_swap(collection, n-1)
    rec_insertion_sort(collection, n-1)

def data_swap(collection, index):

    #Checks order between adjacent elements
    if index >= len(collection) or collection[index - 1] <= collection[index]:
        return

    #Swaps adjacent elements since they are not in ascending order
    collection[index - 1], collection[index] = (
    collection[index], collection[index - 1]
    )

    data_swap(collection, index + 1)

if __name__ == "__main__":
    numbers = input("Enter integers seperated by spaces: ")
    numbers = [int(num) for num in numbers.split()]
    rec_insertion_sort(numbers, len(numbers))
    print(numbers)
