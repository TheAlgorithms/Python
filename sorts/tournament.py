import math

def tournament_sort(arr):
"""
Tournament Sort implementation.
Sorts the input list in ascending order.

```
Args:
    arr (list): List of comparable elements

Returns:
    list: Sorted list
"""
n = len(arr)
if n == 0:
    return []

# Next power of 2 (for complete tree)
size = 1 << (n - 1).bit_length()

# Build tree with "infinity" placeholders
tree = [math.inf] * (2 * size)

# Insert elements into leaves
for i in range(n):
    tree[size + i] = arr[i]

# Build tournament winners upward
for i in range(size - 1, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

sorted_list = []

for _ in range(n):
    # The root has the current minimum
    winner = tree[1]
    sorted_list.append(winner)

    # Find the leaf index of this winner
    idx = tree.index(winner, size)

    # Replace it with infinity
    tree[idx] = math.inf

    # Update tree upwards
    idx //= 2
    while idx > 0:
        tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])
        idx //= 2

return sorted_list
```

# Example usage

if **name** == "**main**":
nums = [5, 3, 8, 4, 2, 7, 1, 6]
print("Original:", nums)
print("Sorted  :", tournament_sort(nums))
