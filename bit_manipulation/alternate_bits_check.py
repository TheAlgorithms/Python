# function to check if all the bits
# are set or not in the binary
# representation of 'x'
def allbitsareset(x):
    # if true, then all bits are set
    if ((x + 1) & x) == 0:
        return True

    # else all bits are not set
    return False


# Function to check if a number
# has bits in alternate pattern
def bitsareinlltorder(x):
    num = x ^ (x >> 1)

    # To check if all bits are set in 'num'
    return allbitsareset(num)
