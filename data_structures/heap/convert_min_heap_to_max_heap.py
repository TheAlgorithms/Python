# This code is contributed by raj1238

def MaxHeapify(arr, ind, n):
    left = 2 * ind + 1
    right = 2 * ind + 2
    largest = ind
    if left < n and arr[left] > arr[ind]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != ind:
        arr[ind], arr[largest] = arr[largest], arr[ind]
        MaxHeapify(arr, largest, n)
 
def convertMaxHeap(arr, n):
    for i in range(int((n - 2) / 2), -1, -1):
        MaxHeapify(arr, i, n)
 

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()
 
# Driver Code
if __name__ == '__main__':
     
    # array representing Min Heap
    arr = [-4, 24, 48, 3, 2, -9, 11, 1, 5, 7, 6]
    n = len(arr)
 
    print("Min Heap : ")
    printArray(arr, n)
 
    convertMaxHeap(arr, n)
 
    print("Max Heap : ")
    printArray(arr, n)
 
