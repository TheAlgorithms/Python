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

def quick_sort_first(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quick_sort_first(A, left, pivot_index)
        quick_sort_first(A, pivot_index + 1, right)

if __name__ == "__main__":
    file_name = input("Please enter a filename:\n")

    file = open(file_name, 'r')

    arr = []
    for i in file:
        arr.append(int(i.strip()))

    #NOTE: we start the left at 1 because the first number
    #denotes the number of elements in the the text file
    quick_sort_first(arr, 1, len(arr))

    print(arr[1:])