"""
Picks the random index as the pivot
"""
import random


def partition(a, left_index, right_index):
    pivot = a[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[left_index], a[i - 1] = a[i - 1], a[left_index]
    return i - 1


def quick_sort_random(a, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        a[pivot], a[left] = (
            a[left],
            a[pivot],
        )  # switches the pivot with the left most bound
        pivot_index = partition(a, left, right)
        quick_sort_random(
            a, left, pivot_index
        )  # recursive quicksort to the left of the pivot point
        quick_sort_random(
            a, pivot_index + 1, right
        )  # recursive quicksort to the right of the pivot point


def main():
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]

    quick_sort_random(arr, 0, len(arr))

    print(arr)


if __name__ == "__main__":
    main()
