# Print all subset combinations of n element in given set of r element.


def combination_util(arr, n, r, index, data, i):
    """
    Current combination is ready to be printed, print it
    arr[]  ---> Input Array
    data[] ---> Temporary array to store current combination
    start & end ---> Staring and Ending indexes in arr[]
    index  ---> Current index in data[]
    r ---> Size of a combination to be printed
    """
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    #  When no more elements are there to put in data[]
    if i >= n:
        return
    # current is included, put next at next location
    data[index] = arr[i]
    combination_util(arr, n, r, index + 1, data, i + 1)
    # current is excluded, replace it with
    # next (Note that i+1 is passed, but
    # index is not changed)
    combination_util(arr, n, r, index, data, i + 1)
    # The main function that prints all combinations
    # of size r in arr[] of size n. This function
    # mainly uses combinationUtil()


def print_combination(arr, n, r):
    # A temporary array to store all combination one by one
    data = [0] * r
    # Print all combination using temporary array 'data[]'
    combination_util(arr, n, r, 0, data, 0)


# Driver function to check for above function
arr = [10, 20, 30, 40, 50]
print_combination(arr, len(arr), 3)
# This code is contributed by Ambuj sahu
