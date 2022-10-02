def binarySearch(Array, lower_bound, upper_bound, value):
    """
    This function carries out Binary search on a 1d array
    """
    r = int((lower_bound+upper_bound)/2)
    
    if (Array[r] == value):
        
        return True
    if((lower_bound == r) or (upper_bound == r)):
        return False
    if (Array[r] < value):
        return binarySearch(Array, r + 1, upper_bound, value)
    if (Array[r] > value):
        return binarySearch(Array, lower_bound, r, value)


def matBinSearch(value, matrix):
    """
    This function loops over a 2d matrix and calls binarySearch on the selected 1d array
    """
    index = 0
    while matrix[index][0] < value:
        if binarySearch(matrix[index], 0, len(matrix[index]) - 1, value):
            return True
        else : index = index+1
    return False
    
Array = [[1, 4, 7, 11, 15],
[2, 5, 8, 12, 19],
[3, 6, 9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]]

value = 11

if matBinSearch(value, Array):
    print("True")