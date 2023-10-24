def countWaysToMakeChange(arr, n, T):
    # Initialize a list 'prev' to store the number of ways for different target amounts
    prev = [0] * (T + 1)

    # Initialize the base condition for the first element in the array
    for i in range(T + 1):
        if i % arr[0] == 0:
            prev[i] = 1
    # Else condition is automatically fulfilled, as 'prev' is initialized to zeros.

    # Iterate through the array elements and target amounts
    for ind in range(1, n):
        # Initialize a list 'cur' to store the number of ways for the current element
        cur = [0] * (T + 1)
        for target in range(T + 1):
            # Calculate the number of ways when the current element is not taken
            notTaken = prev[target]

            # Initialize a variable for the number of ways when the current element is taken
            taken = 0
            if arr[ind] <= target:
                taken = cur[target - arr[ind]]

            # Store the total number of ways in 'cur'
            cur[target] = notTaken + taken

        # Update 'prev' with the results from 'cur' for the next iteration
        prev = cur

    # Return the total number of ways for the given target amount
    return prev[T]


def main():
    arr = [1, 2, 3]
    target = 4
    n = len(arr)

    print("The total number of ways is", countWaysToMakeChange(arr, n, target))


if __name__ == "__main__":
    main()
