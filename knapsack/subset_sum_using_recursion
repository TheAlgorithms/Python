def is_subset_sum_recursive(arr, n, target):
    # Base cases
    if target == 0:
        return True  # A subset with sum 0 always exists (empty subset)
    if n == 0:
        return False  # No elements left to form the sum

    # If the current element is greater than the target, ignore it
    if arr[n-1] > target:
        return is_subset_sum_recursive(arr, n-1, target)

    # Otherwise, check if sum can be obtained by including or excluding the current element
    return (is_subset_sum_recursive(arr, n-1, target) or
            is_subset_sum_recursive(arr, n-1, target - arr[n-1]))

arr = [3, 34, 4, 12, 5, 2]
target = 9
result = is_subset_sum_recursive(arr, len(arr), target)
print(f"Subset with sum {target} {'exists' if result else 'does not exist'}")

Time Complexity: O(2^N)
Space Complexity: O()
