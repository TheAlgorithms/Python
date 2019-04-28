#!/usr/bin/env python3

def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index]
    return i - 1

def quick_sort_median3(A, left, right):
    if left < right:
        get_median(A, left, right - 1)
        pivot_index = partition(A, left, right)
        quick_sort_median3(A, left, pivot_index)
        quick_sort_median3(A, pivot_index + 1, right)

#Helper function to get the median value and then swap it into the left most position
#at a given recursive call
def get_median(A, left, right):
    if right - left <= 1:
        if A[left] > A[right]:
            A[left], A[right] = A[right], A[left]
    else:
        first = A[left]
        middle = A[left + ((right - left) // 2)]
        last = A[right]

        if middle > first and middle < last or middle < first and middle > last:
            A[left + ((right - left) // 2)], A[left] = first, middle
        elif last > first and last < middle or last < first and last > middle:
            A[right], A[left] = first, last

if __name__ == "__main__":
    file_name = input("Please enter a filename:\n")

    file = open(file_name, 'r')

    arr = []
    for i in file:
        arr.append(int(i.strip()))

    #NOTE: we start the left at 1 because the first number
    #denotes the number of elements in the the text file
    quick_sort_median3(arr, 1, len(arr))

    print(arr[1:])