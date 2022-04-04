def gray_code(bit_count: int) -> list:
    """
    Takes in an integer n and returns a n-bit
    gray code sequence
    An n-bit gray code sequence is a sequence of 2^n
    integers where:

    a) Every integer is between [0,2^n -1] inclusive
    b) The sequence begins with 0
    c) An integer appears at most one times in the sequence
    d)The binary representation of every pair of integers differ
       by exactly one bit
    e) The binary representation of first and last bit also
       differ by exactly one bit

    >>> gray_code(2)
    [0, 1, 3, 2]

    >>> gray_code(1)
    [0, 1]

    >>> gray_code(3)
    [0, 1, 3, 2, 6, 7, 5, 4]

    >>> gray_code(-1)
    Traceback (most recent call last):
        ...
    ValueError: The given input must be positive

    >>> gray_code(10.6)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for <<: 'int' and 'float'
    """

    # bit count represents no. of bits in the gray code
    if bit_count < 0:
        raise ValueError("The given input must be positive")

    # get the generated string sequence
    sequence = gray_code_sequence_string(bit_count)
    #
    # convert them to integers
    for i in range(len(sequence)):
        sequence[i] = int(sequence[i], 2)

    return sequence


def gray_code_sequence_string(bit_count: int) -> list:
    """
    Will output the n-bit grey sequence as a
    string of bits

    >>> gray_code_sequence_string(2)
    ['00', '01', '11', '10']

    >>> gray_code_sequence_string(1)
    ['0', '1']
    """

    # The approach is a recursive one
    # Base case achieved when either n = 0 or n=1
    if bit_count == 0:
        return ["0"]

    if bit_count == 1:
        return ["0", "1"]

    seq_len = 1 << bit_count  # defines the length of the sequence
    # 1<< n is equivalent to 2^n

    # recursive answer will generate answer for n-1 bits
    smaller_sequence = gray_code_sequence_string(bit_count - 1)

    sequence = []

    # append 0 to first half of the smaller sequence generated
    for i in range(seq_len // 2):
        generated_no = "0" + smaller_sequence[i]
        sequence.append(generated_no)

    # append 1 to second half ... start from the end of the list
    for i in reversed(range(seq_len // 2)):
        generated_no = "1" + smaller_sequence[i]
        sequence.append(generated_no)

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
