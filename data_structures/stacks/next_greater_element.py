def printNGE(arr):
    """
    Function to print element and Next Greatest Element (NGE) pair for all elements of list
    NGE - Maximum element present afterwards the current one which is also greater than current one
    >>> printNGE([11,13,21,3])
    11 -- 13
    13 -- 21
    21 -- -1
    3 -- -1
    
    Naive way to solve this is to take two loops and check for the next bigger number but that will make the
    time complexity as O(n^2). The better way to solve this would be to use a stack to keep track of maximum
    number givig a linear time complex solution.
    
    """
    stack = []              
    result = [-1]*len(arr)
    
    for index in reversed(range(len(arr))):
        if len(stack):
            while stack[-1] < arr[index]:
                stack.pop()
                if len(stack) == 0:
                    break
                    
        if len(stack) != 0:
            result[index] = stack[-1]
            
        stack.append(arr[index])
        
    for x in range(len(arr)):
        print("{} -- {}".format(arr[x], result[x]))

# Driver program to test above function
arr = [11, 13, 21, 3]
printNGE(arr)
