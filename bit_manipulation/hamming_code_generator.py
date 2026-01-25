"""
Author: Ayush Chakraborty
Date: 6th October 2024

generate (15,11) hamming encoded bits gives 11 bit data

input: 11 bit binary number with type string
return: 16 bit binary hamming encoded number returned in string form
"""


def hamming_15_11(number: str) -> str:
    """
    Performs parity checks to assign values to the redundant bits,
    in the 16 bit number
    returned, bits at index 0, 1, 2, 4, 8 are redundant bits used for checking

    Hamming generated 16 bits generated from the 11 bit binary number can only detect
    and change a single bit change, but can only detect more than a
    single bit change

    for more theoretical knowledege about Hamming codes, refer:
    https://www.youtube.com/watch?v=X8jsijhllIA&t=0s
    by 3B1B YT channel

    Wikipedia:
    https://en.wikipedia.org/wiki/Hamming_code

    >>> hamming_15_11("00110001110")
    '0010101110001110'
    >>> hamming_15_11("10110000110")
    '0101001100000110'
    >>> hamming_15_11("10111100110")
    '0011001101100110'
    >>> hamming_15_11("10001000010")
    '0001100001000010'
    >>> hamming_15_11("00010abcdef")
    "Input must be an 11-bit binary string containing only '0's and '1's."

    """
    is_bin = True  # assuming it's binary initially
    for i in number:
        if i not in ("0", "1"):
            is_bin = False
            break

    if len(number) == 11 and is_bin:
        digits = [int(number[i]) for i in range(len(number))]

        total_ones = sum(digits)
        hamming_digits = [0] * 16

        parity_positions = {
            1: [0, 1, 3, 4, 6, 8, 10],
            2: [0, 2, 3, 5, 6, 9, 10],
            4: [1, 2, 3, 7, 8, 9, 10],
            8: [4, 5, 6, 7, 8, 9, 10],
        }

        redundant_bits = [0] * 5

        redundant_bits_index = 1
        for positions in parity_positions.values():
            parity = 0
            for idx in positions:
                parity ^= digits[idx]
            redundant_bits[redundant_bits_index] = parity
            redundant_bits_index += 1

        redundant_bits[0] = (
            total_ones % 2
            ^ redundant_bits[1]
            ^ redundant_bits[2]
            ^ redundant_bits[3]
            ^ redundant_bits[4]
        )

        data_index = 0
        redundant_bit_locations = [0, 1, 2, 4, 8]
        for k in range(16):
            if k in redundant_bit_locations:
                hamming_digits[k] = redundant_bits.pop(0)
            else:
                hamming_digits[k] = digits[data_index]
                data_index += 1

        return "".join([str(i) for i in hamming_digits])

    elif len(number) != 11 or not is_bin:
        return "Input must be an 11-bit binary string containing only '0's and '1's."

    else:
        return "Invalid input"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
