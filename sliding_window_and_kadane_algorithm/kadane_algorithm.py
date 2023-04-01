# The idea of Kadane’s algorithm is to maintain a variable max_ending_here
# hat stores the maximum sum contiguous subarray ending at current index and a
# variable max_so_far stores the maximum sum of contiguous subarray found so far,
# Everytime there is a positive-sum value in max_ending_here
# compare it with max_so_far and update max_so_far if it is greater than max_so_far


def get_max_sum(arr, n):
    sum = 0
    max_sum = -1

    for i in range(n):
        sum = sum + arr[i]
        max_sum = max(max_sum, sum)

        if (sum < 0):
            sum = 0

    return max_sum


# taking the size of the array from the user
n = int(input("Enter the size of the array: "))

arr = []

for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)

ans = get_max_sum(arr, n)

print(f"The maximum sum of the array is {ans}")
