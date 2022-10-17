# Code Contributed by Atharv Patil, 2nd year, IIIT Pune
# kadanes algorithm calculates maximum subarray sum in O(n) time complexity and
# O(1) auxiliary space complexity


def kadane(array: list[int]) -> int:
    """
    >>> kadane([1,2,3,5,6,-144,1,3,5,10])
    19
    >>> kadane([1,-2,1,1,4,5,6,1,-1,9,10])
    36
    >>> kadane([5,6,-10,1,2,3,5,-3,6,-134,1,45])
    46
    """
    n = len(array)  # Initialization of n as length of array.
    mxsm = float("-inf")  # Initialization of mxsm as negative infinity.
    tempsm = 0  # Initialization of tempsm as 0.

    for i in range(n):

        tempsm += array[i]

        if tempsm > mxsm:  # mxsm will take the value of tempsm whenever
            mxsm = tempsm  # tempsm will exceed it.

        if tempsm < 0:  # tempsm will be 0 whenever it becomes negative
            tempsm = 0

    return mxsm


if __name__ == "__main__":
    import doctest
    doctest.testmod()
