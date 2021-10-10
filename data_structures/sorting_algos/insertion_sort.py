def insertion_sort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
    
arr = [5, 1, 7, 2, 9, 4, 3]
print(insertion_sort(arr))