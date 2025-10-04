from typing import List
import doctest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that
        answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        This solution runs in O(n) time and O(1) extra space (excluding output),
        without using division.

        >>> Solution().productExceptSelf([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> Solution().productExceptSelf([-1, 1, 0, -3, 3])
        [0, 0, 9, 0, 0]
        >>> Solution().productExceptSelf([0, 0, 0])
        [0, 0, 0]
        >>> Solution().productExceptSelf([0, 1, 2, 3])
        [6, 0, 0, 0]
        >>> Solution().productExceptSelf([0, 0, 1])
        [0, 0, 0]
        >>> Solution().productExceptSelf([-1, -2, -3])
        [6, 3, 2]
        >>> Solution().productExceptSelf([1, 2])
        [2, 1]
        >>> Solution().productExceptSelf([1, 1, 1])
        [1, 1, 1]
        >>> Solution().productExceptSelf([-30, 30, -30, 30])
        [-27000, 27000, -27000, 27000]
        >>> Solution().productExceptSelf([5, 0, 0, 5])
        [0, 0, 0, 0]
        """
        n = len(nums)
        answer = [1] * n

        # Left pass: Compute prefix products
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]

        # Right pass: Compute suffix products and multiply into answer
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


# #optimized Answer
# class Solution(object):
#     def productExceptSelf(self, nums):
#         m = 1
#         z = 0
#         for i in nums:
#             if i !=0:
#                 m*= i
#             else:
#                 z+=1

#         if z==1:
#             return [m if i==0 else 0 for i in nums]
#         if z>1:
#             return [0]*len(nums)
#         return [m//i for i in nums]


if __name__ == "__main__":
    # Run doctests
    doctest.testmod()

    # Additional manual execution example
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [0, 0, 0],
        [0, 1, 2, 3],
        [0, 0, 1],
        [-1, -2, -3],
        [1, 2],
        [1, 1, 1],
        [-30, 30, -30, 30],
        [5, 0, 0, 5],
    ]

    print("\nRunning additional test cases:")
    for case in test_cases:
        result = sol.productExceptSelf(case)
        print(f"Input: {case} -> Output: {result}")
