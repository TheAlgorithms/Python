def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = gnome_sort(unsorted_list)
print(sorted_list)

# worst case time complexity of O(n^2)
# works by repeatedly swapping adjacent elements if they are in the wrong order
