def getMissingNumber(arr):
 
    # Compute XOR of all the elements in the list
    xor = 0
    for i in arr:
        xor = xor ^ i
 
    # Compute XOR of all the elements from 1 to `n+1`
    for i in range(1, len(arr) + 2):
        xor = xor ^ i
 
    return xor
 
 
if __name__ == '__main__':
 
    arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print('The missing number is', getMissingNumber(arr))
