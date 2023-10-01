# Define the max_subarray function which calculates the maximum subarray sum
def max_subarray(arr):
    max_sum = arr[
        0
    ]  # Initialize max_sum and current_sum with the first element of the array
    current_sum = arr[0]

    for i in range(
        1, len(arr)
    ):  # Iterate through the array starting from the second element
        current_sum = max(arr[i], current_sum + arr[i])  # Calculate the current sum
        max_sum = max(max_sum, current_sum)  # Update the maximum sum if needed

    return max_sum  # Return the maximum subarray sum


# Take custom input from the user
user_input = input(
    "Enter a list of numbers separated by spaces: "
)  # Prompt the user for input
arr = list(map(int, user_input.split()))  # Convert the input into a list of integers

# Call the max_subarray function with the custom input
result = max_subarray(arr)  # Calculate the maximum subarray sum

# Print the result
print(f"The maximum subarray sum is: {result}")  # Display the result to the user
