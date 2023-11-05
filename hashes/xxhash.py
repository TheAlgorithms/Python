# Author: Your Name
# Author email: your.email@example.com
# Coding date: Month Year
# Black: True

"""
    * This code implements the xxHash algorithm:
        https://github.com/Cyan4973/xxHash

    * xxHash is an extremely fast non-cryptographic hash algorithm that can be used
      to hash data for various applications like hash tables, checksums, and more.

    * The implemented code consists of:
        * A function for calculating the xxHash hash value for given data.

    * How to use:
        You can use the `xxhash` function to calculate the hash value for your data.

    * Example:
        data = b'Hello, World!'
        seed = 0
        hash_value = xxhash(data, seed)
        print(f'Hash value: {hash_value}')

"""

# Constants
PRIME32_1 = 0x9E3779B1
PRIME32_2 = 0x85EBCA77
PRIME32_3 = 0xC2B2AE3D
PRIME32_4 = 0x27D4EB2F
PRIME32_5 = 0x165667B1


def xxhash(data, seed=0):
    """
    Calculate the xxHash hash value for the given data.

    :param data: Data to be hashed (bytes)
    :param seed: Seed value for the hash (integer)
    :return: xxHash hash value (integer)

    >>> data = b'Hello, World!'
    >>> seed = 0
    >>> xxhash(data, seed)
    133790109
    """
    length = len(data)
    if length >= 16:
        v1 = seed + PRIME32_1 + PRIME32_2
        v2 = seed + PRIME32_2
        v3 = seed
        v4 = seed - PRIME32_1
        p = 0
        end = length - 16
        while p <= end:
            input_bytes = data[p : p + 16]
            input_ints = list(
                int.from_bytes(input_bytes, byteorder="little", signed=False)
                for i in range(16)
            )
            v1 += input_ints[0] * PRIME32_2
            v1 = (v1 << 13) | (v1 >> 19)
            v1 *= PRIME32_1
            v2 += input_ints[1] * PRIME32_2
            v2 = (v2 << 13) | (v2 >> 19)
            v2 *= PRIME32_1
            v3 += input_ints[2] * PRIME32_2
            v3 = (v3 << 13) | (v3 >> 19)
            v3 *= PRIME32_1
            v4 += input_ints[3] * PRIME32_2
            v4 = (v4 << 13) | (v4 >> 19)
            v4 *= PRIME32_1
            p += 16

        hash_value = (
            ((v1 << 1) | (v1 >> 31))
            + ((v2 << 7) | (v2 >> 25))
            + ((v3 << 12) | (v3 >> 20))
            + ((v4 << 18) | (v4 >> 14))
        )
    else:
        hash_value = seed + PRIME32_5

    hash_value += length
    p = 0
    end = length
    while p <= end - 4:
        chunk = data[p : p + 4]
        chunk_value = int.from_bytes(chunk, byteorder="little", signed=False)
        hash_value += chunk_value * PRIME32_3
        hash_value = ((hash_value << 17) | (hash_value >> 15)) * PRIME32_4
        p += 4

    while p < end:
        chunk_value = data[p]
        hash_value += chunk_value * PRIME32_5
        hash_value = ((hash_value << 11) | (hash_value >> 21)) * PRIME32_1
        p += 1

    hash_value ^= hash_value >> 15
    hash_value *= PRIME32_2
    hash_value ^= hash_value >> 13
    hash_value *= PRIME32_3
    hash_value ^= hash_value >> 16
    return hash_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
