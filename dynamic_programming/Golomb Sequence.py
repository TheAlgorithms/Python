# Python 3 Program to find first
# n terms of Golomb sequence.
 
# Return the nth element of
# Golomb sequence
def findGolomb(n):
 
    # base case
    if (n == 1):
        return 1
 
    # Recursive Step
    return 1 + findGolomb(n -
    findGolomb(findGolomb(n - 1)))
 
 
# Print the first n term
# of Golomb Sequence
def printGolomb(n):
 
    # Finding first n terms of
    # Golomb Sequence.
    for i in range(1, n + 1):
        print(findGolomb(i), end=" ")
 
# Driver Code
n = 9
 
printGolomb(n)
