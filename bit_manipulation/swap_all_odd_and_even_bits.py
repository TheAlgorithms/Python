def swap_odd_even_bits(num):
    # Get all even bits
    even_bits = (
        num & 0xAAAAAAAA
    )  # 0xAAAAAAAA is a 32-bit number with all even bits set to 1

    # Get all odd bits
    odd_bits = (
        num & 0x55555555
    )  # 0x55555555 is a 32-bit number with all odd bits set to 1

    # Right shift even bits by 1 and left shift odd bits by 1 to swap them
    even_bits >>= 1
    odd_bits <<= 1

    # Combine the swapped even and odd bits
    result = even_bits | odd_bits

    return result


# Example usage:
num = 23  # Binary: 10111
swapped_num = swap_odd_even_bits(num)  # Result: 43 (Binary: 101011)
print(swapped_num)

# In this code:

# 1. We use bitwise AND operations to separate the even bits (0, 2, 4, 6, etc.) and odd bits (1, 3, 5, 7, etc.) in the input number.
# 2. We then right-shift the even bits by 1 position and left-shift the odd bits by 1 position to swap them.
# 3. Finally, we combine the swapped even and odd bits using a bitwise OR operation to obtain the final result.
