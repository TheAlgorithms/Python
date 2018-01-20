from __future__ import print_function
import math
def jump_search(arr, x):
    n = len(arr)
    step = math.floor(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += math.floor(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1



arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
index = jump_search(arr, x)
print("\nNumber " + str(x) +" is at index " + str(index));