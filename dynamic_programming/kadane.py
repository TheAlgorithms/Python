"""
Kadane Problem Statement: Given an array of n numbers,
the task is to calculate the maximum subarray sum.

A subarray is a part of a section of an array. A subarray can be empty.
Example :
[2, 3, 4] is a subarray of [1, 2, 3, 4, 5].
[] is a subarray of [1, 2, 3, 4, 5].

A subarray sum is the sum of the elements in the subarray.
Example :
The sum of the subarray [2, 3, 4] is 9.
The sum of the subarray [] is 0.
"""


def maximum_subarray_sum(array: list[int]) -> int:
    """
    Finds the maximum subarray sum of an array and return it.

    >>> maximum_subarray_sum([1, 2, 3, 4, 5])
    15
    >>> maximum_subarray_sum([1, 2, -10, 4, 5])
    9
    >>> maximum_subarray_sum([-3, -5, 18, -2, 3])
    19
    >>> maximum_subarray_sum([-3, -5, -18, -2, -3])
    0
    """

    # maximum_subarray_sum stores the maximum subarray sum
    # max_ending_here stores the maximum subarray sum ending at a certain element
    maximum_subarray_sum = 0
    max_ending_here = 0

    for value in array:
        max_ending_here += value

        maximum_subarray_sum = max(maximum_subarray_sum, max_ending_here)
        max_ending_here = max(max_ending_here, 0)

    return maximum_subarray_sum


if __name__ == "__main__":
    array = [-3, -5, 18, -2, 3]

    print(f"Array : {array}")
    print(f"Maximum subarray sum = {maximum_subarray_sum(array)}")

    import doctest

    doctest.testmod()
