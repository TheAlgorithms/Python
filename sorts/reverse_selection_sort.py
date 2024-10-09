"""
A pure Python implementation of the Reverse Selection Sort algorithm.
This algorithm progressively sorts the array by finding the largest
element in each pass and placing it at the front.
For doctests run following command:
python3 -m doctest -v reverse_selection_sort.py
For manual testing run:
python3 reverse_selection_sort.py
"""


def reverse_selection_sort(collection: list) -> list:
    """
    A pure implementation of reverse selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection sorted in descending order
    Examples:
    >>> reverse_selection_sort([45,23,11,89,54,1,3,36])
    [89, 54, 45, 36, 23, 11, 3, 1]
    >>> reverse_selection_sort([0,-89,32,5,46,8,11])
    [46, 32, 11, 8, 5, 0, -89]
    >>> reverse_selection_sort([34,-2,-1,98,-42])
    [98, 34, -1, -2, -42]
    """
    n = len(collection)
    for i in range(n - 1):
        # Find the maximum element in the unsorted portion
        max_idx = i
        for j in range(i + 1, n):
            if collection[j] > collection[max_idx]:
                max_idx = j

        # Swap the maximum element with the first element of the unsorted portion
        collection[i], collection[max_idx] = collection[max_idx], collection[i]

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(reverse_selection_sort(unsorted))
