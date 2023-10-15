from typing import List


def find_duplicate_xor(nums: List[int]) -> int:
    """
    Find the duplicate number in a list using XOR.

    This function finds the duplicate number in a list by XOR-ing all the elements.

    >>> find_duplicate_xor([1, 2, 3, 2, 4, 5, 6, 4])
    3
    >>> find_duplicate_xor([1, 2, 3, 2, 4, 5, 6, 4, 7, 7])
    3
    >>> find_duplicate_xor([1, 1, 1, 2, 2, 3, 3])
    3
    >>> find_duplicate_xor([1, 2, 3, 4, 5, 6, 7, 8, 9])
    0
    """

    result = 0
    for num in nums:
        result ^= num

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
