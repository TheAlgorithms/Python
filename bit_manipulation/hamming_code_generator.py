""" "
Author: Ayush Chakraborty
Date: 6th October 2024

generate (15,11) hamming encoded bits gives 11 bit data

input: 11 bit binary number with type string
return: 16 bit binary hamming encoded number returned in string form
"""

from functools import reduce

def hamming_15_11(number: str) -> str:
    """
    Performs parity checks to assign values to the redundant bits, 
    in the 16 bit number
    returned, bits at index 0, 1, 2, 4, 8 are redundant bits used for checking

    Hamming generated 16 bits generated from the 11 bit binary number can only detect 
    and change a single bit change, but can only detect more than a 
    single bit change

    for more theoretical knowledege about Hamming codes, refer: 
    https://www.youtube.com/watch?v=X8jsijhllIA&t=143s
    by 3B1B YT channel

    >>> hamming_15_11("00110001110")
    '0010101110001110'
    >>> hamming_15_11("10110000110")
    '0101001100000110'
    >>> hamming_15_11("10111100110")
    '0011001101100110'
    >>> hamming_15_11("10001000010")
    '0001100001000010'

    """
    if len(number) == 11:
        digits = [0 if number[i] == "0" else 1 for i in range(len(number))]
        total_num_1 = sum(digits)
        hamming_digits = [0 for i in range(16)]
        bit_1 = reduce(
            lambda temp_bit1, temp_bit2: temp_bit1 ^ temp_bit2,
            [
                digits[1],
                digits[4],
                digits[8],
                digits[0],
                digits[3],
                digits[6],
                digits[10],
            ],
        )
        bit_2 = reduce(
            lambda temp_bit1, temp_bit2: temp_bit1 ^ temp_bit2,
            [
                digits[2],
                digits[5],
                digits[9],
                digits[0],
                digits[3],
                digits[6],
                digits[10],
            ],
        )
        bit_3 = reduce(
            lambda temp_bit1, temp_bit2: temp_bit1 ^ temp_bit2,
            [
                digits[1],
                digits[2],
                digits[3],
                digits[7],
                digits[8],
                digits[9],
                digits[10],
            ],
        )
        bit_4 = reduce(
            lambda temp_bit1, temp_bit2: temp_bit1 ^ temp_bit2,
            [
                digits[4],
                digits[5],
                digits[6],
                digits[7],
                digits[8],
                digits[9],
                digits[10],
            ],
        )
        bit_0 = int(total_num_1 % 2) ^ bit_1 ^ bit_2 ^ bit_3 ^ bit_4

        redundant_bits = [bit_0, bit_1, bit_2, bit_3, bit_4]

        j = -1
        r = 0
        redundant_bit_locations = [0, 1, 2, 4, 8]
        for k in range(16):
            if k in redundant_bit_locations:
                hamming_digits[k] = redundant_bits[r]
                r += 1
            else:
                j += 1
                hamming_digits[k] = digits[j]

        return "".join([str(i) for i in hamming_digits])

    else:
        return "please provide a 11 bit binary number"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
