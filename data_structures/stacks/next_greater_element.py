# Function to print element and Next Greatest Element (NGE) pair for all elements of list
# NGE - Maximum element present afterwards the current one which is also greater than current one
def printNGE(arr):

    for i in range(0, len(arr), 1):

        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break

        print(str(arr[i]) + " -- " + str(next))


# Driver program to test above function
'''
For the given list the ouput should be something like this:
11 -- 21
13 -- 21
21 -- -1
3 -- -1
'''
arr = [11, 13, 21, 3]
printNGE(arr)
