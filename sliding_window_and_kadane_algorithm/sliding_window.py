#  It is an algorithm where we can fast compute the things
# which have a fixed window for calculation and we can fetch the
# result in an optimized manner than using the nested loops(naive approach).
# The main goal of this algorithm is to reuse the result of one window to
# compute the result of the next window.


# For Example
# Given an array of integers of size ‘n’, Our aim is to calculate
# the maximum sum of ‘k’ consecutive elements in the array.


def get_max_sum(arr, n, k):
    max_sum = -1
    sum = 0

    for i in range(k):
        sum = sum + arr[i]

    max_sum = sum

    for i in range(k, n):
        sum = sum - arr[i-k]
        sum = sum + arr[i]
        max_sum = max(max_sum, sum)

    return max_sum


# taking the size of the array from the user
n = int(input("Enter the size of the array: "))

k = int(input("Enter the window size: "))

arr = []

for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)

ans = get_max_sum(arr, n, k)

print(f"The maximum sum of the array for window size {k} is {ans}")
