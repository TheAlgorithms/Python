"""
Author: Sanjay Muthu <https://github.com/XenoBytesX>

This is an implementation of the Dynamic Programming solution to the Range Sum Query.

The problem statement is:
    Given an array and q queries,
    each query stating you to find the sum of elements from l to r (inclusive)

Example:
    arr = [1, 4, 6, 2, 61, 12]
    queries = 3
    l_1 = 2, r_1 = 5
    l_2 = 1, r_2 = 5
    l_3 = 3, r_3 = 4

    as input will return

    [81, 85, 63]

    as output

0-indexing:
NOTE: 0-indexing means the indexing of the array starts from 0
Example: a = [1, 2, 3, 4, 5, 6]
         Here, the 0th index of a is 1,
               the 1st index of a is 2,
               and so forth

Time Complexity: O(N + Q)
* O(N) pre-calculation time to calculate the prefix sum array
* and O(1) time per each query = O(1 * Q) = O(Q) time

Space Complexity: O(N)
* O(N) to store the prefix sum

Algorithm:
So, first we calculate the prefix sum (dp) of the array.
The prefix sum of the index i is the sum of all elements indexed
from 0 to i (inclusive).
The prefix sum of the index i is the prefix sum of index (i - 1) + the current element.
So, the state of the dp is dp[i] = dp[i - 1] + a[i].

After we calculate the prefix sum,
for each query [l, r]
the answer is dp[r] - dp[l - 1] (we need to be careful because l might be 0).
For example take this array:
    [4, 2, 1, 6, 3]
The prefix sum calculated for this array would be:
    [4, 4 + 2, 4 + 2 + 1, 4 + 2 + 1 + 6, 4 + 2 + 1 + 6 + 3]
    ==> [4, 6, 7, 13, 16]
If the query was l = 3, r = 4,
the answer would be 6 + 3 = 9 but this would require O(r - l + 1) time ≈ O(N) time

If we use prefix sums we can find it in O(1) by using the formula
prefix[r] - prefix[l - 1].
This formula works because prefix[r] is the sum of elements from [0, r]
and prefix[l - 1] is the sum of elements from [0, l - 1],
so if we do prefix[r] - prefix[l - 1] it will be
[0, r] - [0, l - 1] = [0, l - 1] + [l, r] - [0, l - 1] = [l, r]
"""


def prefix_sum(array: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    >>> prefix_sum([1, 4, 6, 2, 61, 12], [(2, 5), (1, 5), (3, 4)])
    [81, 85, 63]
    >>> prefix_sum([4, 2, 1, 6, 3], [(3, 4), (1, 3), (0, 2)])
    [9, 9, 7]
    """
    # The prefix sum array
    dp = [0] * len(array)
    dp[0] = array[0]
    for i in range(1, len(array)):
        dp[i] = dp[i - 1] + array[i]

    # See Algorithm section (Line 44)
    result = []
    for query in queries:
        left, right = query
        res = dp[right]
        if left > 0:
            res -= dp[left - 1]
        result.append(res)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
