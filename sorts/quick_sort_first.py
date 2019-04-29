"""
Picks the leftmost index as the pivot
"""
from __future__ import print_function

def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index]
    return i - 1

def quick_sort_first(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quick_sort_first(A, left, pivot_index)
        quick_sort_first(A, pivot_index + 1, right)

if __name__ == "__main__":
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    arr = [int(item) for item in user_input.split(',')]

    quick_sort_first(arr, 0, len(arr))

    print(arr)