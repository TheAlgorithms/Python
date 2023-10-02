# function to check if all the bits
# are set or not in the binary
# representation of 'input_number'
def allbitsareset(input_number) -> bool:
    # if true, then all bits are set
    if ((input_number + 1) & input_number) == 0:
        return True

    # else all bits are not set
    return False


# Function to check if a number
# has bits in alternate pattern
def bitsareinlltorder(input_number) -> bool:
    result_number = input_number ^ (input_number >> 1)

    # To check if all bits are set in 'num'
    return allbitsareset(result_number)
    
input_by_user = 15

if (bitsAreInAltOrder(input_by_user)):
    print("Yes");
else:
    print("No");


"""
>>> Input :  15
>>> Output :  No
>>> Explanation: Binary representation of 15 is 1111.
"""
