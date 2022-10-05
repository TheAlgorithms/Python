"""
Insertion sort algorithm
run on terminal to see the result
run ->python insertion_sort2.py
"""


def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp


# array to be sorted
a = [15, 10, 5, 7, 13, 8, 2]
print("Unsorted array:")
print(a)
# method call
insertion_sort(a)
print("Sorted array:")
print(a)
