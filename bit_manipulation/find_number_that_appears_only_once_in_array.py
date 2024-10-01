'''
This problem comes from LeetCode 136: Single Number

Problem Statement: You are given an list of number where each number appears twice in the list but there is a single number that appears once only. Find that single number.

Intuition:
- Hence we know that a ^ a = 0 (^ is XOR binary operator)
- We can XOR all numbers, then we will get the only single number
- Example: let's take nums = [1, 2, 4, 1, 4, 3, 2]
    - We can see all numbers appears twice except 3
    - If we take XOR of all element, we will get 3, let me demonstrate -
        - 1 ^ 2 ^ 4 ^ 1 ^ 4 ^ 3 ^ 2
    - Since we know a ^ a = 0, we can cancel them out -
        - 1 ^ 1 ^ 2 ^ 2 ^ 4 ^ 4 ^ 3
        - 0 ^ 0 ^ 0 ^ 3
    - We also know a ^ 0 = a, then we will get our answer as 3

Complexities:
- Time: O(n)
- Space: O(1)
'''

def find_single_number(nums):
    '''
    LeetCode 136: Single Number
    https://leetcode.com/problems/single-number/description/

    >>> find_single_number([1, 4, 1, 7, 9, 2, 9, 7, 2])
    4
    >>> find_single_number([1, 2, 4, 1, 4, 3, 2])
    3
    >>> find_single_number([4, 1, 2, 1, 2])
    4
    '''
    single_num = 0
    
    for i in nums:
        single_num = single_num ^ i;
    
    return single_num

if __name__ == "__main__":
    import doctest
    doctest.testmod()
