# python program to print all subset combination of n element in given set of r element .
# arr[]  ---> Input Array
# data[] ---> Temporary array to store current combination
# start & end ---> Staring and Ending indexes in arr[]
# index  ---> Current index in data[]
# r ---> Size of a combination to be printed
def combinationUtil(arr, n, r, index, data, i):
    # Current combination is ready to be printed,
    # print it
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    #  When no more elements are there to put in data[]
    if i >= n:
        return
    # current is included, put next at next
    # location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1, data, i + 1)
    # current is excluded, replace it with
    # next (Note that i+1 is passed, but
    # index is not changed)
    combinationUtil(arr, n, r, index, data, i + 1)
    # The main function that prints all combinations
    # of size r in arr[] of size n. This function
    # mainly uses combinationUtil()


def printcombination(arr, n, r):
    # A temporary array to store all combination
    # one by one
    data = [0] * r
    # Print all combination using temprary
    # array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)


# Driver function to check for above function
arr = [10, 20, 30, 40, 50]
printcombination(arr, len(arr), 3)
# This code is contributed by Ambuj sahu
