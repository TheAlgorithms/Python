# Binary Search in python
def binarySearch(arr, l, r ,value):
    while l <= r:
        mid = (l + r) / 2

        if value == arr[mid]:
            return mid

        elif arr[mid] > value:
            r = mid - 1

        else:
            l = mid + 1

    return -1

arr = [5,10,12,14,17,18,19]
length = len(arr)
value = 17
index = binarySearch(arr, 0, length - 1, value)
if index == -1:
    print("Not in array")
else:
    print("Found at position %d" % index)
