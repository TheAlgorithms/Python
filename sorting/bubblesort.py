"""Online Reference: https://www.geeksforgeeks.org/bubble-sort/"""


def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        # check for every iteration
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [5, 9, 1, 2, 7, 3, 8, 2]
print(bubbleSort(arr))

"""Notes
1. very bad time complexity, two nested loops - O(n^2)
2. good space complexity
3. not recommended"""
