def findAns(arr, target):
    row = 0
    col = len(arr[row]) - 1
    while (row < len(arr) and col >= 0):
        if (arr[row][col] == target):
            return [row, col]
 
        # Target lies in further row
        if (arr[row][col] < target):
            row += 1
 
        # Target lies in previous column
        else:
            col -= 1
 
    return [-1, -1]
 
 
# Driver Code
if __name__ == '__main__':
    # Binary search in sorted matrix
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ans = findAns(arr, 12)
    print("Element found at index: ", ans)
