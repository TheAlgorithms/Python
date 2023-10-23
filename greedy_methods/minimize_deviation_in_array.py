'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.
'''

from heapq import heapify, heappop, heappush

class Solution:
    def minimumDeviation(self, nums):
        """
        Function to find the minimum deviation of an array after performing operations.

        Args:
            nums (List[int]): A list of positive integers.

        Returns:
            min_deviation (int): The minimum deviation of the array after operations.

        Examples:
            >>> solution = Solution()
            >>> solution.minimumDeviation([1, 2, 3, 4])
            1
            >>> solution.minimumDeviation([5, 10, 20, 30, 30])
            25
            >>> solution.minimumDeviation([8, 8, 8, 8, 8])
            0
        """
        hq = [-n * 2 if n % 2 else -n for n in nums]
        heapify(hq)
        min_ = -min(hq, key=lambda x: -x)
        min_deviation = -hq[0] - min_

        while hq and hq[0] % 2 == 0:
            n = heappop(hq) // 2
            heappush(hq, n) 
            min_ = min(min_, -n)
            min_deviation = min(min_deviation, -hq[0] - min_)
        
        return min_deviation

if __name__ == "__main__":
    import doctest

    doctest.testmod()