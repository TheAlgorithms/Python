# Program to find the Next Greater Element (NGE) for each element in the array

arr = [4, 5, 2, 25, 7, 8]
n = len(arr)

print("Original array:", arr)

# List to store results, default is -1 for elements with no greater element
nge = [-1] * n

# Outer loop for each element
for i in range(n):
    # Inner loop to find the next greater element
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            nge[i] = arr[j]
            break  # Stop once the next greater is found

# Print result
for i in range(n):
    print(f"Next Greater Element for {arr[i]} is {nge[i]}")
