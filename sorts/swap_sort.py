"""
This is a pure implementation of simple swap sort algorithm in Python.
It counts the number of smaller values and then exchanges the element with the matching digit
Each element may only occur ones.
"""

def swap_sort(collection):
    """Pure implementation of simple swap sort algorithm in Python.

    :param collection: some mutable ordered collection with heterogeneous comparable items inside 
    :return: the same collection ordered by ascending
    Examples:
    >>> swap_sort(1,7,2,5,-3,6,9,10,4)
    [-3, 1, 2, 4, 5, 6, 7, 9, 10]
    """

    index = 0
    while index < len(collection) - 1:
        amount_smaller_elements = sum(x < collection[index] for x in collection)
        if index == amount_smaller_elements:
            index += 1
        else:
            collection[index], collection[amount_smaller_elements] = collection[amount_smaller_elements], collection[index]
    return collection

if __name__== "__main__":
    user_input = input("Enter different numbers seperated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(swap_sort(unsorted))