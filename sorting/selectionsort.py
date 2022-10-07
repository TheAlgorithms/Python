"""Online Reference: https://www.geeksforgeeks.org/selection-sort/ """


def selectSort(arr):
    for i in range(0, len(arr) - 1):
        # i is the index we will operate on, this iteration, thus we shall initialise from i
        min = arr[i]  # the smallest item in list
        index = i  # updating acc to index of the smallest item in list
        for j in range(i + 1, len(arr)):  # i+1 as we don't want to compare with self
            # if the element is less than the curren min,
            if arr[j] < min:
                min = arr[j]  # update min if current is lower than previous min
                index = j  # index of the current min
        # swaping the element in index i with the minimum in index j
        arr[i], arr[index] = arr[index], arr[i]
    return arr


arr = [8, 6, 5, 0, 4, 3, 2]
print(selectSort(arr))
