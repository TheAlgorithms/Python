import struct

def fast_inverse_square_root(number):
    threehalfs = 1.5

    # Convert the input number to a 32-bit float
    i = struct.unpack('I', struct.pack('f', number))[0]

    # Initial guess for the square root (using bit manipulation)
    i = 0x5f3759df - (i >> 1)

    # Convert the modified bits back to a float
    number = struct.unpack('f', struct.pack('I', i))[0]

    # Newton-Raphson iteration for increased accuracy
    number = number * (threehalfs - (0.5 * number * number))

    return number

# Example usage
if __name__ == "__main__":
    input_number = 4.0  # Replace with the number you want to find the inverse square root of
    result = fast_inverse_square_root(input_number)
    print("Fast Inverse Square Root:", result)
    print("Actual Inverse Square Root:", 1 / (input_number ** 0.5))
