"""
This is a pure Python implementation of the binary insertion sort algorithm

For doctest run the following command:
python -m doctest -v binary_insertion_sort.py
or
python3 -m doctest -v binary_insertion_sort.py

For manual testing run:
python binary_insertion_sort.py
"""
def binary_insertion_sort(collection: list) -> list:
    """
    Pure implementation of the binary insertion sort algorithm in Python.

    :param collection: A mutable ordered collection with homogeneous
    comparable items inside.
    :return: The same collection ordered in ascending order.
    """
    n = len(collection)
    for i in range(1, n):
        val = collection[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if val < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            collection[j] = collection[j - 1]
        collection[low] = val
    return collection

def test_binary_insertion_sort():
    # Basic test cases
    assert binary_insertion_sort([0, 4, 1234, 4, 1]) == [0, 1, 4, 4, 1234]
    assert binary_insertion_sort([]) == []
    assert binary_insertion_sort([-1, -2, -3]) == [-3, -2, -1]

    # Test sorting of characters
    lst = ["d", "a", "b", "e", "c"]
    assert binary_insertion_sort(lst) == ["a", "b", "c", "d", "e"]

    # Test sorting with random integer values
    import random
    collection = random.sample(range(-50, 50), 100)
    assert binary_insertion_sort(collection) == sorted(collection)

    # Test sorting with random alphanumeric characters
    import string
    collection = random.choices(string.ascii_letters + string.digits, k=100)
    assert binary_insertion_sort(collection) == sorted(collection)

    # Test with a reversed list
    reversed_list = list(range(10, 0, -1))
    assert binary_insertion_sort(reversed_list) == list(range(1, 11))

    # Test with a list of the same elements
    same_elements_list = [5] * 10
    assert binary_insertion_sort(same_elements_list) == [5] * 10

    # Test sorting with negative numbers
    negative_numbers = [-5, -1, -10, -3, -2]
    assert binary_insertion_sort(negative_numbers) == [-10, -5, -3, -2, -1]

    # Test with a large list of random integers
    large_collection = random.sample(range(-1000, 1000), 1000)
    assert binary_insertion_sort(large_collection) == sorted(large_collection)

    # Test with a single-element list
    single_element_list = [42]
    assert binary_insertion_sort(single_element_list) == [42]

    print("All test cases passed.")

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = binary_insertion_sort(unsorted)
    print("Sorted list:", sorted_list)
