from typing import Any


def library_sort(collection: list[Any]) -> list[Any]:
    """
    Sort a collection using the Library Sort algorithm.

    This function takes an unsorted collection (list) of elements and sorts it in ascending order using
    the Library Sort algorithm. The algorithm is based on counting the occurrences of elements in the
    collection to create a sorted array.

    Args:
        collection (list): The unsorted collection to be sorted.

    Returns:
        list: A new list containing the sorted elements in ascending order.

    Example:
        >>> library_sort([5, 2, 9, 1, 5, 6])
        [1, 2, 5, 5, 6, 9]

    Note:
        - The function works with collections of integers.
        - The original collection remains unchanged.
        - If the collection is empty, it is returned as is.

    """
    # Check if the collection is empty, and if so, return it as-is
    if not collection:
        return collection

    # Find the minimum and maximum values in the collection
    min_val, max_val = min(collection), max(collection)

    # Create a library (counting) array with a size based on the range of values
    library = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element in the collection
    for num in collection:
        library[num - min_val] += 1

    # Reconstruct the sorted array based on the counts in the library
    sorted_arr = []
    for i, count in enumerate(library):
        sorted_arr.extend([i + min_val] * count)

    return sorted_arr


if __name__ == "__main__":
    import doctest
    import time

    # Run doctests to check code examples in docstrings
    doctest.testmod()

    # Prompt the user for input
    user_input = input("Enter items separated by a comma:").strip()

    # Parse user input into a list of integers
    unsorted = [int(item) for item in user_input.split(",")]

    # Measure the execution time of the library_sort function
    start = time.process_time()
    sorted_items = library_sort(unsorted)

    # Print the sorted items and processing time in nanoseconds
    print(*sorted_items, sep=",")
    print(f"Processing time: {(time.process_time() - start) * 1e9 + 7} nanoseconds")
