"""
This is a pure Python implementation of counting sort algorithm.
For doctests run the following command:
python -m doctest -v counting_sort.py
or
python3 -m doctest -v counting_sort.py

For the manual testing run:
python counting_sort.py
"""


def counting_sort(collection):
    """A pure implementation of counting sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # If the collection is empty, it returns empty
    if collection == []: 
        return []

    # Get some information about the collection
    coll_len = len(collection)
    coll_max = max(collection)
    coll_min = min(collection)

    # Creating the counting array.
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # Count the times how much a number appears in the collection.
    for number in collection:
        counting_arr[number - coll_min] += 1

    # Sum each position with it's predecessors. Now, counting_arr[i] tells 
    # us how many elements less than equals to i are in the collection.
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # Create an output collection
    ordered = [0] * coll_len

    # Place the elements in the output, keeping the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered


def counting_sort_string(string):
    """
    >>> counting_sort_string("thisisastring")
    'aghiiinrssstt'
    """
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


if __name__ == "__main__":
    # Testing of string sort
    assert "aghiiinrssstt" == counting_sort_string("thisisastring")

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(counting_sort(unsorted))
