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
        # Instead of printing, append the combination to the list
        result.append(tuple(data[:r]))
        return
         #  When no more elements are there to put in data[]
    if i >= n:
        return
    data[index] = arr[i]
    combination_util(arr, n, r, index + 1, data, i + 1)
    combination_util(arr, n, r, index, data, i + 1)

def print_combination(arr, n, r):
    data = [0] * r
    result = []  # Initialize an empty list to store the combinations
    combination_util(arr, n, r, 0, data, 0)
    return result  # Return the list of tuples

if __name__ == "__main":
    arr = [10, 20, 30, 40, 50]
    combinations = print_combination(arr, len(arr), 3)
    for combo in combinations:
        print(combo)
#The Code is contributed by Airwakz
