"""
This is a pure Python implementation of the Cyclic Sort algorithm.

For doctests run following command:
python -m doctest -v cyclic_sort.py
or
python3 -m doctest -v cyclic_sort.py
For manual testing run:
python cyclic_sort.py
"""


def cyclic_sort(nums: list) -> list:
    """
    Sorts the input list in-place using the Cyclic Sort algorithm.

    :param nums: List of integers to be sorted.
    :return: The same list sorted in ascending order.

    Time complexity: O(n), where n is the number of elements in the list.

    Examples:
    >>> cyclic_sort([3, 5, 2, 1, 4])
    [1, 2, 3, 4, 5]
    >>> cyclic_sort([])
    []
    """

    # Perform cyclic sort
    i = 0
    while i < len(nums):
        # Calculate the correct index for the current element
        correct_index = nums[i] - 1
        # If the current element is not at its correct position,
        # swap it with the element at its correct index
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            # If the current element is already in its correct position,
            # move to the next element
            i += 1

    return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*cyclic_sort(unsorted), sep=",")
