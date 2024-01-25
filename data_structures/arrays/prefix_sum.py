"""
Author  : Ratheshan Sathiyamoorthy
Date    : October 24, 2023

Implement the class of prefix sum with useful functions based on it.

"""


class PrefixSum:
    def __init__(self, array: list[int]) -> None:
        # Store the original array, no need to precompute the prefix sum.
        self.array = array

    def get_sum(self, start: int, end: int) -> int:
        """
        The function returns the sum of the array from the start to the end indexes.
        Runtime: O(1)
        Space: O(1)

        >>> PrefixSum([1, 2, 3]).get_sum(0, 2)
        6
        >>> PrefixSum([1, 2, 3]).get_sum(1, 2)
        5
        >>> PrefixSum([1, 2, 3]).get_sum(2, 2)
        3
        >>> PrefixSum([1, 2, 3]).get_sum(2, 3)
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        """
        if start == 0:
            # Calculate sum from the original array using built-in sum function.
            return sum(self.array[: end + 1])

        # Calculate sum from the original array using built-in sum function.
        return sum(self.array[start : end + 1])

    def contains_sum(self, target_sum: int) -> bool:
        """
        The function returns True if the array contains the target_sum, False otherwise.
        Runtime: O(n)
        Space: O(n)

        >>> PrefixSum([1, 2, 3]).contains_sum(6)
        True
        >>> PrefixSum([1, 2, 3]).contains_sum(5)
        True
        >>> PrefixSum([1, 2, 3]).contains_sum(3)
        True
        >>> PrefixSum([1, 2, 3]).contains_sum(4)
        False
        >>> PrefixSum([1, 2, 3]).contains_sum(7)
        False
        >>> PrefixSum([1, -2, 3]).contains_sum(2)
        True
        """
        prefix_sum = 0
        sums = {0}

        for num in self.array:
            prefix_sum += num
            if prefix_sum - target_sum in sums:
                # Found a subarray with the desired sum.
                return True
            sums.add(prefix_sum)

        # The desired sum was not found in any subarray.
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
