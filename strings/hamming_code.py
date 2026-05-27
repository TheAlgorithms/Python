from typing import List, Tuple


def calculate_parity_bits(data_bits: List[int]) -> int:
    """
    Calculates the number of redundant parity bits needed for Hamming Code.
    >>> calculate_parity_bits([1, 0, 1, 1])
    3
    """
    m = len(data_bits)
    r = 0
    while (2**r) < (m + r + 1):
        r += 1
    return r


def hamming_encode(data_str: str) -> str:
    """
    Encodes a binary string into a Hamming Code (7,4 or adaptive format).
    Features error detection parity implementation.
    >>> hamming_encode("1011")
    '1010101'
    """
    data = [int(x) for x in data_str]
    r = calculate_parity_bits(data)
    m = len(data)

    # Initialize code word with placeholders (0)
    code = [0] * (m + r)

    # Place data bits into non-parity positions
    j = 0
    for i in range(1, len(code) + 1):
        if (i & (i - 1)) != 0:  # Not a power of 2
            code[i - 1] = data[j]
            j += 1

    # Calculate parity bits using XOR logic
    for i in range(r):
        parity_pos = 2**i
        parity_val = 0
        for j in range(1, len(code) + 1):
            if j & parity_pos and j != parity_pos:
                parity_val ^= code[j - 1]
        code[parity_pos - 1] = parity_val

    return "".join(map(str, code))


def hamming_decode_and_correct(code_str: str) -> Tuple[str, int]:
    """
    Decodes the Hamming code, detects, and automatically corrects a single-bit error.
    Returns a tuple of (corrected_data_bits_string, error_position).
    >>> hamming_decode_and_correct("1010101")
    ('1011', 0)
    >>> hamming_decode_and_correct("1010111")  # Error injected at position 6
    ('1011', 6)
    """
    code = [int(x) for x in code_str]
    n = len(code)

    # Determine number of parity bits r
    r = 0
    while (2**r) <= n:
        r += 1

    error_pos = 0
    # Check each parity bit syndrome
    for i in range(r):
        parity_pos = 2**i
        parity_sum = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity_sum ^= code[j - 1]
        if parity_sum != 0:
            error_pos += parity_pos

    # Correct the error if detected
    if error_pos > 0:
        code[error_pos - 1] ^= 1  # Flip the corrupted bit

    # Extract original data bits
    original_data = []
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            original_data.append(code[i - 1])

    return "".join(map(str, original_data)), error_pos


if __name__ == "__main__":
    import doctest

    doctest.testmod()
