# Converting Octal number to Binary

# defining a function that returns
# binary equivalent of the number
def octal_to_binary(oct_num: int) -> int:

    """
    >>> octal_to_binary(1)
    '001'
    >>> octal_to_binary(12)
    '001010'
    >>> octal_to_binary(2)
    '010'
    >>> octal_to_binary(8)
    Traceback (most recent call last):
    ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary(19)
    Traceback (most recent call last):
    ...
    ValueError: Non-octal value was passed to the function

    """

    binary = ""  # initialising bin as String

    # While loop to extract each digit
    while oct_num != 0:

        # extracting each digit
        d = int(oct_num % 10)
        if d == 0:
            # concatenation of string using join function
            binary = "".join(["000", binary])

        elif d == 1:
            # concatenation of string using join function
            binary = "".join(["001", binary])

        elif d == 2:
            # concatenation of string using join function
            binary = "".join(["010", binary])

        elif d == 3:
            # concatenation of string using join function
            binary = "".join(["011", binary])

        elif d == 4:
            # concatenation of string using join function
            binary = "".join(["100", binary])

        elif d == 5:
            # concatenation of string using join function
            binary = "".join(["101", binary])

        elif d == 6:
            # concatenation of string using join function
            binary = "".join(["110", binary])

        elif d == 7:
            # concatenation of string using join function
            binary = "".join(["111", binary])

        else:
            # an option for invalid input
            raise ValueError("Non-octal value was passed to the function")
            break

        # updating the oct for while loop
        oct_num = int(oct_num / 10)

    # returning the string binary that stores
    # binary equivalent of the number
    return binary


# Driver Code
print("Enter the Octal Number")

try:
    oct_num = int(input())
except ValueError:
    print("Please enter an integer.")
    exit()

# value of function stored final_bin
final_bin = "" + octal_to_binary(oct_num)

# result is printed
print("Equivalent Binary Value =", final_bin)

if __name__ == "__main__":
    from doctest import testmod

testmod()
