import random


def random_sort(arr):
    while any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        random.shuffle(arr)


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original List:", my_list)

random_sort(my_list)
print("Randomly Sorted List:", my_list)
