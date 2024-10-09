#Description: Sort an array in a wave-like form. In this form, arr[0] >= arr[1] <= arr[2] >= arr[3]...

#Input: [10, 5, 6, 3, 2, 20, 100, 80]
#Output: [20, 10, 6, 3, 5, 2, 80, 100]
#Key Idea: Sort the array and swap every adjacent pair of elements.

def wave_array(arr):
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
