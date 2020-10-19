def findPeakRecursion(arr, low , high , n):
    mid = low + (high - low ) / 2
    mid = int(mid)

    if((mid == 0 or arr[mid -1] <= arr[mid -1 ]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakRecursion(arr, low, (mid - 1), n)

    else:
        return findPeakRecursion(arr, mid + 1, high , n)

def findPeakInit(arr, n):
    return findPeakRecursion(arr, 0, n - 1 , n)


arr = [2,3,342,5,1,56]
print("Peak is at index: ", findPeakInit(arr, len(arr)))