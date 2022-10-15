def diagonalDifference(arr):
        sumOfDiagonalFromLeft = 0
        sumOfDiagonalFromRight = 0
        pointIndexFromLeft = 0
        pointIndexFromLast = len(arr)-1
        for i in range(len(arr)):
            sumOfDiagonalFromLeft += arr[i][pointIndexFromLeft]
            # print(arr[i][pointIndexFromLeft])
            pointIndexFromLeft += 1
        
        for i in range(len(arr)):
            sumOfDiagonalFromRight += arr[i][pointIndexFromLast]
            # print(arr[i][pointIndexFromLast])
            if pointIndexFromLast < 0:
                break
            else:
                pointIndexFromLast -= 1
    
        diagonalDifference = abs(sumOfDiagonalFromLeft - sumOfDiagonalFromRight)
        return diagonalDifference
    
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))