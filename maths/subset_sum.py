# Test to see if a subset of a given set can add up to a given Sum

# Returns true if there is a subset of that set with a sum equal to the parameter sum
# Returns false if you cannot add two numbers in the set to create the passed sum


def isSubsetForSum(set, sum):
    numOfItemsinArray = len(set)
    """
    The value of subset[i][ii] will be true when there's
    a subset of set[0..ii-1] with sum equal to i
    """

    subset = [[False for i in range(sum + 1)] for i in range(numOfItemsinArray + 1)]

    # If sum is 0, then answer is true
    for i in range(numOfItemsinArray + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False

    # Fill the subset table in bottom up manner
    for i in range(1, numOfItemsinArray + 1):
        for ii in range(1, sum + 1):
            if ii < set[i - 1]:
                subset[i][ii] = subset[i - 1][ii]
            if ii >= set[i - 1]:
                subset[i][ii] = subset[i - 1][ii] or subset[i - 1][ii - set[i - 1]]

    return subset[numOfItemsinArray][sum]
