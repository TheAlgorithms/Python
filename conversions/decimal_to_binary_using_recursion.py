# This function converts positive integer values to their binary equivalent
def bin_recursive(decimal: int) -> str:
    """
    Converts a positive integer decimal number to its binary equivalent using recursion.
    The funtion takes in an integer number via the parameter "decimal" and returns a string.
    """
    # Initialize exit base of the recursion function
    if decimal == 1 or decimal == 0: return str(decimal)
    
    half = decimal // 2
    remainder = decimal % 2
    return bin_recursive(half) + str(remainder)

# This funtion handles wrong inputs, calls the funtion above, adds "0b" & "-0b" to positive and negative decimal inputs respectively and then prints out the output.
def main(number) -> str:
    try:
        # try converting number to an integer
        number = int(number)
    except Exception:
        # Handle exception raised and return nothing
        print("Input value is not an integer")
        return
    
    if number < 0:
        number = -number
        print("-0b" + bin_recursive(number))
    else: print("0b" + bin_recursive(number))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
