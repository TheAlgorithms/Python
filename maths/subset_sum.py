# Test to see if a subset of a given set can add up to a given Sum

# Returns true if there is a subset of that set with a sum equal to the parameter sum
# Returns false if you cannot add two numbers in the set to create the passed sum

#array must be an array
#desired_sum must be an int

def Sum_InSubset(array: list, desired_sum: int) -> None:

    """
    In an array see if a subset adds up to a sum

    :param array: list
    :param desired_sum: int
    :return: boolean

    >>> is_Subset_For_Sum((1,2,5,6),7)
    True
    """

    try:
        array = list(array)
    except:
        raise ValueError("Parameter 1, invalid file type. Value should be list")  

    try:
        sumToCheckAgainst = int(desired_sum)
    except:
        raise ValueError("Parameter 2, invalid file type. Value should be int")  
        
    

    num_Array = len(array)
    
    """
    The value of subset[i][ii] will be true when there's
    a subset of set[0..ii-1] with sum equal to i
    """

    subset = [
        [False for i in range(desired_sum + 1)]
        for i in range(num_Array + 1)
    ]

    # If sumToCheckAgainst is 0, then answer is true
    for i in range(num_Array + 1):
        subset[i][0] = True

    # If sumToCheckAgainst is not 0 and set is empty,
    # then answer is false
    for i in range(1, desired_sum + 1):
        subset[0][i] = False

    # Fill the subset table in bottom up manner
    for i in range(1, num_Array + 1):
        for ii in range(1, desired_sum + 1):
            if ii < array[i - 1]:
                subset[i][ii] = subset[i - 1][ii]
            if ii >= array[i - 1]:
                subset[i][ii] = subset[i - 1][ii] or subset[i - 1][ii - array[i - 1]]

    return subset[num_Array][desired_sum]


if __name__ == "__main__":
    import doctest
    doctest.testmod()