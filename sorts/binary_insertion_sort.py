"""
Illustrate how to implement binary insertion sort algorithm.

Author: REHAN SHAIKH

Binary Insertion Sort: Binary insertion sort is a sorting algorithm which uses insertion sort with binary search rather than linear search to find the position where the element should be inserted . The advantage is that we reduce the number of comparisons for inserting one element from O(N) to O(log N).

Time Complexity: O(n2) is the worst case running time because of the series of swaps required for each insertion

Auxiliary Space: O(logn)

"""

def binary_search(arr, N, key) -> int:
    low = 0
    high = N
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid
    return low
    
def insertion_sort(arr) -> None : 
    for i in range (1,len(arr)):
        key = arr[i]
        pos = binary_search(arr, i, key)
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[pos] = key
 
user_input = input("Enter numbers separated by a comma:").strip()
arr = [int(item) for item in user_input.split(",")]

insertion_sort(arr)

for i in range(len(arr)):
    print(arr[i])
