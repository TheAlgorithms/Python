"""
This is a pure Python implementation of an adaptive merge sort algorithm.
This implementation detects and merges presorted runs for better performance on partially sorted data.

For doctests run following command:
python -m doctest -v adaptive_merge_sort.py
or
python3 -m doctest -v adaptive_merge_sort.py
For manual testing run:
python adaptive_merge_sort.py
"""


def adaptive_merge_sort(collection: list) -> list:
    """
    Sorts a list using an adaptive merge sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Time Complexity: O(n log n) in the average case,
                     O(n) for nearly sorted input.

    Examples:
    >>> adaptive_merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> adaptive_merge_sort([])
    []
    >>> adaptive_merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def find_run(collection: list, start: int) -> int:
        """
        Detects and returns the length of a naturally occurring run starting from 'start'.

        :param collection: The list to detect runs in.
        :param start: The starting index for finding the run.
        :return: Length of the detected run.
        """
        run_length = 1
        while (
            start + run_length < len(collection)
            and collection[start + run_length - 1] <= collection[start + run_length]
        ):
            run_length += 1
        return run_length

    def merge(left: list, right: list) -> list:
        """
        Merge two sorted lists into a single sorted list.

        :param left: Left collection
        :param right: Right collection
        :return: Merged result
        """
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return collection

    runs = []
    i = 0
    # Step 1: Identify naturally occurring runs and store them in 'runs'
    while i < len(collection):
        run_length = find_run(collection, i)
        runs.append(collection[i : i + run_length])
        i += run_length

    # Step 2: Iteratively merge runs until one sorted collection remains
    while len(runs) > 1:
        merged_runs = []
        for j in range(0, len(runs), 2):
            if j + 1 < len(runs):
                merged_runs.append(merge(runs[j], runs[j + 1]))
            else:
                merged_runs.append(runs[j])
        runs = merged_runs

    return runs[0]  # The single, fully sorted list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_list = adaptive_merge_sort(unsorted)
        print(*sorted_list, sep=",")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
