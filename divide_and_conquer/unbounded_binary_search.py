# A monotonically not increasing function f(x) = 3x - 100
def f(x):
    return 3 * x - 100


# Find the value of x in the search space [low, high] using binary search
# where f(x) becomes positive for the first time
def binarySearch(low, high):

    # Base condition (search space is exhausted)
    if high < low:
        return -1

    # we find the mid value in the search space
    mid = low + ((high - low) / 2)

    # if f(mid) is positive
    if f(mid) > 0:

        # return mid if it is first element of the search space or
        # when f(mid-1) is not positive
        if mid == low or f(mid - 1) <= 0:
            return mid

        # else discard all elements in the right search space
        return binarySearch(low, mid - 1)

    # if f(mid) is zero or negative,
    # discard all elements in the left search space
    return binarySearch(mid + 1, high)


# Returns the positive value x where f(x) becomes positive for the first time
def exponentialSearch():

    # find the range in which the result would reside
    i = 1
    while f(i) <= 0:
        # calculate the next power of 2
        i *= 2

    # call binary search on [i/2, i]
    return binarySearch(i / 2, i)


if __name__ == '__main__':

    x = exponentialSearch()
    print("f(x) becomes positive for the first time when x =", int(x))
