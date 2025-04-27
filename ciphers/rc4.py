"""
Implementation of RC4 (Rivest Cipher 4) stream cipher algorithm.

Reference:
- https://en.wikipedia.org/wiki/RC4
"""


def ksa(key: bytes) -> list[int]:
    """
    Key Scheduling Algorithm (KSA) for RC4.

    Args:
        key: The secret key as bytes.

    Returns:
        A permutation (list) of 256 integers (S-box).

    Example:
    >>> ksa(b'Key')[:5]
    [0, 1, 2, 3, 4]
    """
    key_length = len(key)
    s_box = list(range(256))
    j = 0

    for i in range(256):
        j = (j + s_box[i] + key[i % key_length]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]

    return s_box


def prga(s_box: list[int], message_length: int) -> list[int]:
    """
    Pseudo-Random Generation Algorithm (PRGA) for RC4.

    Args:
        s_box: The S-box after KSA.
        message_length: Number of bytes to generate.

    Returns:
        A keystream as a list of integers.

    Example:
    >>> prga(list(range(256)), 5)
    [0, 1, 2, 3, 4]
    """
    i = 0
    j = 0
    keystream = []

    for _ in range(message_length):
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        k = s_box[(s_box[i] + s_box[j]) % 256]
        keystream.append(k)

    return keystream


def rc4(key: bytes, data: bytes) -> bytes:
    """
    Encrypt or decrypt data using RC4 stream cipher.

    Args:
        key: The secret key as bytes.
        data: The plaintext or ciphertext as bytes.

    Returns:
        Encrypted or decrypted output as bytes.

    Example:
    >>> ciphertext = rc4(b'Key', b'Plaintext')
    >>> rc4(b'Key', ciphertext)
    b'Plaintext'
    """
    s_box = ksa(key)
    keystream = prga(s_box, len(data))
    output = bytes(
        [
            data_byte ^ keystream_byte
            for data_byte, keystream_byte in zip(data, keystream)
        ]
    )
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt data using RC4 cipher."
    )
    parser.add_argument(
        "mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt"
    )
    parser.add_argument("key", type=str, help="Encryption/Decryption key")
    parser.add_argument("input", type=str, help="Input text")

    args = parser.parse_args()

    key_bytes = args.key.encode("ascii")
    input_bytes = args.input.encode("ascii")

    result_bytes = rc4(key_bytes, input_bytes)

    if args.mode == "encrypt":
        print(result_bytes.hex())
    else:  # decrypt mode
        try:
            # if user passed hex data, decode it
            input_bytes = bytes.fromhex(args.input)
            result_bytes = rc4(key_bytes, input_bytes)
            print(result_bytes.decode("ascii"))
        except ValueError:
            print("Error: Input must be valid hex string when decrypting.")
