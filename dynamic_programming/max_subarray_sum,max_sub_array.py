"""
Given a array of length n, max_subarray_sum() finds
the maximum of sum of contiguous sub-array using divide and conquer method.

Time complexity : O(n log n)

Ref : INTRODUCTION TO ALGORITHMS THIRD EDITION
(section : 4, sub-section : 4.1, page : 70)"""


from sys import maxsize


def max_sum_from_start(array):
    """This function finds the maximum contiguous sum of array from 0 index

    Parameters :
    array (list[int]) : given array

    Returns :
    max_sum (int) : maximum contiguous sum of array from 0 index

    """
    array_sum = 0
    max_sum = float("-inf")
    for num in array:
        array_sum += num
        if array_sum > max_sum:
            max_sum = array_sum
    return max_sum


def max_cross_array_sum(array, left, mid, right):
    """This function finds the maximum contiguous sum of left and right arrays

    Parameters :
    array, left, mid, right (list[int], int, int, int)

    Returns :
    (int) :  maximum of sum of contiguous sum of left and right arrays

    """

    max_sum_of_left = max_sum_from_start(array[left : mid + 1][::-1])
    max_sum_of_right = max_sum_from_start(array[mid + 1 : right + 1])
    return max_sum_of_left + max_sum_of_right


def max_subarray_sum(array, left, right):
    """Maximum contiguous sub-array sum, using divide and conquer method

    Parameters :
    array, left, right (list[int], int, int) :
    given array, current left index and current right index

    Returns :
    int :  maximum of sum of contiguous sub-array

    """

    # base case: array has only one element
    if left == right:
        return array[right]

    # Recursion
    mid = (left + right) // 2
    left_half_sum = max_subarray_sum(array, left, mid)
    right_half_sum = max_subarray_sum(array, mid + 1, right)
    cross_sum = max_cross_array_sum(array, left, mid, right)
    return max(left_half_sum, right_half_sum, cross_sum)


if __name__ == "__main__":
    array = [-2, -5, 6, -2, -3, 1, 5, -6]
    array_length = len(array)
    print(
        "Maximum sum of contiguous subarray:",
        max_subarray_sum(array, 0, array_length - 1),
    )
    # method 2


def find_max_sub_array(a, low, high):
    if low == high:
        return low, high, a[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_sub_array(a, low, mid)
        right_low, right_high, right_sum = find_max_sub_array(a, mid + 1, high)
        cross_left, cross_right, cross_sum = find_max_cross_sum(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_left, cross_right, cross_sum


def find_max_cross_sum(a, low, mid, high):
    left_sum, max_left = -999999999, -1
    right_sum, max_right = -999999999, -1
    summ = 0
    for i in range(mid, low - 1, -1):
        summ += a[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    summ = 0
    for i in range(mid + 1, high + 1):
        summ += a[i]
        if summ > right_sum:
            right_sum = summ
            max_right = i
    return max_left, max_right, (left_sum + right_sum)


def max_sub_array(nums: list[int]) -> int:
    """
    Finds the contiguous subarray which has the largest sum and return its sum.

    >>> max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    An empty (sub)array has sum 0.
    >>> max_sub_array([])
    0

    If all elements are negative, the largest subarray would be the empty array,
    having the sum 0.
    >>> max_sub_array([-1, -2, -3])
    0
    >>> max_sub_array([5, -2, -3])
    5
    >>> max_sub_array([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    """
    best = 0
    current = 0
    for i in nums:
        current += i
        current = max(current, 0)
        best = max(best, current)
    return best


if __name__ == "__main__":
    """
    A random simulation of this algorithm.
    """
    import time
    from random import randint

    from matplotlib import pyplot as plt

    inputs = [10, 100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]
    tim = []
    for i in inputs:
        li = [randint(1, i) for j in range(i)]
        strt = time.time()
        (find_max_sub_array(li, 0, len(li) - 1))
        end = time.time()
        tim.append(end - strt)
    print("No of Inputs       Time Taken")
    for i in range(len(inputs)):
        print(inputs[i], "\t\t", tim[i])
    plt.plot(inputs, tim)
    plt.xlabel("Number of Inputs")
    plt.ylabel("Time taken in seconds ")
    plt.show()

    # 3 method


def max_sub_array_sum(a: list, size: int = 0):
    """
    >>> max_sub_array_sum([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
    -3
    """
    size = size or len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far


if __name__ == "__main__":
    a = [-13, -3, -25, -20, 1, -16, -23, -12, -5, -22, -15, -4, -7]
    print(("Maximum contiguous sum is", max_sub_array_sum(a, len(a))))
# method 4
from collections.abc import Sequence


def max_subarray_sum(nums: Sequence[int]) -> int:
    """Return the maximum possible sum amongst all non - empty subarrays.

    Raises:
      ValueError: when nums is empty.

    >>> max_subarray_sum([1,2,3,4,-2])
    10
    >>> max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
    6
    """
    if not nums:
        raise ValueError("Input sequence should not be empty")

    curr_max = ans = nums[0]
    nums_len = len(nums)

    for i in range(1, nums_len):
        num = nums[i]
        curr_max = max(curr_max + num, num)
        ans = max(curr_max, ans)

    return ans


if __name__ == "__main__":
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subarray_sum(array))
