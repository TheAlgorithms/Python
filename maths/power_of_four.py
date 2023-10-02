# Problem Statement: 
# Link : https://leetcode.com/problems/power-of-four/description/


# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.
# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

# Example 3:
# Input: n = 1
# Output: true



# Intuition:
# The intuition behind this code is based on the property of powers of four. In base-4 (quaternary) representation, any power of four will have only one '1' digit followed by zero or more '0' digits. 
# For example, 4^0 = 1, 4^1 = 4, 4^2 = 16, and so on. In base-4, these numbers are represented as 1, 10, 100, and so on.
# So, if you take the base-10 logarithm of a power of four and divide it by the base-10 logarithm of 4, you should get an integer. If you get an integer, it means the number is a power of four.

# Time Complexity:
# The time complexity of this code is O(1) because it involves basic mathematical operations like logarithms and integer checks, which have constant time complexity.

#  Space Complexity:
#  The space complexity of this code is also O(1) because it uses a constant amount of memory to store the result of the logarithmic calculation and the integer check. The space used is not dependent on the input value n, so it remains constant regardless of the size of n.


import math

def isPowerOfFour(n):
    if n <= 0:
        return False

    logarithm4 = math.log10(n) / math.log10(4)

    return logarithm4.is_integer()

# Example usage:
print(isPowerOfFour(16))  # Output: True
print(isPowerOfFour(5))   # Output: False
