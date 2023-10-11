# Return all subset combinations of n element in given set of r element.


def combination_util(arr, n, r, index, data, i):
    """
    Current combination is ready to be returned, return it
    arr[]  ---> Input Array
    data[] ---> Temporary array to store current combination
    start & end ---> Staring and Ending indexes in arr[]
    index  ---> Current index in data[]
    r ---> Size of a combination to be returned
    """
    if index == r:
        return tuple(data)
    #  When no more elements are there to put in data[]
    if i >= n:
        return None
    # current is included, put next at next location
    data[index] = arr[i]
    res1 = combination_util(arr, n, r, index + 1, data, i + 1)
    # current is excluded, replace it with
    # next (Note that i+1 is passed, but
    # index is not changed)
    res2 = combination_util(arr, n, r, index, data, i + 1)
    if res1 is None:
        return res2
    elif res2 is None:
        return res1
    else:
        return res1, res2


def get_combinations(arr, n, r):
    # A temporary array to store all combination one by one
    data = [0] * r
    # Return all combination using temporary array 'data[]'
    return combination_util(arr, n, r, 0, data, 0)


if __name__ == "__main__":
    # Driver code to check the function above
    arr = [10, 20, 30, 40, 50]
    print(get_combinations(arr, len(arr), 3))
    # This code is contributed by Ambuj sahu
