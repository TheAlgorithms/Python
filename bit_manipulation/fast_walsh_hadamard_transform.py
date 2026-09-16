"""
Fast Walsh-Hadamard Transform (FWHT) for Bitwise Convolutions.

Reference: https://en.wikipedia.org/wiki/Fast_Walsh%E2%80%93Hadamard_transform
Reference: https://cp-algorithms.com/algebra/walsh-hadamard-transform.html

Computes bitwise XOR, AND, and OR convolutions of two numeric sequences in O(N log N)
time, where N is a positive power of 2.
"""


def fwht_xor(sequence: list[int], inverse: bool = False) -> list[int]:
    """
    Perform Fast Walsh-Hadamard Transform (or inverse) for XOR operation.

    Time Complexity: O(N log N)

    >>> fwht_xor([1, 2, 3, 4])
    [10, -2, -4, 0]
    >>> fwht_xor([10, -2, -4, 0], inverse=True)
    [1, 2, 3, 4]
    >>> fwht_xor([1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Length of sequence must be a positive power of 2.
    >>> fwht_xor([])
    Traceback (most recent call last):
        ...
    ValueError: Length of sequence must be a positive power of 2.
    >>> fwht_xor([1, 2, 3, 5], inverse=True)
    Traceback (most recent call last):
        ...
    ValueError: Inverse XOR transform requires elements divisible by sequence length.
    """
    sequence_length = len(sequence)
    if sequence_length == 0 or (sequence_length & (sequence_length - 1)) != 0:
        raise ValueError("Length of sequence must be a positive power of 2.")

    result = list(sequence)
    half_block = 1
    while half_block < sequence_length:
        block_size = half_block * 2
        for block_start in range(0, sequence_length, block_size):
            for offset in range(half_block):
                left_index = block_start + offset
                right_index = left_index + half_block
                left_val = result[left_index]
                right_val = result[right_index]
                result[left_index] = left_val + right_val
                result[right_index] = left_val - right_val
        half_block *= 2

    if inverse:
        if any(element % sequence_length != 0 for element in result):
            raise ValueError(
                "Inverse XOR transform requires elements divisible by sequence length."
            )
        result = [element // sequence_length for element in result]
    return result


def xor_convolution(sequence_a: list[int], sequence_b: list[int]) -> list[int]:
    """
    Compute bitwise XOR convolution C[k] = sum_{i ^ j = k} (A[i] * B[j]).

    Time Complexity: O(N log N)

    >>> xor_convolution([1, 2], [3, 4])
    [11, 10]
    >>> xor_convolution([1, 2], [3])
    Traceback (most recent call last):
        ...
    ValueError: Input sequences must have equal length.
    """
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Input sequences must have equal length.")

    transformed_a = fwht_xor(sequence_a)
    transformed_b = fwht_xor(sequence_b)
    pointwise_product = [
        transformed_a[index] * transformed_b[index] for index in range(len(sequence_a))
    ]
    return fwht_xor(pointwise_product, inverse=True)


def fwht_or(sequence: list[int], inverse: bool = False) -> list[int]:
    """
    Perform Fast Walsh-Hadamard Transform for OR operation.

    Time Complexity: O(N log N)

    >>> fwht_or([1, 2])
    [1, 3]
    >>> fwht_or([1, 3], inverse=True)
    [1, 2]
    >>> fwht_or([1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Length of sequence must be a positive power of 2.
    """
    sequence_length = len(sequence)
    if sequence_length == 0 or (sequence_length & (sequence_length - 1)) != 0:
        raise ValueError("Length of sequence must be a positive power of 2.")

    result = list(sequence)
    half_block = 1
    while half_block < sequence_length:
        block_size = half_block * 2
        for block_start in range(0, sequence_length, block_size):
            for offset in range(half_block):
                left_index = block_start + offset
                right_index = left_index + half_block
                if not inverse:
                    result[right_index] += result[left_index]
                else:
                    result[right_index] -= result[left_index]
        half_block *= 2

    return result


def or_convolution(sequence_a: list[int], sequence_b: list[int]) -> list[int]:
    """
    Compute bitwise OR convolution C[k] = sum_{i | j = k} (A[i] * B[j]).

    Time Complexity: O(N log N)

    >>> or_convolution([1, 2], [3, 4])
    [3, 18]
    >>> or_convolution([1, 2], [3])
    Traceback (most recent call last):
        ...
    ValueError: Input sequences must have equal length.
    """
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Input sequences must have equal length.")

    transformed_a = fwht_or(sequence_a)
    transformed_b = fwht_or(sequence_b)
    pointwise_product = [
        transformed_a[index] * transformed_b[index] for index in range(len(sequence_a))
    ]
    return fwht_or(pointwise_product, inverse=True)


def fwht_and(sequence: list[int], inverse: bool = False) -> list[int]:
    """
    Perform Fast Walsh-Hadamard Transform for AND operation.

    Time Complexity: O(N log N)

    >>> fwht_and([1, 2])
    [3, 2]
    >>> fwht_and([3, 2], inverse=True)
    [1, 2]
    >>> fwht_and([1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Length of sequence must be a positive power of 2.
    """
    sequence_length = len(sequence)
    if sequence_length == 0 or (sequence_length & (sequence_length - 1)) != 0:
        raise ValueError("Length of sequence must be a positive power of 2.")

    result = list(sequence)
    half_block = 1
    while half_block < sequence_length:
        block_size = half_block * 2
        for block_start in range(0, sequence_length, block_size):
            for offset in range(half_block):
                left_index = block_start + offset
                right_index = left_index + half_block
                if not inverse:
                    result[left_index] += result[right_index]
                else:
                    result[left_index] -= result[right_index]
        half_block *= 2

    return result


def and_convolution(sequence_a: list[int], sequence_b: list[int]) -> list[int]:
    """
    Compute bitwise AND convolution C[k] = sum_{i & j = k} (A[i] * B[j]).

    Time Complexity: O(N log N)

    >>> and_convolution([1, 2], [3, 4])
    [13, 8]
    >>> and_convolution([1, 2], [3])
    Traceback (most recent call last):
        ...
    ValueError: Input sequences must have equal length.
    """
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Input sequences must have equal length.")

    transformed_a = fwht_and(sequence_a)
    transformed_b = fwht_and(sequence_b)
    pointwise_product = [
        transformed_a[index] * transformed_b[index] for index in range(len(sequence_a))
    ]
    return fwht_and(pointwise_product, inverse=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
