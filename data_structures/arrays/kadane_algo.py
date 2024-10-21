# Function to find the maximum sum of a subarray
def kadanes_algorithm(arr):
    # Initializing variables
    max_current = arr[0]  # This will store the current max sum
    max_global = arr[0]  # This will store the global max sum

    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Update the current max sum by choosing the maximum between
        # the current element alone or the current element plus the previous max
        max_current = max(arr[i], max_current + arr[i])

        # Update the global max sum if the current max is larger
        if max_current > max_global:
            max_global = max_current

    return max_global


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanes_algorithm(arr)
print("Maximum subarray sum is:", result)
