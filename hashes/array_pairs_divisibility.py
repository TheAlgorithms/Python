"""
check-if-array-pairs-are-divisible-by-k

Problem statement:
Given an array of integers arr of even length n and an integer k.

Divide the array into n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs.
See that there is no way to divide arr into 3 pairs each with sum divisible by 10.

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
"""

# Time complexity: O(n)
# Space complexity: O(k)

# Approach:
# 1. Create a list of size k with all elements as 0.
# 2. For each element in the array, increment the element at index i%k.
# 3. If the element at index 0 is odd, return False.
# 4. Check if the number of elements at index i and k-i are equal.
# 5. If not, return False.
# 6. If all the conditions are satisfied, return True.


class Solution:
    def can_arrange(self, arr: list[int], input_num: int) -> bool:
        """
        Function to check if array pairs are divisible by k
        :param arr: List of integers
        :param k: Integer
        :return: Boolean

        Example:
        >>> obj = Solution()
        >>> obj.can_arrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5)
        True
        >>> obj.can_arrange([1, 2, 3, 4, 5, 6], 7)
        True
        """
        sol_arr = [0 for i in range(input_num)]
        for i in arr:
            sol_arr[i % input_num] += 1
        if sol_arr[0] % 2 != 0:
            return False
        i, j = 1, input_num - 1
        while j > i:
            if sol_arr[i] == sol_arr[j]:
                j -= 1
                i += 1
            else:
                return False
        return True


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    input_num = 5
    s = Solution()
    print(s.can_arrange(arr, input_num))  # Output: True
