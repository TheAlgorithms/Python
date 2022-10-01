#Median search is used when we want to search kth smallest element in an array, it uses the concept of quick sort to find the kth smallest element in an array.

import sys
 
def kthSmallest(arr, l, r, K):
 
    # If k is smaller than number of
    # elements in array
    if (K > 0 and K <= r - l + 1):
 
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, l, r)
 
        # If position is same as k
        if (pos - l == K - 1):
            return arr[pos]
        if (pos - l > K - 1):  # If position is more,
                              # recur for left subarray
            return kthSmallest(arr, l, pos - 1, K)
 
        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r,
                           K - pos + l - 1)
 
    # If k is more than number of
    # elements in array
    return sys.maxsize
 
# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
 
 
def partition(arr, l, r):
 
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
 
 
# Driver Code
if __name__ == "__main__":
 
    arr = [12, 3, 5, 7, 4, 19, 26]
    N = len(arr)
    K = 3
    print("K'th smallest element is",
          kthSmallest(arr, 0, N - 1, K))
