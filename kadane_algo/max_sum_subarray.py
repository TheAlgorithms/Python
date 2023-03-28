# In below code, we are keeping track of two variables: max_till_now, which stores the maximum sum so far,
# and max_end, which stores the maximum sum of the subarray ending at the current index.
# We iterate through the input array, updating max_end based on whether adding the current element would increase or
# decrease the sum, and updating max_till_now if we find a new maximum sum.

# assuming input array consists of at-least one non-zero element.
def max_sum_subarray(val):
    n = len(val)

    if n == 0:
        return 0

    max_till_now = val[0]
    max_end = val[0]

    for i in range(1, n):
        max_end = max(val[i], max_end + val[i])
        max_till_now = max(max_till_now, max_end)
    return max_till_now


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_subarray(arr))
