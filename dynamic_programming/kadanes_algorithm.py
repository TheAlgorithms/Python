# Code Contributed by Atharv Patil, 2nd year, IIIT Pune
# kadanes algorithm calculates maximum subarray sum in O(n) time complexity and
# O(1) space complexity


def kadane(array):
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


a = list(
    map(int, input("Enter the array: ").split())
)  # Input of the array as list in python.

print(
    "Maximum subarray sum is", kadane(a)
)  # kadane function call with the array as argument
