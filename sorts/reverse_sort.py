def reverse_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True  
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False  

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original List:", my_list)

reverse_sort(my_list)
print("Reverse Sorted List:", my_list)
