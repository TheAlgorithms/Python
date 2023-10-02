# function to check if all the bits
# are set or not in the binary
# representation of 'x'
def allbitsareset(x) -> bool:
    # if true, then all bits are set
    if ((x + 1) & x) == 0:
        return True

    # else all bits are not set
    return False


# Function to check if a number
# has bits in alternate pattern
def bitsareinlltorder(x) -> bool:
    num = x ^ (x >> 1)

    # To check if all bits are set in 'num'
    return allbitsareset(num)

"""
>>> Input :  15
>>> Output :  No
>>> Explanation: Binary representation of 15 is 1111.
"""
