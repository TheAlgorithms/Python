def quick_sort(arr, l, r):  # arr[l:r]
    if r - l <= 1:  # base case
        return ()

   # partition w.r.t pivot - arr[l]
   # dividing array into three parts one pivot
   # one yellow part which contains elements less than pivot
   # and last green part which contains elements greater than pivot
    yellow = l + 1
    for green in range(l+1, r):
        if arr[green] <= arr[l]:
            arr[yellow], arr[green] = arr[green], arr[yellow]
            yellow += 1
    
    # move pivot into place
    arr[l], arr[yellow - 1] = arr[yellow - 1], arr[l]

    quick_sort(arr, l, yellow-1)  # calling in recursion
    quick_sort(arr, yellow, r)

    return arr

print("Enter elements you want to sort: ")
array = list(map(int, input().split()))
sorted_array = quick_sort(array, 0, len(array))
print("Sorted array is: ", *sorted_array)
