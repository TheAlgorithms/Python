def binary_search(arr, element, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
element = 2

#printing the array
print("The given array is", arr)

#printing element to be found
print("Element to be found is ", element)

#calling method
index = binary_search(arr, element, 0, len(arr)-1)

#printing result
if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")
