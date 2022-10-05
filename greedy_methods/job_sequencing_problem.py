def printJobScheduling(arr, t):
 
    n = len(arr)
 
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    result = [False] * t
 
    job = ['-1'] * t
 
    for i in range(len(arr)):
 
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
 
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    print(job)
 
 
# Driver's Code
if __name__ == '__main__':
    arr = [[1, 4, 20],  
              [2, 1, 20],
              [3, 1, 40],
              [4, 1, 30]
 

    printJobScheduling(arr, 3)
