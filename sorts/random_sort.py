import random

def random_sort(arr):
    sorted_arr = sorted(arr) 
    while arr != sorted_arr:
        random.shuffle(arr)

my_list = [4, 2, 7, 1, 9, 5]
print("Original List:", my_list)

random_sort(my_list)
print("Sorted List:", my_list)