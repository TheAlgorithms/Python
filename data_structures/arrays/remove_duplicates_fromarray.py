# Program to remove duplicates from a sorted array

# Input: sorted array
arr = [1, 1, 2, 2, 3, 4, 4, 5]

print("Original array:", arr)

# Create an empty list to store unique elements
unique_arr = []

# Traverse the array
for num in arr:
    # Add the number only if it's not already in unique_arr
    if len(unique_arr) == 0 or num != unique_arr[-1]:
        unique_arr.append(num)

print("Array after removing duplicates:", unique_arr)
