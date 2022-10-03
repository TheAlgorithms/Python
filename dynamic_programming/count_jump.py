"""
Given an array of numbers where each element represents the max number of jumps that can be made forward from that element.
For each array element, count the number of ways jumps can be made from that element to reach the end of the array.
If an element is 0, then a move cannot be made through that element. The element that cannot reach the end should have a count "-1".
"""
from typing import List


def count_ways_to_jump(arr: List[int]) -> List[int]:
    """
    >>> count_ways_to_jump([3,2,0,1])
    [2, 1, -1, 0]
    >>> count_ways_to_jump([1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9])
    [52, 52, 28, 16, 8, -1, -1, 4, 2, 1, 0]
    """
    n = len(arr)
    # count_jump[i] store number of ways
    # arr[i] can reach to the end
    count_jump = [0 for i in range(n)]

    # Last element does not require to jump. Count ways to jump for remaining elements
    for i in range(n - 2, -1, -1):
        if arr[i] >= n - i - 1:
            count_jump[i] += 1

        j = i + 1
        while j < n - 1 and j <= arr[i] + i:
            if count_jump[j] != -1:
                count_jump[i] += count_jump[j]
            j += 1

        # if arr[i] cannot reach to the end
        if count_jump[i] == 0:
            count_jump[i] = -1

    return count_jump


if __name__ == '__main__':
    import doctest

    doctest.testmod()
