"""
Given an array arr[] of size n-1 with integers in the range of [1, n], the task is to find the missing number from the first N integers.

Note: There are no duplicates in the list.

Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , n = 8
Output: 5
Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}, n = 5
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
"""


def find_missing_number(arr, n):
    hash = [0] * (n + 1)

    for num in arr:
        hash[num] += 1
    for i in range(1, (n + 1)):
        if hash[i] == 0:
            return i
    return -1


print(find_missing_number([1, 2, 3, 4, 6, 7, 8], 8))
