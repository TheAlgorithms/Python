"""
This is a pure Python implementation of the Cyclic Sort algorithm.

For doctests run following command:
python -m doctest -v cyclic_sort.py
or
python3 -m doctest -v cyclic_sort.py
For manual testing run:
python cyclic_sort.py
or
python3 cyclic_sort.py
"""


def cyclic_sort(nums: list[int]) -> list[int]:
    """
    Sorts the input list of n integers from 1 to n in-place
    using the Cyclic Sort algorithm.

    :param nums: List of n integers from 1 to n to be sorted.
    :return: The same list sorted in ascending order.

    Time complexity: O(n), where n is the number of integers in the list.

    Examples:
    >>> cyclic_sort([])
    []
    >>> cyclic_sort([3, 5, 2, 1, 4])
    [1, 2, 3, 4, 5]
    """

    # Perform cyclic sort
    index = 0
    while index < len(nums):
        # Calculate the correct index for the current element
        correct_index = nums[index] - 1
        # If the current element is not at its correct position,
        # swap it with the element at its correct index
        if index != correct_index:
            nums[index], nums[correct_index] = nums[correct_index], nums[index]
        else:
            # If the current element is already in its correct position,
            # move to the next element
            index += 1

    return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*cyclic_sort(unsorted), sep=",")
