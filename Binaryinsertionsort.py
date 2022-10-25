# This function will return the index of element 
# just greater than 'key' in Array from 0-N
def binarySearch(Array, N, key):
    L = 0
    R = N
    while(L < R):
        mid = (L + R)//2
        if (Array[mid] <= key):
            L = mid + 1
        else:
            R = mid
    return L
    
def binaryInsertionSort(Array):
    # We assume the 1st element of Array to be already sorted.
    # Now we start iterating from the 2nd element to the last element.
    for i in range (1,len(Array)):
        key = Array[i]
        pos = binarySearch(Array, i, key)
        # 'pos' will now contain the index where 'key' should be inserted.
        j = i
        # Shifting every element from 'pos' to 'i' towards right.
        while(j > pos):
            Array[j] = Array[j-1]
            j = j-1
        # Inserting 'key' in its correct position.
        Array[pos] = key
        print("The array after",i,"iterations =", *Array)
 
Array = [8, 6, 1, 5, 3]
binaryInsertionSort(Array)
